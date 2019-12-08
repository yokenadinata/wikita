from django.shortcuts import render
from django.http import HttpResponse
import wikipedia
# Create your views here.
import re
import os
import urllib
import requests
import json
import urllib.request
from bs4 import BeautifulSoup
import cgi
#
# Create your views here.

buset = None
def home(request):
	if request.method == 'POST':
		global buset
		buset = request.POST['input']
		#print(buset)
		return index(request)
	else:
		return render(request,'home.html')
	#return render(request,'home.html')
	

def index(request):
	#bus = home(request)
	print(buset)
	test=buset
	wikipedia.set_lang("ID")
	#test='fahri hamzah'
	#abc='Maudy_Ayunda'
	abc1=test.lower().title()
	abc2=abc1.replace(" ","_")
	#title = os.popen("curl -s https://id.wikipedia.org/wiki/"+test+" | grep 'lahir' | grep 'title=' | grep '<a href='").read()
	# wikipedia.set_lang("IN")
	# wikipedia.page(test)
	a = wikipedia.summary(test)
	page = wikipedia.page(test)
	pattern = re.compile(
	"\d{1,2}\s+(Januari|Februari|Maret|April|Mei|Juni|"
	"Juli|Agustus|September|Oktober|November|"
	"Desember)")
	#print(title)
	pattern2 = re.compile(
		"\d{4}")

	#cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
	#cleantext = re.sub(cleanr, '', ket)
	tangbul = pattern.search(a).group()
	tahun = pattern2.search(a).group()
	# print(tangbul)
	# print(tahun)

	image = page.images[0]
	#r = urllib.request.urlopen("https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles=%s&pithumbsize=500" % abc)
	#aa=r.read()
	#html="https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles=%s&pithumbsize=500"
	#urlawal= ("https://id.wikipedia.org/w/api.php?action=query&format=json&titles=%s" % abc)
	urll=("https://id.wikipedia.org/w/api.php?action=parse&format=json&prop=sections&page=%s" % abc2)
	response = urllib.request.urlopen(urll)
	data = json.loads(response.read().decode('utf-8'))
	hasilolah=data['parse']['pageid']
	print(hasilolah)
	hehe=str(hasilolah)
	print(hehe)
	url = ("https://id.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles=%s" % abc2) 
	try:
		response = urllib.request.urlopen(url)
		data = json.loads(response.read().decode('utf-8'))
		context={
		 'image': data['query']['pages'][""+hehe+""]['original']['source'],
		 'tangbul': tangbul,
		 'tahun': tahun,
		 'nama': abc1,
		 'sum': a,
		}
		#print(data['query']['pages']['1718759']['original']['source'])
		return render(request, 'index.html', context)
	except:
		context={
		 'image': 'image gk ada',
		 'tangbul': tangbul,
		 'tahun': tahun,
		 'nama': abc1,
		 'sum': a,
		}
		return render(request, 'index.html', context)
	
	# content = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles=Jaguar&pithumbsize=500")
	# abc = json.loads(content)
	# print(abc)
	# with urllib.request.urlopen("https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles=Jaguar&pithumbsize=500") as url:
 #    data = json.loads(url.read().decode())
    # print(response)
	# print(cleantext)
	#return render(request,'index.html',context)
	#return render(request, 'index.html',context)

