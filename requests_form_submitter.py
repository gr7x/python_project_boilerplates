import requests
import webbrowser
 
url = 'https://duckduckgo.com/html/'
payload = {'q':'pythons'}
r = requests.get(url, params=payload)
with open("requests_results.html", "wb") as f:
    f.write(r.content)


webbrowser.open("requests_results.html")
