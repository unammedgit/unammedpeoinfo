import os
import webbrowser
from colorama import init, Fore, Style

init(autoreset=True)  # Inizializza colorama

def print_ascii_art():
    ascii_art = f"""
{Fore.YELLOW}
 ____ ___                                               .___ ________                    __            
|    |   \  ____  _____     _____    _____    ____    __| _/ \______ \    ____  _______ |  | __  ______
|    |   / /    \ \__  \   /     \  /     \ _/ __ \  / __ |   |    |  \  /  _ \ \_  __ \|  |/ / /  ___/
|    |  / |   |  \ / __ \_|  Y Y  \|  Y Y  \\  ___/ / /_/ |   |    `   \(  <_> ) |  | \/|    <  \___ \ 
|______/  |___|  /(____  /|__|_|  /|__|_|  / \___  >\____ |  /_______  / \____/  |__|   |__|_ \/____  >
               \/      \/       \/       \/      \/      \/          \/                      \/     \/ 
{Style.RESET_ALL}
    """
    print(ascii_art)

def generate_dork_1():
    print("\nGenerazione Dork 1: Informazioni su soggetto online")
    nome = input("Nome (premere invio se non presente): ")
    cognome = input("Cognome (premere invio se non presente): ")
    elemento_1 = input("Elemento 1 (premere invio se non presente): ")
    elemento_2 = input("Elemento 2 (premere invio se non presente): ")

    dork_parts = []
    if nome and cognome:
        dork_parts.append(f'"{nome} {cognome}" OR "{cognome} {nome}"')
    elif nome:
        dork_parts.append(f'"{nome}"')
    elif cognome:
        dork_parts.append(f'"{cognome}"')

    if elemento_1:
        dork_parts.append(elemento_1)

    if elemento_2:
        dork_parts.append(elemento_2)

    dork = " AND ".join(dork_parts)
    print(f"{Fore.GREEN}Google Dorks generata:{Style.RESET_ALL}")
    print(dork)

    open_in_browser(dork)

def generate_dork_2():
    print("\nGenerazione Dork 2: Documenti su soggetto online")
    nome = input("Nome (premere invio se non presente): ")
    cognome = input("Cognome (premere invio se non presente): ")
    anno_di_nascita = input("Anno di nascita o altro elemento (premere invio se non presente): ")
    elemento_2 = input("Elemento 2 (premere invio se non presente): ")

    dork_parts = []
    if nome and cognome:
        dork_parts.append(f'intext:"{nome} {cognome}" OR intext:"{cognome} {nome}"')
    elif nome:
        dork_parts.append(f'intext:"{nome}"')
    elif cognome:
        dork_parts.append(f'intext:"{cognome}"')

    file_types = [
        'doc', 'docx', 'odt', 'pdf', 'rtf', 'sxw', 'psw', 'ppt', 'pptx', 'pps', 'csv', 'txt', 'xls'
    ]
    file_type_dork = ' OR '.join([f'filetype:{ext}' for ext in file_types])

    if anno_di_nascita:
        dork_parts.append(anno_di_nascita)

    if elemento_2:
        dork_parts.append(elemento_2)

    dork = f"({file_type_dork}) {(' AND '.join(dork_parts))}"
    print(f"{Fore.GREEN}Google Dorks generata:{Style.RESET_ALL}")
    print(dork)

    open_in_browser(dork)

def open_in_browser(dork):
    try:
        webbrowser.open(f'https://www.google.com/search?q={dork}')
    except:
        print(f"{Fore.RED}Errore nell'aprire il browser.{Style.RESET_ALL}")

def main():
    print_ascii_art()
    print("Scegli che tipo di dork generare:")
    print(f"{Fore.BLUE}1. {Fore.RESET}Informazioni su soggetto online")
    print(f"{Fore.BLUE}2. {Fore.RESET}Documenti su soggetto online")

    choice = input("Inserisci il numero corrispondente alla tua scelta: ")

    if choice == '1':
        generate_dork_1()
    elif choice == '2':
        generate_dork_2()
    else:
        print(f"{Fore.RED}Scelta non valida. Si prega di inserire un numero valido.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()