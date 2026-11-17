import dns.resolver
from concurrent.futures import ThreadPoolExecutor

domain = input("Enter Domain Name:")

wordlists = [
	"www",
	"mail",
	"api",
	"dev",
	"admin",
	"test",
	"blog",
	"shop",
	"ftp",
	"vpn",
]

def check_subdomain(name):
	subdomain = f"{name}.{domain}"
	try:
		answers = dns.resolver.resolve(subdomain, "A")
		for answer in answers:
			print(f"FOUND {subdomain} > {answer} ")
	except Exception:
		pass
print("\nStarting Subdomain Finder...\n")

with ThreadPoolExecutor(max_workers=5) as executor:
	executor.map(check_subdomain, wordlists)
print("\nScan completed!")
