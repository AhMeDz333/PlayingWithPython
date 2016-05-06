
####################################
# File name: ClearProject.py       #
# Author: AhMeDz                   #
# Submission:  1 May 2016          #
####################################


from __future__ import division
from collections import Counter
import sys, re, math, itertools, urllib2

def divFound(content):
	pattern = r'Divide by two'
	return len(re.findall(pattern, content)) != 0

def recurse(content, n = 400, prev = -1):
	if n == 0:
		return

	pattern = r'nothing.*?(\d+)'
	num = re.findall(pattern, content)
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
	if len(num) != 0:
		url += str(num[0])
		prev = num[0]
	elif divFound(content):
		url += str(prev/2)
		prev /= 2
	else:
		print 'hehehehehehehe THE END!'
		return
	print url
	content = urllib2.urlopen(url).read()
	recurse(content, n-1)

#################################

source = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php').read()
# pattern = r'<!--([\s\S]*?)-->'
# pattern = r'nothing.*?(\d+)'
# l = re.findall(pattern, source)
recurse(source)



#nothing = 12345
#nothing is 12345
