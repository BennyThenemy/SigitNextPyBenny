import base64

encoded_string = "CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgI" \
                 "CAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICA" \
                 "gICA7LS0tLS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAg" \
                 "ICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1" \
                 "tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgIC" \
                 "AgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCA" \
                 "gICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgI" \
                 "CAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8" \
                 "fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo="


def main():
    # Decode from Base64 and convert to bytes
    decoded_bytes = base64.b64decode(encoded_string)

    # Convert bytes to UTF-8 string
    decoded_string = decoded_bytes.decode('utf-8')

    print(decoded_string)


if __name__ == '__main__':
    main()

