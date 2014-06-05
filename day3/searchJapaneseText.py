#coding: utf-8

# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import re
import urllib2
from bs4 import BeautifulSoup

"""Count the frequency of specific unicode patterns in all the statements
    made by the Permanent Japanese Mission to the U.N. in the period 2002-2014."""

if __name__=="__main__":

    searchStrAfg = u"アフガニスタン"
    searchStrNK = u"北朝鮮"

    patternAfg = re.compile(searchStrAfg)
    patternNK = re.compile(searchStrNK)

    countAfg = 0
    countNK = 0

    for i in range(2002,2014):
        url = "http://www.un.emb-japan.go.jp/jp/statements/%s.html" % i
        print "Fetching url %s....." % url
        html = urllib2.urlopen(url).read()

        soup = BeautifulSoup(html)

        """Count the number of references to Afghanistan and North Korea in the document."""
        rowTags = soup.find_all("tr")
        for rowTag in rowTags:
            colTags = rowTag.find_all("td")
            if(colTags):
                colTag = colTags[0]
                afgTag = colTag.find(text=patternAfg)
                if(afgTag):
                    countAfg += 1
                NKTag = colTag.find(text=patternNK)
                if(NKTag):
                    countNK += 1

    print "Total number of Statements with Afghanistan in the title is %d" % countAfg
    print "Total number of Statments with North Korea in the title is %d" % countNK
