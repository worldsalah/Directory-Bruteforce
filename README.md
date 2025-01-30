# Directory Bruteforcing Tool

## Description
This Python script performs directory bruteforcing on a given target URL using a wordlist. It helps identify hidden directories that may not be publicly accessible.

## Features
- Scans a target website for hidden directories.
- Uses a wordlist to check for common directory names.
- Identifies accessible (200 OK) and forbidden (403 Forbidden) directories.
- Simple and easy to use.

## Requirements
- Python 3.x
- `requests` library (install with `pip install requests`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/directory-bruteforce.git
   cd directory-bruteforce
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script with the following command:
```bash
python script.py <target_url> <wordlist_file>
```

### Example
```bash
python script.py https://example.com wordlist.txt
```

## Wordlist Format
Create a `wordlist.txt` file with directory names to check, for example:
```
admin
login
images
uploads
dashboard
```

## Output Example
```
[+] Starting directory bruteforce on https://example.com

[+] Found: https://example.com/admin (Status: 200)
[!] Forbidden: https://example.com/uploads (Status: 403)
```

## License
This project is licensed under the MIT License.

## Disclaimer
This tool is for educational purposes only. Use it responsibly and only on websites you have permission to test.

