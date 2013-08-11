# Checks RSS function with a few feeds. Should put in exception blocks...
from RSS import RSS


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

if __name__ == '__main__':
    main()
