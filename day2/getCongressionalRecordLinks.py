# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

from bs4 import BeautifulSoup
import urllib2

'''Extract and print link information from the Senate Section column.'''

URL = "http://beta.congress.gov/congressional-record/browse-by-date/"
soup = BeautifulSoup(urllib2.urlopen(URL).read())
baseURL = "http://beta.congress.gov/"

table = soup.find("table")

childRows = table.find_all("tr")

for childRow in childRows[1:]:
    childColumns = childRow.find_all("td")
    try:
        print("%s, %s%s\n" \
                % (childColumns[2].find("a").text,\
                baseURL,childColumns[2].find("a").get("href")))
    except:
        pass
