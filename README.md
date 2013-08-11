## RSS.py
Grabs the good stuff from an RSS url. 

Typically available keys are ```['guid', 'link', 'description', 'pubDate', 'title']```.

#### Google News
Search Google News for "florida man":
```
Python 2.7.5 (default, May 19 2013, 13:26:46) 
[GCC 4.2.1 Compatible Apple Clang 4.1 ((tags/Apple/clang-421.11.66))] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from RSS import RSS
>>> url = 'https://news.google.com/news/feeds?q=%22florida+man%22&ie=UTF-8&output=rss'
>>> feed = RSS (url)
>>> for i in feed:
...     print i['title']
... 
Florida man allegedly kills wife, posts confession, photo of body on Facebook - CNN (blog)
Police: Florida man stabbed daughter with sword - Naples Daily News
7-year sentence for Florida man who fled crash that killed former Bergen ... - Hunterdon County Democrat -  NJ.com
The Florida man who allegedly killed his wife and documented it on Facebook - The Week Magazine
Florida Man Wanted in East Cobb Molestation - Patch.com
Florida man who reports killing wife and posts photo on Facebook held without ... - Bradenton Herald
Police: Man stabbed daughter with sword - MiamiHerald.com
South Florida man accused of fatally shooting wife, posting photo of body on ... - Fox News
Florida man murders wife, posts photo of lifeless body on Facebook: report - Washington Times
Florida man accused of killing wife, posting grisly photo on Facebook - Detroit Free Press
>>> 
```

#### Yahoo! News
Search Y!N with same query:
```
>>> url ='http://news.search.yahoo.com/rss?q=%22florida+man%22'
>>> feed = RSS (url)
>>> for i in feed:
...     print i['title']
... 
Florida man allegedly kills wife, posts confession, photo of body on Facebook
Florida man accused of killing wife, posting grisly photo on Facebook
Police: Florida Man Stabbed Daughter With Sword
Florida man held on charges he disrupted flight from Russia
Florida man accused of killing wife, posting photo to Facebook
Fla. man accused of killing wife, posting photo
Florida man accused of fatally shooting wife apparently posted photo of her body on Facebook
Fla. man accused of killing wife; posted photo
The Florida man who allegedly killed his wife and documented it on Facebook
South Florida man accused of fatally shooting wife, posting photo of body on Facebook
>>> 
```
Check the dates on these results:
```
>>> for i in feed:
...     print i['pubDate']
... 
Sun, 11 Aug 2013 09:11:08 -0700
Fri, 09 Aug 2013 06:20:16 -0700
Sun, 11 Aug 2013 08:43:41 -0700
Fri, 09 Aug 2013 13:27:25 -0700
Thu, 08 Aug 2013 19:44:17 -0700
Thu, 08 Aug 2013 16:31:04 -0700
Fri, 09 Aug 2013 01:37:08 -0700
Thu, 08 Aug 2013 15:45:59 -0700
Fri, 09 Aug 2013 03:41:00 -0700
Thu, 08 Aug 2013 15:45:56 -0700
>>> 
```
