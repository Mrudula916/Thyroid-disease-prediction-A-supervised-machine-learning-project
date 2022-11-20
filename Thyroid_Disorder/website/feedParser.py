import feedparser

class ParseFeed():

    def __init__(self, url):
        self.feed_url = url

    def parse(self):
        '''
        Parse the URL, and print all the details of the news 
        '''
        feeds = feedparser.parse(self.feed_url).entries
        feeds_list = {}
        counter = 0
        for f in feeds:
            if(counter == 10):
                break
            feeds_list[counter] = {
                'Published Date': f.get("published", ""),
                'Title': f.get("title", ""),
                'Url': f.get("link", "")
            }
            counter += 1
        return feeds_list
    
def dict_parse(dict):
    for key in dict:
        try:
            dict[key] = float(dict[key])
        except:
            dict[key] = 1 if dict[key] == "yes" else 0
    return dict