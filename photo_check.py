import exifread

def check_photo(path):
    print(f"\n[+] Analizez: {path}")
    with open(path, "rb") as f:
        tags = exifread.process_file(f, details=False)

    if not tags:
        print("[✗] Nu există metadate EXIF (poate fi curățată imaginea)")

    gps_info = {}
    for tag, value in tags.items():
        if tag == "GPSInfo" or "GPS" in tag:
            gps_info[tag] = str(value)
        elif tag in ("Image Make", "Image Model", "EXIF DateTimeOriginal"):
            print(f"    {tag}: {value}")

    print(f"    GPS raw: {gps_info}")
    print("[i] Copiază coordonatele GPS în Google Maps pentru locație")
