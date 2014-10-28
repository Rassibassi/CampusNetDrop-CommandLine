#!/usr/bin/python

import sys, datetime, os
import urllib2
import xml.etree.ElementTree as ET
#
from CampusNetDrop import *
dirname, filename = os.path.split(os.path.abspath(__file__))

### Downloader
# Load Config
configFile = open(dirname+'/config.txt')
lines = configFile.readlines()
configFile.close()

# Run through courses
for line in lines:
	line = line.strip()
	line = line.split(";")
	elementID = line[1]
	directory = line[2]
	print " ################### "
	print "  "+line[0]
	print " ################### "

	# get files of course from xml
	url='https://www.campusnet.dtu.dk/data/CurrentUser/Elements/%s/Files' % (str(elementID))
	req = createRequest(url)
	response = urllib2.urlopen(req)
	root = ET.fromstring(response.read())

	# create folder structure
	createFolders(root,directory)
	to_download = []
	# get files to download
	getFiles(root,"",to_download)
	for download in to_download:
		# download file if it doesnt exist or if there is a new version
		file_path = directory+download['Path']+"/"+download['Name']
		if os.path.isfile(file_path):
			file_created = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
			if not file_created > download['Created']:
				download_file(elementID,download['Id'],file_path)
			else:
				print "Latest version already downloaded. "+download['Path']+"/"+download['Name']
		else:
			download_file(elementID,download['Id'],file_path)