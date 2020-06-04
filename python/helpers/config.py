def read_target_coins(config_path):
    """Reads a config file and returns a list of coins"""
    config_file = open(config_path, 'r')
    lines = config_file.readlines()
    config_file.close()
    return lines
