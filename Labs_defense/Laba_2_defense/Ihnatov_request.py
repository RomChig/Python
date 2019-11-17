import http.client, sys
import json, pprint

foo = {'text': 'Test'}

host = input("Site: ")
port = input("Port: ")
def my_funct(host, port):
    if host in ['www.samsung.com', 'www.facebook.com', 'www.aimprosoft.com'] and port in ['80', '443']:
        print("\nYour host is " + host)
        print("Your port is " + port + "\n")
    else:
        print("Sorry, but you entered not right data")
        sys.exit()
my_funct(host,port)

json_data = json.dumps(foo)

connection = http.client.HTTPConnection(host, port)
connection.request("GET", "/")
response = connection.getresponse()

headers = response.getheaders()
headers2 = {'Content-type': 'application/json'}

connection2 = http.client.HTTPConnection(host, port)
connection2.request('POST', '/post', json_data, headers2)
response2 = connection2.getresponse()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint("HTTP Headers: {}".format(headers))

print("Status: {} and reason: {}".format(response.status, response.reason))
if response.status == 200:
    print("\n" + response2.read().decode())
print("Section 1: GET Request:")
print("\nSection 2: GET Headers:")
print("\nSection 3: POST Request:")
print("Successful request to '" + host + "'")
print("Status: {} and reason: {}".format(response.status, response.reason))
