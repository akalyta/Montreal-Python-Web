# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import urllib2
from UNHelper import scrapeSpeeches
import os
import re
from bs4 import BeautifulSoup

'''Download the full speeches (PDFs) made in the General Debate of
    the 66th, 67th, 68th Session of the U.N. General Assembly.
    Use PDFMiner to scrape text from the PDF document.'''

if __name__ == "__main__":

    baseURL = "http://gadebate.un.org/"

    # retrieve full speeches from the General Debate of
    # 68th session of the U.N. General Assembly
    #dates = ["2013-09-24","2013-09-25","2013-09-26","2013-09-27",
    dates = ["2013-09-26","2013-09-27",
                "2013-09-28", "2013-09-29", "2013-09-30", "2013-10-01"]

    targetDir = os.getcwd() + "/" + "UNGA_68"
    # make the target directory on your local machine if it doesn't already exist
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)

    # scrape speeches by calling the UNHelper.scrapeSpeeches() function
    for date in dates:
        # for each date, construct URL of web page containing list of statements
        url = baseURL + "homepage/" + date
        scrapeSpeeches("68",targetDir,url,baseURL)

    '''
    # use the scrapeSpeeches function to retrieve speeches
    # for the General Debate of the 66th and 67th sessions too.
    for sNum in ["66","67"]:
        targetDir = os.getcwd() + "/" + "UNGA_" + sNum

        # make the target directory if it doesn't already exist
        if not os.path.exists(targetDir):
            os.mkdir(targetDir)
        url = "http://gadebate.un.org/sessions-archive/" + sNum

        # scrape speeches by calling the UNHelper.scrapeSpeeches() function
        scrapeSpeeches(sNum,targetDir,url,baseURL)
    '''
