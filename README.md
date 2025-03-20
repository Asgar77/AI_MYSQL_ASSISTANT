# 🔍 MySQL Query Assistant

![Screenshot 2025-03-20 163021](https://github.com/user-attachments/assets/3a82724e-35b2-4983-981f-193c559b9c5e)


> 💬 *"Talk to your database like it's a human assistant!"*

## ✨ Features

- 🗣️ **Natural Language Queries** - Ask questions in plain English
- 🎨 **Beautiful UI** - Professional and responsive design
- 📜 **Query History** - Never lose track of your previous questions
- 🏗️ **Schema Explorer** - View your database structure with one click
- 📊 **Data Visualization** - See your results with styled tables
- 📈 **Result Analytics** - Get insights about your query results
- 💾 **Easy Export** - Download your data as CSV with one click
- ⚙️ **Simple Configuration** - Connect to any MySQL database

## 🎬 Demo

![Screenshot 2025-03-20 163055](https://github.com/user-attachments/assets/ec999695-69f4-4441-9615-560b88ec91f4)

![Screenshot 2025-03-20 163118](https://github.com/user-attachments/assets/725b49bf-0043-44f8-95c5-37f55dcf597a)


## 🚀 Quick Start

### Prerequisites

- 🐍 Python 3.8+
- 🗄️ MySQL database
- 🔑 Groq API key

### Installation

1️⃣ **Clone the repo**
```bash
git clone https://github.com/Asgar77/AI_MYSQL_ASSISTANT.git
cd mysql-query-assistant
```

2️⃣ **Set up environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3️⃣ **Create your .env file**
```bash
cp .env.example .env
# Edit .env with your database credentials and API key
```

4️⃣ **Launch the app**
```bash
streamlit run app.py
```

5️⃣ **Open your browser**
📱 Visit `http://localhost:8501` and start querying!

## 💡 Example Queries

Try asking:

- 🔸 "Show me all customers in Germany"
- 🔸 "What are the top 5 products by revenue?"
- 🔸 "How many orders were placed last month?"
- 🔸 "List all employees who haven't made a sale this year"

## 🧠 How It Works

<p align="center">
  <img src="https://via.placeholder.com/600x300.png?text=Architecture+Diagram" alt="Architecture">
</p>

1. 🗣️ You ask a question in natural language
2. 🤖 Our AI agent (powered by Groq's Llama3-70b) interprets your question
3. 🔄 The agent generates the appropriate SQL query
4. 🗄️ The query runs against your MySQL database
5. 📊 Results are beautifully displayed with helpful analytics

## 🛠️ Technology Stack

- 🖥️ **Frontend**: Streamlit
- 🧠 **AI**: LangChain + Groq (Llama3-70b)
- 🗄️ **Database**: MySQL + SQLAlchemy
- 📊 **Data Processing**: Pandas

## 📁 Project Structure

```
mysql-query-assistant/
├── 📄 app.py                   # Main application
├── 📄 requirements.txt         # Dependencies
├── 📄 .env.example             # Environment template
├── 📄 .gitignore               # Git ignore file
├── 📄 LICENSE                  # MIT License
└── 📄 README.md                # Documentation
```

## ⚙️ Configuration Options

| Setting | Description | Default |
|---------|-------------|---------|
| 🖥️ **DB_HOST** | MySQL server hostname | localhost |
| 👤 **DB_USER** | Database username | USER |
| 🔑 **DB_PASSWORD** | Database password | - |
| 📁 **DB_NAME** | Database name | classicmodels |
| 🔐 **GROQ_API_KEY** | Your Groq API key | - |

## 🔮 Future Enhancements

- 🔒 User authentication and access control
- 🌓 Dark mode theme option
- 📱 Mobile app version
- 📊 Advanced data visualization options
- 🔄 Scheduled queries and reports
- 📈 Performance optimization suggestions
- 📁 Multiple database connections

## 👥 Contributing

We ❤️ contributions! Here's how:

1. 🍴 Fork the repo
2. 🔄 Create your feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit changes (`git commit -m 'Add some amazing feature'`)
4. 📤 Push to branch (`git push origin feature/amazing-feature`)
5. 🔍 Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🎨 [Streamlit](https://streamlit.io/) for the amazing framework
- 🧠 [LangChain](https://langchain.com/) for the AI capabilities
- 🤖 [Groq](https://groq.com/) for the fast LLM API

## 📞 Contact & Support

- 🐞 Found a bug? [Open an issue](https://github.com/yourusername/mysql-query-assistant/issues)
- 💬 Questions? [Discussions](https://github.com/yourusername/mysql-query-assistant/discussions)
- 📧 Contact: your.email@example.com

---


