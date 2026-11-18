
import requests
from datetime import datetime

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

sites = {
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Reddit": "https://www.reddit.com/user/{}/",
    "TikTok": "https://www.tiktok.com/@{}",
    "Instagram": "https://www.instagram.com/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "X": "https://x.com/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Medium": "https://medium.com/@{}",
    "Telegram": "https://t.me/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Tumblr": "https://{}.tumblr.com",
    "Vimeo": "https://vimeo.com/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Keybase": "https://keybase.io/{}",
    "Mastodon": "https://mastodon.social/@{}",
    "WordPress": "https://{}.wordpress.com",
}

print(CYAN + "=" * 50 + RESET)
print(CYAN + "       OSINT USERNAME SCANNER" + RESET)
print(CYAN + "=" * 50 + RESET)

username = input("Username: ").strip()

results = []

for site, url in sites.items():
    profile = url.format(username)

    try:
        r = requests.get(
            profile,
            timeout=7,
            allow_redirects=True
        )

        if r.status_code == 200:
            status = "POSSIBLY FOUND"
            color = GREEN

        elif r.status_code == 404:
            status = "NOT FOUND"
            color = RED

        elif r.status_code in (403, 429):
            status = "UNKNOWN"
            color = YELLOW

        else:
            status = f"UNKNOWN ({r.status_code})"
            color = YELLOW

        print(f"{color}[{status}]{RESET} {site}: {profile}")

        results.append(f"[{status}] {site}: {profile}")

    except requests.exceptions.Timeout:
        print(f"{YELLOW}[TIMEOUT]{RESET} {site}")
        results.append(f"[TIMEOUT] {site}: {profile}")

    except requests.exceptions.RequestException:
        print(f"{RED}[ERROR]{RESET} {site}")
        results.append(f"[ERROR] {site}: {profile}")

filename = f"{username}_results.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write(f"Username OSINT Report: {username}\n")
    file.write(f"Date: {datetime.now()}\n")
    file.write("=" * 50 + "\n")

    for result in results:
        file.write(result + "\n")

print()
print(GREEN + f"Results saved to: {filename}" + RESET)
