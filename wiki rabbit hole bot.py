from lxml import html
import requests, random

def filter(links, nullLink=[]):
    for link in links:
        if link.find('JPG') == -1:
            nullLink.append(link)
    return nullLink

links = []
p = str(requests.get('https://en.wikipedia.org/wiki/Main_Page').content)
pos = p.find('id="mp-upper"')

for i in range( p[p.find('id="mp-upper"'):p.find('id="mp-middle"')].count('href="/wiki/')):
    start = p.find('href="/wiki/', pos) + 6
    pos = p.find('"', p.find('href="/wiki/', pos) + 7)
    links.append( p[start:pos])

links = filter(links)

# loop for desired iterations
for depth in range(int(input("How deep will the rabbit hole go: "))):
    p = str(requests.get('https://en.wikipedia.org' + str(random.choice(links))).content)
    links = []
    # find all hrefs
    pos = 0
    for i in range( p.count('href="/wiki/')):
        start = p.find('href="/wiki/', pos) + 6
        pos = p.find('"', p.find('href="/wiki/', pos) + 7)
        links.append( p[start:pos])
    links = filter(links)
    
    #enter page
print('https://en.wikipedia.org' + random.choice(links))
# open chromium and display page



