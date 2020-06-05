import helpers.log as log


def read_file(filepath):
    """Reads a file and returns a list with each line"""
    try:
        config_file = open(filepath, 'r')
    except Exception as e:
        log.warn(e)
        lines = []
    else:
        lines = config_file.readlines()
        config_file.close()
    return lines


def write_list_file(filepath, list):
    """Write list to file, one element per line"""
    with open(filepath, 'w+') as output_file:
        for element in list:
            output_file.write(str(element) + "\n")
