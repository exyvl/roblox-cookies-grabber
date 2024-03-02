import webbrowser
from colorama import Fore, Style

discord_link = "https://discord.gg/bnF37q6Udf"

# Wyświetlanie dużej grafiki ASCII
ascii_art = """
    _  ___ ___ _   _   ____ ___ ____   ____ ___  ____  ____  
    | |/ _ \\_ _| \\ | | |  _ \\_ _/ ___| / ___/ _ \\|  _ \\|  _ \\ 
 _  | | | | | ||  \\| | | | | | |\\___ \\| |  | | | | |_) | | | |
| |_| | |_| | || |\\  | | |_| | | ___) | |__| |_| |  _ <| |_| |
 \\___/ \\___/___|_| \\_| |____/___|____/ \\____\\___/|_| \\_\\____/
"""

# Wyświetlanie napisu w terminalu
print(Fore.CYAN + ascii_art)
print(Fore.BLUE + "Draw for €25 LTC join on Discord: " + discord_link)
print(Style.RESET_ALL)  # Resetowanie kolorów do domyślnych

# Otwieranie linku w przeglądarce
webbrowser.open(discord_link)

# Oczekiwanie na naciśnięcie klawisza Enter przed zakończeniem programu
input("Press Enter to exit...")
