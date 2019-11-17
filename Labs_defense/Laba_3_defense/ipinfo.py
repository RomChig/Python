import urllib.request
import json
import os

getIP = input("[+] Enter IP --> ")
url = "https://ipinfo.io/" + getIP + "/json"

try:
    getInfo = urllib.request.urlopen( url )

except:
    print( "\n[!] - IP not found! - [!]\n" )
infoList = json.load(getInfo)

def whoisIPinfo(ip):
    try:
        myComand = "whois " + getIP
        whoisInfo = os.popen( myComand ).read()
        return whoisInfo
    except:
        return "\n [!] -- Error -- [!] \n"

print( "-" * 60 )
print( "IP: ", infoList["ip"] )
print( "City: ", infoList["city"] )
print( "Region: ", infoList["region"] )
print( "Country: ", infoList["country"] )
try:
    print( "Hostname: ", infoList["hostname"] )
except:
    print( "Hostname: none" )
print( "-" * 60 )
print( whoisIPinfo ( getIP ) )
print( "-" * 60)