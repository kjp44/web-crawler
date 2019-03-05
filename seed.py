import queue


def getSeedURLsQ(seedURLs):
    q = queue.Queue()
    for URL in seedURLs:
    	q.put(URL)
    return q


def getRelatedTerms():
	relatedTerms = [r'\bsnakes?\b',
	r'\bpythons?\b',
	r'\bboas?\b',
	r'\bvipers',
	r'\bmambas?\b',
	r'\bcolubrids?\b',
	r'\badders?\b',
	r'\banacondas?\b',
	r'\basps?\b',
	r'\bcobras?\b',
	r'\bconstricts?\b',
	r'\bvenom']
	return relatedTerms