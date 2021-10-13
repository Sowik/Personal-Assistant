import feedparser
from PersonalAss import Assistant
import wikipedia

def rssfeed():

    urls = ["http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
            "http://feeds.bbci.co.uk/news/england/london/rss.xml",
            "http://feeds.bbci.co.uk/news/world/europe/rss.xml",
        ]

#feed = feedparser.parse("http://feeds.bbci.co.uk/news/england/london/rss.xml")
    posts = []
    for url in urls:
        posts.extend(feedparser.parse(url).entries)

    for post in posts:
        date = "(%d/%02d/%02d)" % (post.published_parsed.tm_year,\
        post.published_parsed.tm_mon, \
        post.published_parsed.tm_mday)
        data=("post date: " + date+"\n"+
        "post title: " + post.title+"\n"+
        "post link: " + post.link+"\n")
        print(data)
        Assistant.speak(data)
        print("|---------NEXT-----------|")