import os
import re
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from stock_tool import StockTool

# Load API key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini AI
llm = GoogleGenerativeAI(model="gemini-2.0-flash", api_key=GOOGLE_API_KEY)

# Create StockTool instance
stock_tool = StockTool()

# Define stock data fetching tool
def fetch_stock_price(ticker):
    """Fetches latest stock price for a given ticker."""
    data = stock_tool.get_stock_data(ticker)
    if not data.empty:
        latest_price = data["Close"][-1]  # Last closing price
        return f"Latest closing price of {ticker}: ${latest_price:.2f}"
    else:
        return f"❌ Could not fetch data for {ticker}. Please check the ticker symbol."

stock_price_tool = Tool(
    name="StockPriceFetcher",
    func=fetch_stock_price,
    description="Fetches the latest closing stock price for a given ticker."
)

# Define Agents
tools = [stock_price_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Simple agent type
    verbose=True
)

# Function to extract stock ticker from user input
def extract_ticker(user_input):
    """Extract the stock ticker symbol from the user input."""
    # Look for ticker-like patterns (e.g., "AAPL", "GOOGL", "TSLA")
    match = re.search(r'\b[A-Za-z]{1,5}\b', user_input)
    if match:
        return match.group(0)
    else:
        return None

# Test agent with dynamic user input
if __name__ == "__main__":
    # Get user input dynamically (replace this with voice input for actual speech-based queries)
    user_input = input("What is your query? Example: 'Get the stock price of Tesla' \n")

    # Extract ticker from user input
    ticker = extract_ticker(user_input)

    if ticker:
        # Agent runs to fetch stock price
        response = agent.run(f"Get the latest stock price for {ticker}")
        print(response)
    else:
        print("Could not find a valid stock ticker in your query.")
