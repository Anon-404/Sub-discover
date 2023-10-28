import requests
import threading
import time
import os
os.system("clear")
GREEN = "\033[0;32m"
RED = "\033[0;31m"
BLUE = "\033[1;34m"
a = """
   .dMMMb  dMP dMP dMMMMb                                          
  dMP" VP dMP dMP dMP"dMP                                          
  VMMMb  dMP dMP dMMMMK"                                           
dP .dMP dMP.aMP dMP.aMF                                            
VMMMP"  VMMMP" dMMMMP"                                             
"""
b = """
    dMMMMb  dMP .dMMMb  .aMMMb  .aMMMb  dMP dMP dMMMMMP dMMMMb     
   dMP VMP amr dMP" VP dMP"VMP dMP"dMP dMP dMP dMP     dMP.dMP     
  dMP dMP dMP  VMMMb  dMP     dMP dMP dMP dMP dMMMP   dMMMMK"      
 dMP.aMP dMP dP .dMP dMP.aMP dMP.aMP  YMvAP" dMP     dMP"AMF       
dMMMMP" dMP  VMMMP"  VMMMP"  VMMMP"    VP"  dMMMMMP dMP dMP 
"""
def banner():
	print(GREEN,"_"*67)
	print(RED,a)
	print(GREEN,b)
	print("powerd by team Anon404 \ncreated by MRZ724")
	print(GREEN,"_"*67)	
banner()
print()
domain = input("[+] Enter terget domain : ").replace("https://","").replace("http://","").replace("www.","").replace("https://www.","").replace("http://www.","")
print(BLUE,"\b[!] Chacking domain")
try:
	y = requests.get(f"https://{domain}")
	if y.status_code == 200:
		pass
except requests.ConnectionError:
	print(RED,"\b[-] Invalid domain or no internet connection")
	exit()
print(GREEN,"""
[1] Scan with buildin wordlist
[2] Scan with your wordlist
	""")
option = input("[+] Enter your option : ")
if option =="1":
	try:
		sub = open("sub.txt",errors="replace").read()
		sub = sub.splitlines()
	except FileNotFoundError:
		print("[-] File not found")
elif option =="2":
	try:
		file = input("[+] Enter your wordlist name : ")
		sub = open("sub.txt",errors="replace").read()
		sub = sub.splitlines()
	except FileNotFoundError:
		print("[-] File not found")
else:
	print(RED,"\b[-] Wrong option")
	exit()
def myfnc():
	for i in sub:
		yield i
su = myfnc()
os.system("clear")
banner()
print()
start = time.time()
def func():
	discovered_subdomains = []
	for subdomain in su:
		url = f"https://{subdomain}.{domain}"
		try:
			requests.get(url)
		except requests.ConnectionError:
#			print(RED,url)
			pass
		except requests.exceptions.TooManyRedirects:
			pass
		except requests.exceptions.RequestException:
			pass
		else:
			print(GREEN,url)
			discovered_subdomains.append(url)
num_threads = 21
threads = []
for i in range(num_threads):
	thread = threading.Thread(target=func)
	threads.append(thread)
	thread.start()
for thread in threads:
    thread.join()    
end = time.time()
print(f"Time taken: {(end-start)*10**3:.03f}ms")
#print(end-start)
