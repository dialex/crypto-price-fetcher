import helpers.config as config

print("Hello World")

# Read config
config_path = "config.txt"
print("Opening file at " + config_path)
coin_tickers = config.read_file(config_path)
print("Read " + str(len(coin_tickers)) + " lines")

# For each coin ticker
# Call API to fetch price
# Store that price on array
# Write all prices to prices.txt
# Print with colour: info, warning, err
