import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + "<url>")
    sys.exit(1)

print("_____________________________________________________________________________________________________")


print(" |\  \|\   ___  \|\  _____\\   __  \        |\   __  \|\  ___ \ |\   ____\|\   __  \|\   ___  \     ")
print(" \ \  \ \  \\ \  \ \  \__/\ \  \|\  \       \ \  \|\  \ \   __/|\ \  \___|\ \  \|\  \ \  \\ \  \    ")
print("  \ \  \ \  \\ \  \ \   __\\ \  \\\  \       \ \   _  _\ \  \_|/_\ \  \    \ \  \\\  \ \  \\ \  \   ")
print("   \ \  \ \  \\ \  \ \  \_| \ \  \\\  \       \ \  \\  \\ \  \_|\ \ \  \____\ \  \\\  \ \  \\ \  \  ")
print("    \ \__\ \__\\ \__\ \__\   \ \_______\       \ \__\\ _\\ \_______\ \_______\ \_______\ \__\\ \__\ ")
print("     \|__|\|__| \|__|\|__|    \|_______|        \|__|\|__|\|_______|\|_______|\|_______|\|__| \|__| ")

print("                Information Recon scanner based on Python - @sakibulalikhan     ")

print("______________________________________________________________________________________________________")

req = requests.get("https://"+sys.argv[1])
print("🅣🅗🅔 🅗🅔🅐🅓🅔🅡 🅕🅘🅛🅔 = " + "\n" + "\n"+str(req.headers))

print("______________________________________________________________________________________________________")

gethostby_ = socket.gethostbyname(sys.argv[1])
print("\n The IP address of " + sys.argv[1] + " = " + gethostby_ + "\n")

#ipinfo.io api

req_two = requests.get("https://ipinfo.io/" + gethostby_ + " /json")
resp_ = json.loads(req_two.text)

print("______________________________________________________________________________________________________")

print("Location: " + resp_["loc"])
print("Region: " + resp_["region"])
print("City: " + resp_["city"]) 
print("Country: " + resp_["country"])
print("IP Address: " + resp_["ip"])
print("Organization: " + resp_["org"])
print("Postal Code: " + resp_["postal"])
print("Timezone: " + resp_["timezone"])


print("________________________________________________THE_END________________________________________________")