#!/usr/bin/python2.7

__verison__ = '1.1.1'

import urllib2
import string
import random
import datetime
import base64
import githubpy
import sys
import os

from githubpy import github
from bs4 import BeautifulSoup


token = '****************************************'  #Github auth token for authorisation

def extract():

	"""
	Function to first go to the yahoo financial news page, then acts as a crawler
	visit the latest news page, then etract the full news in a variable upload_string, which
	is then encoded in UTF-64, which is then pushed as a file to my github repo.

	"""

	url      = urllib2.urlopen("https://in.finance.yahoo.com/news/")
	soup     = BeautifulSoup(url)
	var      = soup.find("a", {"class":"title"})
	con      = var.get("href")
	header = ''

	for i in range(6, 40):
			header = header + con[i]

	heading = header + "..."

	link     = "https://in.finance.yahoo.com" + con
	url1     = urllib2.urlopen(link)
	soup1    = BeautifulSoup(url1)

	var2 = soup1.find("div", {"itemprop":"articleBody"})
	var3 = var2.text.encode('ascii', 'ignore')

	upload_string  = str(var3)
	commit_message = str(datetime.datetime.now())
	filename       = heading.title()
	
	gh           = githubpy.github.GitHub(access_token=token)
	encoded_file = base64.b64encode(upload_string)
	gh.repos('Rahul91')('pytest')('contents')(filename).put(path=filename,message=commit_message, content=encoded_file)
		
	print "Successfully pushed a new article titled : %s on %s \n" %(filename, commit_message)
	raw_input("Press Enter to exit :)")

if __name__ == "__main__":
	extract()

