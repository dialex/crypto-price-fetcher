import helpers.io as io
import helpers.api as api
import helpers.log as log
import colorama
from dotenv import load_dotenv

# Enable colored output
colorama.init(autoreset=True)

# Read secrets
load_dotenv()

# Read config
config_path = "config.txt"
log.info(f"Opening file at {config_path}…")
coin_tickers = io.read_file(config_path)
log.debug(f"Read {str(len(coin_tickers))} lines")

# Fetch prices
prices = []
for coin in coin_tickers:
    coin = coin.rstrip()
    log.info(f"Fetching data for {coin}…")
    coin_price = api.get_price(coin)
    log.info(f"  {coin_price} EUR")
    prices.append(coin_price)

# Write results
output_path = "prices.txt"
io.write_list_file(output_path, prices)
log.info(f"Prices exported to {output_path}")

# Disabled colored output
colorama.deinit()
