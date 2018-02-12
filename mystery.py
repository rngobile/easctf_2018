#!/usr/bin/env python3
import binascii
key = "ExUkkrfX"
s = "string"
def mystery(s):
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    return binascii.hexlify(bytes(r, "utf-8"))

def main():
    test = mystery(s)
    print(test)

if __name__ == '__main__':
    main()
