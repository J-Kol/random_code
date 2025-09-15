import yfinance as yf
import matplotlib.pyplot as plt

# ticker = "AAPL"
# start = "2021-01-01"
# end = "2023-12-31"

ticker = input("Stock Name(like NVDA): ").upper()
data = yf.download(ticker, period="1d")
if data.empty:
    print(f"#No data found for {ticker} in the specified date range.")
    ticker = input("Stock Name(like NVDA): ").upper()
start = input("Start date (format: YYYY-MM-DD)")
end = input("End date (format: YYYY-MM-DD)")

data = yf.download(ticker, start=start, end=end)

start_price = data["Close"][0]
end_price = data["Close"][-1]
Percentage = ((end_price-start_price) / start_price) * 100

color = "green" if start_price < end_price else "red"

plt.figure(figsize=(10, 5))
plt.plot(data["Close"], color=color)
plt.title(f"{ticker} Stock Chart({Percentage}%)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.ylim(min(data["Close"]) * 0.95, max(data["Close"]) * 1.05)
plt.xticks(rotation=45)
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()