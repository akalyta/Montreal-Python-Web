# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

from bs4 import BeautifulSoup
import urllib2

'''Print rows from a HTML table.'''

URL = "http://beta.congress.gov/congressional-record/browse-by-date/"
soup = BeautifulSoup(urllib2.urlopen(URL).read())

table = soup.find("table")

childRows = table.find_all("tr")
for i in range(1,len(childRows)):
    print(childRows[i])
