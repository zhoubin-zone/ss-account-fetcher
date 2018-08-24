import os,sys,requests,base64
from bs4 import BeautifulSoup
from qrtools import QR
import string
import random

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def random_string(length):
	return ''.join(random.choice(string.ascii_letters) for m in range(length))
	
#ss out put sample	['aes-256-ctr', 'ssrcat@185.225.139.8', '443']
#ssr out put sample	['185.225.139.75', '443', 'origin', 'aes-256-ctr', 'plain', 'c3NyY2F0']

def format_print(str, type):
	str = str.strip()
	fullinfo = str.split(":")
	print fullinfo

url = "https://ssfree.top"
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,'lxml')
mydivs = soup.findAll("div", {"class": "ss"})
for ss in mydivs:
	format_print(ss['value'],"ss")


url = "https://ss.freess.org"
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,'lxml')
QR_imgs = soup.findAll("a", {"class": "image fit"})
for qrimg in QR_imgs:
	n,img = qrimg['href'].split(",")
	raw_img = base64.b64decode(img)
	tmp_f = random_string(5)
	fp = open(tmp_f, "wb")
	fp.write(raw_img)
	fp.close()
	myCode = QR(filename=tmp_f)
	if myCode.decode():
		if(myCode.data_type == "text"):
			protocol,ss = myCode.data_to_string().split("://")
			format_print(base64.b64decode(ss),protocol)
	os.remove(tmp_f)

url = "https://shadowsocksr.cat"
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,'lxml')
QR_img_urls = soup.findAll("a", {"class": "overlay lightbox"})
for qrimgurl in QR_img_urls:
	imgurl = url+"/"+qrimgurl['href']
	r = requests.get(imgurl,headers=headers)
	tmp_f = random_string(5)
	imageFile = open(tmp_f, 'wb')
	for chunk in r.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()
	myCode = QR(filename=tmp_f)
	if myCode.decode():
		if(myCode.data_type == "text"):
			#print myCode.data_to_string()
			protocol,ss = myCode.data_to_string().split("://")
			#print base64.b64decode(ss+"==")
			format_print(base64.b64decode(ss+"=="),protocol)
	os.remove(tmp_f)
