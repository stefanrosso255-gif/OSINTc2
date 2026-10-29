import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def check_phone(number):
    print(f"\n[+] Verific număr: {number}")
    try:
        nr = phonenumbers.parse(number, None)
        if not phonenumbers.is_valid_number(nr):
            print("[✗] Număr invalid")
            return
        print(f"    Țară:       {geocoder.description_for_number(nr, 'ro')}")
        print(f"    Operator:   {carrier.name_for_number(nr, 'ro')}")
        print(f"    Fus orar:   {timezone.time_zones_for_number(nr)}")
        # Pe Google often găsești numărul → link direct
        print(f"    Cautare:    https://www.google.com/search?q=%22{number}%22")
    except Exception as e:
        print(f"[✗] Eroare: {e}")
