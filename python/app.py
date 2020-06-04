import helpers.io as io
import helpers.api as api

# Read config
config_path = "config.txt"
print("Opening file at " + config_path)
coin_tickers = io.read_file(config_path)
print("Read " + str(len(coin_tickers)) + " lines")

# Fetch prices
prices = []
for coin in coin_tickers:
    coin = coin.rstrip()
    print(f"Fetching data for {coin}")
    coin_price = api.get_price(coin)
    print(f" {coin_price} EUR")
    prices.append(coin_price)

# Write results
output_path = "prices.txt"
io.write_list_file(output_path, prices)

# TODO: refactor: print with colour (info, warning, err)
