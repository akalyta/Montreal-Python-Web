#coding:utf-8

# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import sys

"""Test exercises to encode and decode Unicode strings."""

if __name__=="__main__": 
    strAfg = u"アフガニスタン" 
    strCDI = u"cote d’ivoire"

    print(strAfg.encode("utf-8"))

    """Does this work?"""
    utf8Enc = strAfg.encode("utf-8",errors="strict")

    """Does this work? Uncomment and try it."""
    #strAfg.encode("ascii",errors="strict")
    #strAfg.encode("ascii",errors="ignore")
    #strAfg.encode("ascii",errors="replace")

    """Does this work? Uncomment and try it."""
    #strAfg.encode("latin-1",errors="strict")
    #strCDI.encode("latin-1",errors="strict")

    """Try decoding"""
    #utf8Enc.decode("utf-8")

