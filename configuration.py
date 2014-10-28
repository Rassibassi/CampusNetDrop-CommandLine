#!/usr/bin/python
import os
import urllib2
import xml.etree.ElementTree as ET
#
from CampusNetDrop import *
dirname, filename = os.path.split(os.path.abspath(__file__))

### Login
if not os.path.isfile("lmtdAccss.txt"):
	login()
else:
	print "Configure login? (yes/no)"
	configure = raw_input()
	if (configure == "yes" or configure =="y"):
		login()
	

### Config
print "Configure courses? (yes/no)"
configure = raw_input()
if configure == "yes" or configure =="y":	
	# Create request and load XML into 'root'
	url = 'https://www.campusnet.dtu.dk/data/CurrentUser/Elements'
	req = createRequest(url)
	response = urllib2.urlopen(req)
	root = ET.fromstring(response.read())
	# Run through 'root' node and save elementID, download path and versioning in config
	f = open(dirname+'/config.txt','w')
	for node in root:
		for child in node:
			print "Add \"%s --- %s\" to Downloads? (y/n)" % (node.get('Name'),child.get('Name'))
			answer = raw_input()

			if answer=="yes" or answer=="y":
				print "Where to download the \"%s\" files? (Path)" % (child.get('Name'))
				directory = raw_input()
				directory = directory.replace("\\","/")
				f.write(child.get('Name')+";"+child.get('Id')+";"+directory+"\n")
	f.close()