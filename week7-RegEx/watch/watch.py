import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if re.search(r"<iframe .*></iframe>", s):

        if matches := re.search(r"(https?://(www\.)?youtube\.com/embed/[a-zA-Z0-9]+)", s):

            url = re.sub(r"https?://(www\.)?youtube\.com/embed/", "https://youtu.be/", matches.group(1))

            return url


if __name__ == "__main__":
    main()
