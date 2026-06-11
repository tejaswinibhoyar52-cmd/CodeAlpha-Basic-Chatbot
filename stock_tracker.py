# Stock Portfolio Tracker (Indian Stocks)

stock_prices = {
    "RELIANCE": 1450,
    "TCS": 3800,
    "INFY": 1650,
    "HDFCBANK": 1900,
    "SBIN": 820
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ₹{price}")

while True:
    stock_name = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter Quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ₹{investment}")

    else:
        print("Stock not found! Please enter a valid stock name.")

print("\n===== Portfolio Summary =====")
print(f"Total Investment Value: ₹{total_investment}")

# Save report to a text file
with open("investment_report.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Tracker Report\n")
    file.write("==============================\n")
    file.write(f"Total Investment Value: ₹{total_investment}")

print("Report saved as investment_report.txt")