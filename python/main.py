import helpers.config as config

print("Hello World")

# Read config
config_path = "config.txt"
print("Opening file at " + config_path)
lines = config.read_file(config_path)
print("Read " + str(len(lines)) + " lines")
