import streamlit as st
import pandas as pd
from typing import Optional
import sqlalchemy
from sqlalchemy import create_engine, text
from langchain_groq import ChatGroq
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from dotenv import load_dotenv
import os

class MySQLDatabaseAssistant:
    """A professional MySQL Database Chat Assistant with an enhanced UI."""

    def __init__(self):
        """Initialize the application."""
        load_dotenv()
        self.db_config = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'user': os.getenv('DB_USER', 'USER'),
            'password': os.getenv('DB_PASSWORD', '12345'),
            'database': os.getenv('DB_NAME', 'classicmodels')
        }
        self.groq_api_key = os.getenv('GROQ_API_KEY', '')
        self._cache = {}
        self.engine = None
        self._setup_page_config()
        self._initialize_session_state()

    def _setup_page_config(self):
        """Configure Streamlit page settings with a professional UI."""
        st.set_page_config(
            page_title="MySQL Query Assistant",
            page_icon="📊",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        # Custom CSS for a professional look
        st.markdown("""
        <style>
        /* General layout */
        .stApp {
            background: #f0f2f6;
            font-family: 'Arial', sans-serif;
        }
        .sidebar .sidebar-content {
            background: #2c3e50;
            color: white;
        }
        h1 {
            color: #2c3e50;
            font-size: 2.5em;
            text-align: center;
            margin-bottom: 20px;
        }
        .stTextInput > div > input {
            border: 1px solid #3498db;
            border-radius: 5px;
            padding: 8px;
        }
        .stButton > button {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            transition: background-color 0.3s;
        }
        .stButton > button:hover {
            background-color: #2980b9;
        }
        .chat-message {
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .user-message {
            background: #dfe6e9;
            text-align: right;
        }
        .assistant-message {
            background: #ffffff;
            text-align: left;
        }
        .dataframe-container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            margin-top: 20px;
        }
        .metric-card {
            background: #ffffff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<h1>📊 MySQL Query Assistant</h1>", unsafe_allow_html=True)

    def _initialize_session_state(self):
        """Initialize session state with a professional welcome message."""
        defaults = [
            {"role": "assistant", "content": "Hello! I'm your MySQL Query Assistant. Ask me anything about your database, such as 'List all customers' or 'Show total orders by product.'"}
        ]
        st.session_state.setdefault("messages", defaults)
        st.session_state.setdefault("query_history", [])

    def _establish_connection(self) -> Optional[SQLDatabase]:
        """Establish MySQL database connection with pooling."""
        try:
            connection_string = (
                f"mysql+pymysql://{self.db_config['user']}:{self.db_config['password']}"
                f"@{self.db_config['host']}/{self.db_config['database']}"
            )
            self.engine = create_engine(connection_string, pool_size=5, max_overflow=10)
            return SQLDatabase(self.engine)
        except sqlalchemy.exc.OperationalError as e:
            st.error(f"Database connection failed: {e}")
            return None

    def _cached_query(self, db, query: str) -> pd.DataFrame:
        """Execute query with caching."""
        if query in self._cache:
            return self._cache[query]
        
        try:
            with db.engine.connect() as connection:
                result = pd.read_sql(text(query), connection)
                self._cache[query] = result
                return result
        except sqlalchemy.exc.SQLAlchemyError as e:
            st.error(f"Query execution error: {e}")
            return pd.DataFrame()

    def _create_ai_agent(self, db: SQLDatabase):
        """Create SQL agent with Groq."""
        llm = ChatGroq(
            groq_api_key=self.groq_api_key,
            model_name="Llama3-70b-8192",
            temperature=0.1,
            streaming=True
        )
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)
        
        return create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=False,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
        )

    def _display_query_results(self, result: pd.DataFrame):
        """Display query results in a professional layout."""
        if result.empty:
            st.info("No results found for this query.")
        else:
            st.markdown("<div class='dataframe-container'>", unsafe_allow_html=True)
            styled_df = result.style.background_gradient(cmap='Blues')
            st.dataframe(styled_df, use_container_width=True)
            
            cols = st.columns(3)
            with cols[0]:
                st.markdown(f"<div class='metric-card'><b>Total Rows</b><br>{result.shape[0]}</div>", unsafe_allow_html=True)
            with cols[1]:
                st.markdown(f"<div class='metric-card'><b>Total Columns</b><br>{result.shape[1]}</div>", unsafe_allow_html=True)
            with cols[2]:
                st.markdown(f"<div class='metric-card'><b>Memory Usage</b><br>{result.memory_usage().sum() / 1024:.2f} KB</div>", unsafe_allow_html=True)
            
            csv = result.to_csv(index=False)
            st.download_button("Download as CSV", csv, "query_results.csv", "text/csv")
            st.markdown("</div>", unsafe_allow_html=True)

    def _setup_sidebar(self, db: SQLDatabase):
        """Setup sidebar for configuration and schema exploration."""
        st.sidebar.header("Database Configuration")
        self.db_config['host'] = st.sidebar.text_input("Host", self.db_config['host'])
        self.db_config['user'] = st.sidebar.text_input("Username", self.db_config['user'])
        self.db_config['password'] = st.sidebar.text_input("Password", self.db_config['password'], type="password")
        self.db_config['database'] = st.sidebar.text_input("Database", self.db_config['database'])

        st.sidebar.header("Tools")
        if st.sidebar.button("Show Schema"):
            schema = db.get_table_info()
            st.sidebar.markdown(f"**Schema Overview**\n\n{schema}")

        st.sidebar.header("Query History")
        for q in st.session_state.query_history[-5:]:  # Show last 5 queries
            st.sidebar.write(q)

    def run(self):
        """Main application workflow."""
        # Connect to database
        db = self._establish_connection()
        if not db:
            return
        
        # Setup sidebar
        self._setup_sidebar(db)

        # Create AI agent
        agent = self._create_ai_agent(db)

        # Display chat history
        for msg in st.session_state.messages:
            class_name = "user-message" if msg["role"] == "user" else "assistant-message"
            st.markdown(f"<div class='chat-message {class_name}'>{msg['content']}</div>", unsafe_allow_html=True)

        # Handle user input
        if user_query := st.chat_input("Ask a question about your database"):
            st.session_state.messages.append({"role": "user", "content": user_query})
            st.session_state.query_history.append(user_query)
            st.markdown(f"<div class='chat-message user-message'>{user_query}</div>", unsafe_allow_html=True)

            with st.spinner("Processing your query..."):
                try:
                    response = agent.run(user_query)
                    st.markdown(f"<div class='chat-message assistant-message'>{response}</div>", unsafe_allow_html=True)

                    # Extract and run SQL query if present
                    import re
                    sql_match = re.search(r'SELECT.*?;', response, re.IGNORECASE | re.DOTALL)
                    if sql_match:
                        sql_query = sql_match.group(0)
                        result = self._cached_query(db, sql_query)
                        self._display_query_results(result)

                    st.session_state.messages.append({"role": "assistant", "content": response})

                except Exception as e:
                    st.error(f"Error processing query: {e}")

def main():
    """Application entry point."""
    app = MySQLDatabaseAssistant()
    app.run()

if __name__ == "__main__":
    main()
