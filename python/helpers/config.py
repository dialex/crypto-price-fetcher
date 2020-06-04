def read_file(filepath):
    """Reads a config file and returns a list of coins"""
    print("Opening config file at " + filepath)
    config_file = open(filepath, 'r')
    lines = config_file.readlines()  # TODO: handle not found
    print("Read " + str(len(lines)) + " lines of config")
    config_file.close()
    return lines
