from cowsay import stegosaurus
from colorama import Fore, Back, Style

def main() -> None:
    print(Fore.GREEN)
    stegosaurus("hey")
    print(Style.RESET_ALL)
