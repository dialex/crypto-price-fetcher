from colorama import Fore, Style


def debug(msg):
    print(msg)


def info(msg):
    print(f"{Fore.CYAN}{msg}")


def warn(msg):
    print(f"⚠️ {Fore.YELLOW}{msg}")


def err(msg):
    print(f"🔴 {Fore.RED}{msg}")
