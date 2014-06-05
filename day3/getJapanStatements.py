#coding: utf-8

# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop


import re
import codecs
import urllib2
import urllib
from bs4 import BeautifulSoup

"""Retrieve all the 2013 statements made by the Permanent Japanese Mission to the U.N."""

if __name__=="__main__":

            prefix = "http://www.un.emb-japan.go.jp/jp/statements"
            url = "http://www.un.emb-japan.go.jp/jp/statements/2013.html"
            html = urllib2.urlopen(url).read()

            soup = BeautifulSoup(html)
            """Find the tag object corresponding to the table element"""
            #table = soup.find(text=re.compile(u"タイトル")).parent.parent.parent
            table = soup.find("table",width="97%")

            """Go through each row and fetch the link in the first column."""
            rowTags = table.find_all("tr")
            for rowTag in rowTags:
                colTags = rowTag.find_all("td")
                if(colTags):
                    linkURLs = colTags[0].find_all("a")

                    # get statement in second language (non-English) if available
                    if(len(linkURLs) > 1):
                        linkURL = linkURLs[1].get("href")
                    else:
                        linkURL = linkURLs[0].get("href")

                    # check if it is a PDF file or HTML file
                    if(re.search("\.pdf",linkURL)):
                        linkURL = re.sub(".*\/statements\/([A-Za-z].*\.pdf)","\g<1>",linkURL)
                        PDFName = linkURL
                        print("Downloading file: {0}/{1}.".format(prefix,linkURL))
                        urllib.urlretrieve("{0}/{1}".format(prefix,linkURL),
                                                PDFName)
                    else:
                        linkURL = re.sub(".*\/statements\/([A-Za-z].*\.(html))","\g<1>",linkURL)
                        statement = urllib2.urlopen("%s/%s" % (prefix,linkURL)).read()
                        localFile = linkURL
                        print("Downloading file: {0}/{1}.".format(prefix,linkURL))
                        fout = codecs.open(localFile,"w","utf-8")
                        fout.write(statement.decode("utf-8"))
                        fout.close()
