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

"""Extract information from the table of MPs and print as comma-separated values."""

#URL = "http://www.parl.gc.ca/parlinfo/Lists/Members.aspx"
URL = "http://www.parl.gc.ca/parlinfo/Lists/Members.aspx?Parliament=1924d334-6bd0-4cb3-8793-cee640025ff6&Riding=&Name=&Party=&Province=&Gender=&New=False&Current=False&First=False&Picture=False&Section=False&ElectionDate="
baseURL = "http://www.parl.gc.ca/parlinfo/"

resp = urllib2.urlopen(URL).read()

MPInfo = re.findall(r"href=\"..\/(.*Parliamentarian.*)\">(.*)</a>",resp)
partyInfo = re.findall(r"=.*Party.aspx.*>(.*)</a>",resp)
constituencyInfo = re.findall(r"=.*?Party.aspx.*?>.*?</a>.*?</td>.*?<td class=\"ColumnAlignToLeft\">(.*?)</td>",resp,re.DOTALL)

df = pd.DataFrame(columns=["name","affiliation","constituency","email","parl_address","parl_telephone","parl_fax"])

#follow the MPs URL and save MP info in the DataFrame variable df

#for idx in range(0,len(MPInfo)):
for idx in range(0,3):
    url_str,name_str = MPInfo[idx]
    party_str = partyInfo[idx]
    constituency_str = constituencyInfo[idx]

    MPURL = baseURL + urllib.unquote(MPInfo[0][0])
    MPURL = MPURL.replace("&amp;","&")
    resp = urllib2.urlopen(MPURL).read()
    MPSoup = BeautifulSoup(resp)

    contactURL = re.sub("Section=False&","Section=ContactInformation&",MPURL)
    contactSoup = BeautifulSoup(urllib2.urlopen(contactURL).read())

    telephoneTags  = contactSoup.find_all(id=re.compile("Telephonenumber"))
    telephone_str = telephoneTags[0].string
    fax_str = telephoneTags[1].string
    addressTag = contactSoup.find(id=re.compile("grdParliamentaryAddress_ctl02_Label2"))
    address_str = re.sub("[\t\r\n]",",",addressTag.text)
    emailTag = contactSoup.find(href=re.compile("mailto:"))
    email_str = emailTag.text

    df = df.append({"name":name_str.strip(),
                    "affiliation":party_str.strip(),
                    "constituency":constituency_str.strip(),
                    "email":email_str.strip(),
                    "parl_telephone":telephone_str.strip(),
                    "parl_fax":fax_str.strip(),
                    "parl_address":address_str.strip()
                }, ignore_index=True)

#write MPs dataframe to a csv file
df.to_csv("MPs.csv",sep=",",index=False)
