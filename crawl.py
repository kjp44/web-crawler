from bs4 import BeautifulSoup
from urllib.request import urlopen
import save
import search
import ssl


def createSSL():
    try:
        context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = context

def crawler(crawledURLs, q, relatedTerms, pageLimit):
    savedPages = {}

    pageCount = 0

    while q.empty() == False:
        URL = q.get()

        pageContent = getPageContent(URL)

        if pageContent is None:
            continue

        soup = getSoup(pageContent)

        pageTitle = getPageTitle(soup)

        if not isPageSaved(pageTitle, savedPages):
            pageText = getPageText(soup)
            print('Searching ' + pageTitle + ' for relevant terms')
            if isPageRelevant(pageText, relatedTerms):
                save.saveFile(pageTitle, '.html', pageContent)
                savedPages[pageTitle] = URL
                links = getOutgoingLinks(soup)
                links = cleanOutgoingLinks(links)
                parseOutgoingURLs(links, crawledURLs, q)
                pageCount += 1
                print('#' + str(pageCount) + ': ' + pageTitle + ' - ' + URL + ' saved!')

        #if pageCount >= pageLimit:
            #break

    print('Saved ' + str(pageCount) + ' pages.')

    return savedPages

def getPageContent(URL):
    try:
        htmlResponseText = urlopen(URL).read()
        pageContent = htmlResponseText.decode('utf-8')
        return pageContent
    except Exception as e:
        return None


def getSoup(pageContent):
    soup = BeautifulSoup(pageContent, 'html.parser')
    return soup


def getPageText(soup):
    mainText = soup.get_text()
    return mainText


def getPageTitle(soup):
    title = cleanPageTitle(soup.title.string)
    return title

def cleanPageTitle(title):
    invalidCharacters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', ' - Wikipedia']
    for char in invalidCharacters:
        title = title.replace(char, '')
    return title

def isPageSaved(pageTitle, savedPages):
    if pageTitle in savedPages:
        return True
    else:
        return False

def isPageRelevant(pageText, relatedTerms):
    termCount = 0
    for term in relatedTerms:
        if search.searchForTerm(term, pageText):
            print(term)
            termCount += 1
            if termCount >= 2:
                return True
    return False


def getOutgoingLinks(soup):
    links = soup.find_all('a')
    return links

def cleanOutgoingLinks(links):
    URLs = []
    for link in links:
        URLs.append(link.get('href'))
    return URLs

def parseOutgoingURLs(URLs, crawledURLs, q):
    invalidLinks = '#|.jpg|.png|.svg|.bmp|.tiff|.jpeg|.pdf|disambiguation|booksources|template|category|portal|talk|whatlinkshere'
    validLinks = '^/wiki/'
    for URL in URLs:
        if (search.isGoodURL(URL, invalidLinks, validLinks)):
            URL = reformatWikiURL(URL)
            if URL not in crawledURLs:
                crawledURLs.append(URL)
                q.put(URL)
        else:
            continue    

def reformatWikiURL(URL):
    return "https://en.wikipedia.org" + URL