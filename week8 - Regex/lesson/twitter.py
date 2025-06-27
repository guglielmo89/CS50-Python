import re

url = input("URL: ").strip()

if username := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_])+", url, re.IGNORECASE):
    print(f"User: {username.group(1)}")

# http://twitter.com/guglielmoveri
