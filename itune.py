# import requests
# import sys
# import json


# if len(sys.argv)!= 2:
#     sys.exit()

# respond = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# # print(json.dumps(respond.json(),indent=1))

# o = respond.json()
# for result in o["results"]:
#     print(result["trackName"])


def main():
    hello("Aabhushan")
    hello("Aayush")
    goodbye("Aabhushan")

def hello(name):
    print(f"Hello,{name}")

def hello(name):
    print(f"Hello,{name}")

def goodbye(name):
    print(f"Googbye, {name}")

if __name__ == "__main__":
    main()


