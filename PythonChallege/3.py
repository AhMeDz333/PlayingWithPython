
####################################
# File name: ClearProject.py       #
# Author: AhMeDz                   #
# Submission:  1 May 2016          #
####################################


from __future__ import division
from collections import Counter
import sys, re, math, itertools, urllib2

def isAlpha(c):
	return c.isalpha()

#################################

source = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read().replace('\n', '')
pattern = r'<!--([\s\S]*?)-->'
l = re.findall(pattern, source)
pattern = r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+'
print l
for item in l:
	print "".join(re.findall(pattern, item))


