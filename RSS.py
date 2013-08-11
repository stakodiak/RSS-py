# RSS.py - Uses XML library instead of re.
import urllib2 as u2
import xml.etree.ElementTree as ET


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
