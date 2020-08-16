import feedparser
# locCode=EUR|TR|06420|ANKARA| > KITA|ULKE|POSTAKODU|IL 
def hava():
    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|06420|ANKARA|")
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    print (parse[2], parse[4], parse[5])
    return (hava)

hava()
