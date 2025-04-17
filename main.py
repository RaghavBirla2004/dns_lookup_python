import socket
import webbrowser
domain_name = input("Enter  Address (www.google.com) - ")
domain_name = domain_name.replace("https://", "").replace("http://", "").replace("/", "")

ip_address = socket.gethostbyname(domain_name)

print("Ip Address  = " , ip_address)
decison= input("Open in Web Browswer (y or n) ")
if(decison == "y"):
    print("Opening....")
    webbrowser.open(ip_address)
    
