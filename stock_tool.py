import yfinance as yf
import matplotlib.pyplot as plt
class StockTool:
    def __init__(self):
        pass

    def get_stock_data(self, ticker):
        """Fetch stock price history."""
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1mo")  # Last month data
        return hist

    def get_latest_stock_price(self, ticker):
        """Fetch latest stock price."""
        data = self.get_stock_data(ticker)
        
        if data.empty:
            print(f"❌ No stock data found for {ticker}. Please check the symbol and try again.")
            return None
        
        latest_price = data["Close"].iloc[-1]  # Last closing price
        return latest_price

    def plot_stock_data(self, ticker):
        """Fetch and visualize stock prices."""
        data = self.get_stock_data(ticker)
        
        if data.empty:
            print(f"❌ No stock data found for {ticker}. Please check the symbol and try again.")
            return
        
        plt.figure(figsize=(10, 5))
        plt.plot(data.index, data["Close"], label=f"{ticker} Closing Prices", color="blue")
        plt.xlabel("Date")
        plt.ylabel("Stock Price (USD)")
        plt.title(f"{ticker} Stock Price Over Last Month")
        plt.legend()
        plt.grid()

        # Explicitly call show to ensure plot is displayed
        plt.show()

if __name__ == "__main__":
    tool = StockTool()
    
    # Manually input the stock ticker symbol
    ticker = "GOOGL"  # Example: Google stock ticker, change this to any valid ticker
    #"MSFT" #Example :Microsoft stock ticker, change this to any valid ticker
    
    # Get the latest stock price
    latest_price = tool.get_latest_stock_price(ticker)
    if latest_price is not None:
        print(f"💰 Latest stock price for {ticker}: ${latest_price}")

        # Plot the stock data
        tool.plot_stock_data(ticker)  # Plot the recognized stock symbol
