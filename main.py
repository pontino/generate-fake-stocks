import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_fake_stock_data(start_date: str, end_date: str, initial_price: float):
    # Set the seed for reproducibility
    np.random.seed(20)

    days = (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days

    # Generate random daily returns
    # Mean daily return 0.1%, standard deviation 2%
    daily_returns = np.random.normal(loc=0.001, scale=0.02, size=days)

    # Calculate the price series
    price_series = [initial_price]
    for daily_return in daily_returns:
        price_series.append(price_series[-1] * (1 + daily_return))

    # Create a pandas DataFrame
    dates = pd.date_range(start=start_date, periods=days + 1, freq='D')
    stock_data = pd.DataFrame(data={"Date": dates, "Price": price_series})

    return stock_data


if __name__ == "__main__":
    today = pd.Timestamp.today().strftime("%Y-%m-%d")
    fake_stock_data = generate_fake_stock_data("2021-01-01", today, 100)

    plt.plot(fake_stock_data["Date"], fake_stock_data["Price"])
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Fake Stock Price Data")
    plt.show()

