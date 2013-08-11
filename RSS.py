# RSS.py - Uses XML library instead of re.
import urllib2 as u2
import xml.etree.ElementTree as ET


def main ():
    # Test Google News.
    print "Google News feed:"
    url = 'https://news.google.com/news/feeds?hl=en&gl=us&authuser=0&q=RSS&num=10&um=1&ie=UTF-8&output=rss'
    feed = RSS (url)
    for i in feed:
        print i['title']
    print ""

    # Get HN feed.
    print "HN frontpage:"
    url = 'https://news.ycombinator.com/rss'
    feed = RSS (url)
    for i in feed:
        print i['title']
    print ""

    # Try a subreddit.
    print "r/compsci RSS:"
    url = 'http://www.reddit.com/r/compsci/.rss'
    feed = RSS (url)
    for i in feed:
        print i['title']

def RSS (url):
    # Returns a list of RSS-dict elements.
    feed = list()

    # Get items from RSS channel.
    RSS_feed = u2.urlopen (url).read()
    root = ET.fromstring(RSS_feed)
    for i in root.findall ('./channel/item'):
        elem = dict()
        for j in i:
            elem [j.tag] = j.text
        feed.append (elem)

    return feed

if __name__ == '__main__':
    main()
