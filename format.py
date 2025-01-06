
import re

name = input("What's your name? ").strip()



if matches := re.search(r"^(.+), ?(.+)$",name):
    name = matches.groups(2) + " " + matches.group(1)
print(f"hello,{name}")
