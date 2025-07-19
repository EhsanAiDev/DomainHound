import re
import os
import argparse

# --- Argument Parsing ---
parser = argparse.ArgumentParser(description="DomainHound is a tool for Filter subdomain list based on a provided wordlist.")
parser.add_argument("-w", type=str, required=True, help="Path to the wordlist used for filtering")
parser.add_argument("-sd", type=str, required=True, help="Path to the subdomains list to be filtered")
parser.add_argument("-o", type=str, help="The path you want to save the output")
args = parser.parse_args()

# --- Colors ---
red     = "\033[31m"
blue    = "\033[34m"
green   = "\033[32m"
name_bg = "\033[48;5;235m"
gray_bg = "\033[48;5;237m"
reset   = "\033[0m"

# --- Validation ---
if not os.path.exists(args.w):
    print(f"{red}[ERROR]{reset} Wordlist not found.")
    exit()

if not os.path.exists(args.sd):
    print(f"{red}[ERROR]{reset} Subdomains list not found.")
    exit()

# --- Paths ---
wordlist_path = args.w
subdomains_list_path = args.sd
saving = True if args.o else False

def banner():
    me = f"created by: " + name_bg + red + "NakuTenshi" + reset + reset
    print(fr"""
{blue}+--------------------------------------------------------------------------------------------+{reset}
{blue}|{reset}  _____                        _       _    _                   _                           {blue}|{reset}
{blue}|{reset} |  __ \                      (_)     | |  | |                 | |                          {blue}|{reset}
{blue}|{reset} | |  | | ___  _ __ ___   __ _ _ _ __ | |__| | ___  _   _ _ __ | |_                         {blue}|{reset}
{blue}|{reset} | |  | |/ _ \| '_ ` _ \ / _` | | '_ \|  __  |/ _ \| | | | '_ \| __|                        {blue}|{reset}
{blue}|{reset} | |__| | (_) | | | | | | (_| | | | | | |  | | (_) | |_| | | | | |_ {me}  {blue}|{reset}
{blue}|{reset} |_____/ \___/|_| |_| |_|\__,_|_|_| |_|_|  |_|\___/ \__,_|_| |_|\__|fuck this people        {blue}|{reset}
{blue}|{reset}                                                                                            {blue}|{reset}
{blue}+--------------------------------------------------------------------------------------------+{reset}
""")

def main():
    banner()
    if saving:
        print(f"{blue}[INFO]{reset} Saving the outputs into {args.o}")
        os.system(f"touch ./{args.o}")

    total = 0
    with open(wordlist_path, "r") as wordlist, open(subdomains_list_path, "r") as subdomains_wordlist:
        words      = wordlist.read().split("\n")
        subdomains = subdomains_wordlist.read().split("\n")

        for subdomain in subdomains:
            for word in words:
                if re.search(rf"(?:^|\.){word}(?:\.|$)", subdomain):
                    if saving:
                        with open(args.o, "a") as output_file:
                            output_file.write(f"{subdomain}\n")
                    else:
                        print(f"{green}[+]{reset} {subdomain}")
                    total += 1

    print(f"{blue}[INFO]{reset} The script is done.")
    print(f"{blue}[INFO]{reset} {red}{total}{reset} subdomains found.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bye :)")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
