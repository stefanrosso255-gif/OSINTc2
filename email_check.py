import requests

def check_email(email):
    print(f"\n[+] Verific email: {email}")

    # Validare simplă
    if "@" not in email or "." not in email.split("@")[-1]:
        print("[✗] Format email invalid")
        return

    domain = email.split("@")[-1]

    # MX lookup — domeniul poate primi email?
    try:
        import dns.resolver
        mx = dns.resolver.resolve(domain, "MX")
        print(f"[✓] Domeniul {domain} are servere MX (poate primi email)")
        for record in mx:
            print(f"    MX: {record.exchange}")
    except Exception:
        print(f"[✗] Domeniul {domain} pare invalid sau nu primește email")

    # Verificare breach — gratuit, fără API key
    try:
        r = requests.get(
            f"https://api.valicematt.xyz/api/hibp/{email}",
            timeout=10)
        if r.status_code == 200:
            data = r.json()
            breaches = data.get("breaches") or []
            if breaches:
                print(f"[!] Găsit în {len(breaches)} breach-uri:")
                for b in breaches:
                    nume = b.get("Name") or b.get("name") or str(b)
                    data_b = b.get("BreachDate") or b.get("breachDate") or ""
                    print(f"    [!] Breach: {nume} ({data_b})")
            else:
                print("[✓] Email-ul nu apare în breach-uri cunoscute")
        else:
            print(f"[~] Serviciul de breach a răspuns cu codul {r.status_code} — sărit")
    except requests.exceptions.Timeout:
        print("[~] Verificarea breach-ului a expirat — sărit")
    except Exception as e:
        print(f"[~] Verificarea breach-ului nu a putut fi făcută: {e}")
