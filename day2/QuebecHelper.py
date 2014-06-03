# coding: utf-8
# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

from bs4 import BeautifulSoup
import urllib2
import urllib
import pandas as pd
import re
import sys
import codecs

''' Method that takes in column tag objects and extract electoral information.
    Works with Quebec election data available at:
    "http://www.assnat.qc.ca/en/patrimoine/resultatselec/" '''

def scrapeQuebecRows(cols,year):
    # initialize defaults
    prevYear = year
    name = ""
    party = ""
    votes = ""
    count = ""
    dummyVal = "-1"

    # if there are five columns in the row
    if(len(cols) == 5):
        year = cols[0].string if cols[0].string else cols[0].text
        year = year if re.search("\d",year) else prevYear

        name = cols[1].string if cols[1].string else cols[1].text
        party = cols[2].string if cols[2].string else cols[2].text
        votes = cols[3].string if cols[3].string else cols[3].text
        count = cols[4].string if cols[4].string else cols[4].text
        count = count if re.search("\d",count) else dummyVal

        votes = re.sub(u"\s*","",votes)
        count = re.sub(u"\s*","",count)

    # if there are four columns in the row
    if(len(cols) == 4):
        tmpVal = cols[0].string if cols[0].string else cols[0].text

        # check if first column contains a year
        if(re.search("\s*\d\d\d\d",tmpVal)):
            year = tmpVal
            name = cols[1].string if cols[1].string else cols[1].text
            party = cols[2].string if cols[2].string else cols[2].text
            votes = cols[3].string if cols[3].string else cols[3].text

        # else if first column doesn't contain year, then it must be a
        # name
        else:
            year = prevYear
            name = tmpVal
            party = cols[1].string if cols[1].string else cols[1].text
            votes = cols[2].string if cols[2].string else cols[2].text

        votes = re.sub(u"\s*","",votes)
        count = dummyVal

    return (year,name,party,votes,count)
