# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135,
    "NFLX": 450,    
    "NVDA": 600,    
    "INTC": 45,     
    "IBM": 170,     
    "ORCL": 110,    
    "ADBE": 520,    
    "AMD": 150,     
    "CSCO": 55,     
    "UBER": 70         
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock} : ₹{price}")