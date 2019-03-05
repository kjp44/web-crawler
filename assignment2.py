import seed
import save
import crawl

seedURLs = ['https://en.wikipedia.org/wiki/Snake', 
    'https://en.wikipedia.org/wiki/Reptile']

seedQ = seed.getSeedURLsQ(seedURLs)

relatedTerms = seed.getRelatedTerms()

pageLimit = 100

save.createDirectory('Assignment 2')

save.changeDirectory('Assignment 2')

crawl.createSSL()

savedPages = crawl.crawler(seedURLs, seedQ, relatedTerms, pageLimit)

save.saveFile('_CRAWLED_URLS_', '.txt', save.dictToSave(savedPages))