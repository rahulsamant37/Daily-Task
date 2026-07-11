import yfinance as yf

df = yf.download(
    "AAPL",
    start="2010-01-01",
    end="2025-01-01",
    auto_adjust=False,
)

# flatten if yfinance created a MultiIndex
if hasattr(df.columns, "droplevel"):
    try:
        df.columns = df.columns.droplevel(1)
    except Exception:
        pass

df.to_csv("AAPL.csv")
