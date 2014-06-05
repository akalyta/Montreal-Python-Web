# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import urllib2
import re
import time
import commands as cmds
from bs4 import BeautifulSoup

'''Helper functions for scraping the U.N. General Debate speeches.'''

def scrapePDF(pdfName,txtName):
        ''' pdfName = path to input PDF file
            txtName = path to the output text file

        This function uses PDFMiner to scrape
        a PDF file and save it as a text file
        with .txt extension'''

        status,txtOutput  = cmds.getstatusoutput("pdf2txt.py " + pdfName)
        with open(txtName,"wb") as fout:
            fout.write(txtOutput)

def scrapeSpeeches(sessionNum,targetDir,url,baseURL):
    ''' sessionNum = U.N. session number and URL with a list of links
        targetDir = local directory in which to save speeches
        url = U.N. web page with a list of links to country pages
        baseURL = base URL for the U.N. general debate documents

        This function follows links to country pages and downloads
        speeches in PDF format. Text from the PDF document is
        extracted using PDFMiner.'''

    # parse the HTML content on the page to obtain links to the country pages
    soup = BeautifulSoup(urllib2.urlopen(url).read())

    links = [tag["href"] for tag in soup.find_all(href=re.compile("/" + sessionNum +"/.*"))]
    print("Found {0} links.".format(len(links)))

    # follow link to each of the country pages
    for link in links:
        countryURL = baseURL + link
        countrySoup = BeautifulSoup(urllib2.urlopen(countryURL).read())

        try:
            # obtain URL of the PDF file corresponding to the country's
            # statement (in English)
            pdfURL = countrySoup.find(href=re.compile(".*pdf"),text=re.compile("English"))["href"]

            # download the PDF file
            pdfName = targetDir + "/" + "statement" + link.replace("/","_") + ".pdf"
            txtName = pdfName + ".txt"

            with open(pdfName,"wb") as fout:
                fout.write(urllib2.urlopen(pdfURL).read())

            # scrape text from PDF file
            scrapePDF(pdfName,txtName)

            # inject interval - be nice
            time.sleep(5)
        except Exception as e:
            # an exception is encountered if the country page does not have a
            # link to an English version PDF
            #print(e)
            print("Exception encountered for countryURL is {0}.".format(countryURL))
            pass
