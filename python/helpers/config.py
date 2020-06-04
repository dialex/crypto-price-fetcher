def read_file(filepath):
    """Reads a file and returns a list with each line"""
    try:
        config_file = open(filepath, 'r')
    except Exception as e:
        print(e)
        lines = []
    else:
        lines = config_file.readlines()
        config_file.close()
    return lines
