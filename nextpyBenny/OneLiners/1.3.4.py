if __name__ == '__main__':
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    print("".join(chr(ord(c)+2) if c.isalnum() else c for c in password))
