# Multi-Agent-project
📈 Stock Price Agent with Visualization

📌 Overview

This project builds a multi-agent system using LangChain and yfinance to fetch stock prices and visualize them. The system consists of:

An Agent that processes user queries and fetches stock prices.

A Tool (StockTool) that interacts with the yfinance API to get real-time stock data.

A Visualization Module that plots stock price trends over the last month.

🚀 Features

✅ Fetch the latest stock closing price✅ Plot stock price trends for the last month✅ Natural language processing for ticker extraction✅ Interactive agent-based response

🛠️ Installation

Ensure you have Python installed. Then, install the dependencies:

pip install yfinance matplotlib langchain langchain-google-genai python-dotenv

🔑 Setup API Key

Create a .env file in the project directory and add:

GOOGLE_API_KEY=your_google_api_key_here

📝 Usage

Run the script:

python main.py

Then, enter queries like:

Get the stock price of Tesla
What's the latest price for AAPL?
Show me the stock data for MSFT

📊 Example Output

💰 Latest stock price for TSLA: $245.67

(Followed by a stock price chart)
