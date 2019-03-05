import re

def searchForTerm(term, content):
	if re.search(term, content, re.I):
		return True
	else:
		return False

def isGoodURL(URL, badTerm, goodTerm):
    if URL is None:
        return False
    if searchForTerm(badTerm, URL):
        return False
    if searchForTerm(goodTerm, URL):
    	return True
    else:
        return False