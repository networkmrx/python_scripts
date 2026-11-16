
import nmap

def port_scan(target):
    nm = nmap.PortScanner()

    print(f"\n[+] Scanning target: {target}")
    print("[+] Scanning all TCP ports...\n")

    try:
        nm.scan(target, arguments='-p-')

        for host in nm.all_hosts():
            print(f"\nHost: {host}")
            print(f"Status: {nm[host].state()}")

            for proto in nm[host].all_protocols():
                ports = sorted(nm[host][proto].keys())

                for port in ports:
                    state = nm[host][proto][port]['state']
                    print(f"Port {port}/{proto} - State: {state}")

        print("\n[+] Scan completed!")

    except nmap.PortScannerError as e:
        print(f"[!] Nmap error: {e}")

    except Exception as e:
        print(f"[!] Error: {e}")


if __name__ == "__main__":
    print("=" * 40)
    print("       PYTHON PORT SCANNER")
    print("=" * 40)

    target = input("[?] Enter Domain or IP: ").strip()

    if target:
        port_scan(target)
    else:
        print("[!] Target cannot be empty!")
