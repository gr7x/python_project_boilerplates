import bs4 as bs
import urllib.request

#sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
#soup = bs.BeautifulSoup(sauce, 'lxml')

## --- parse urls with xml ----  ---------------
##sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
##
##soup = bs.BeautifulSoup(sauce, 'xml')
##print(soup)
##
##for url in soup.find_all('loc'):
##    print(url.text)
## ----- ----------------------  -----------
#print(soup)

#print(soup.title)

#print(soup.p)

#print(soup.find_all('p'))


##for paragraph in soup.find_all('p'):
##       print(paragraph.string)
##       print(paragraph.text)
##

#print(soup.get_text())

#for url in soup.find_all('a'):
#    print(url)
#    print(url.text)
#    print(url.get('href'))


##---------- new topic -------------##
#look through nav bar
##nav = soup.nav
##print(nav)
##for url in nav.find_all('a'):
##    print(url.get('href'))
    

##body = soup.body
##for paragraph in body.find_all('p'):
##    print(paragraph.text)


##for div in soup.find_all('div', class_='body'):
##    print(div.text)
##

##table = soup.table
##
##print(table)
##
##table2 = soup.find('table')
##
##table_rows = table.find_all('tr')
##
##for tr in table_rows:
##    td = tr.find_all('td')
##    row = [i.text for i in td]
##    print(row)


#---------------------------------------------------

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)

