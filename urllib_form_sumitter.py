import urllib
import urllib.request
#import urllib2
import webbrowser
 
data = urllib.parse.urlencode({'q': 'Python2'})
url = 'http://duckduckgo.com/html/'
full_url = url + '?' + data
response = urllib.request.urlopen(full_url)
with open("results.html", "wb") as f:
    f.write(response.read())
 
webbrowser.open("results.html")
