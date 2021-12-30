import hashlib
import sys
import requests



def main(password):
    password = password.encode('utf-8')
    hash = hashlib.sha1(password).hexdigest().upper()
    pre, suf = hash[:5], hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{pre}"
    result = requests.get(url=url)

    hashes = (line.split(':') for line in result.text.splitlines())
    found = False
    while not found:
        try:
            hsh, occ = next(hashes)
        except StopIteration as e:
            break
        else:
            found = suf in hsh
            if found:
                print(f"The password {password} was found {occ} time{'s' if occ != 1 else ''}")
    if not found:
        print("Yay! Safe seems safe to use")

if __name__ == "__main__":
    main(sys.argv[1].strip())