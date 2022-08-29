from termcolor import colored


levels = {
  "info": "blue",
  "warning": "yellow",
  "danger": "red"
}

def logger(msg: str, warning_level: str = 'info') -> None:
  "print message to terminal with specific color"
  print(colored(msg, levels[warning_level]))