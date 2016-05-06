
####################################
# File name: ClearProject.py       #
# Author: AhMeDz                   #
# Submission:  1 May 2016          #
####################################


from __future__ import division
from collections import Counter
import sys, re, math, itertools, urllib2

def isAlpha(c):
	return c.isalpha() or c == ' '

#################################

source = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
pattern = r'<!--([\s\S]*?)-->'
l = re.findall(pattern, source)
for item in l:
	print "".join(filter(lambda c: isAlpha(c), item))



