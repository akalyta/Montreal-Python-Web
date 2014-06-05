# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import urllib2
from bs4 import BeautifulSoup
import pandas as pd

'''This Python script reads Senators' contact information from
   http://www.senate.gov/general/contact_information/senators_cfm.xml.
   It parses the first and last names, party and state
   and prints this information to screen for all the Senators.'''

# instantiate pandas DataFrame to store scraped Senator information
senatorsDF = pd.DataFrame(columns = ["first_name","last_name","party","state"])

# Download the XML document from Senate website and create a BeautifulSoup
# object
url = "http://www.senate.gov/general/contact_information/senators_cfm.xml"
xml = urllib2.urlopen(url).read()
soup = BeautifulSoup(xml)

#print soup.prettify()

print "List of Senators and affiliations obtained from www.senate.gov:"

# Find all the member tag objects in the XML document using find_all()
for member in soup.find_all("member"):

    first_name_str = member.first_name.string
    last_name_str = member.last_name.string
    party_str = member.party.string
    state_str = member.state.string
    senatorsDF = senatorsDF.append({"first_name":first_name_str, \
                        "last_name":last_name_str, \
                        "party":party_str, \
                        "state":state_str},ignore_index=True)

# Print dataframe to screen
print("{0:10s}\t,{1:10s}\t,{2:10s}\t,{3:10s}".
        format("first_name",
                "last_name",
                "party",
                 "state"))
for i,row in senatorsDF[1:20].iterrows():
     print("{0:10s}\t,{1:10s}\t,{2:10s}\t,{3:10s}".
             format(row['first_name'],
                    row['last_name'],
                    row['party'],
                    row['state']))

# Another quick way to Print dataframe to screen
# print(senatorsDF.head(20))

# Write dataframe to csv file
senatorsDF.to_csv("senatorsPA.csv",sep=",",index=False)
