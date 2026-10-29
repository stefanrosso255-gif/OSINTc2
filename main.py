import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

from email_check import check_email
from photo_check import check_photo
from ip_check import check_ip
from phone_check import check_phone
from whois_check import check_domain
from username_check import check_username
from breach_check import check_breaches_free

def menu():
    print("""
╔════════════════════════════╗
║        OSINT TOOL          ║
╠════════════════════════════╣
║ 1. Email                   ║
║ 2. Poza (EXIF)             ║
║ 3. IP                      ║
║ 4. Număr telefon           ║
║ 5. Domeniu (WHOIS)         ║
║ 6. Username                ║
║ 7. Breach check (email)    ║
║ 0. Ieșire                  ║
╚════════════════════════════╝""")

while True:
    menu()
    alegere = input("Alegere: ").strip()
    if alegere == "1": check_email(input("Email: "))
    elif alegere == "2": check_photo(input("Cale imagine: "))
    elif alegere == "3": check_ip(input("IP: "))
    elif alegere == "4": check_phone(input("Telefon (ex +407...): "))
    elif alegere == "5": check_domain(input("Domeniu: "))
    elif alegere == "6": check_username(input("Username: "))
    elif alegere == "7": check_breaches_free(input("Email: "))
    elif alegere == "0": break
