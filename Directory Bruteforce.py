import requests
import sys

# Function to brute-force directories
def directory_bruteforce(target_url, wordlist_file):
    try:
        with open(wordlist_file, "r") as file:
            directories = file.read().splitlines()

        print(f"[+] Starting directory bruteforce on {target_url}\n")
        
        for directory in directories:
            url = f"{target_url}/{directory}"
            response = requests.get(url)
            
            if response.status_code == 200:
                print(f"[+] Found: {url} (Status: {response.status_code})")
            elif response.status_code == 403:
                print(f"[!] Forbidden: {url} (Status: {response.status_code})")
            
    except FileNotFoundError:
        print("[-] Wordlist file not found!")
    except requests.exceptions.RequestException as e:
        print(f"[-] Request error: {e}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <target_url> <wordlist_file>")
        sys.exit(1)
    
    target_url = sys.argv[1].rstrip('/')
    wordlist_file = sys.argv[2]
    
    directory_bruteforce(target_url, wordlist_file)
