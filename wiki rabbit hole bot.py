from lxml import html
import requests, random


# will filter out all JPG related hrefs (Wiki only uses JPGS as their image type)
def filter(links):
    for link in links:
        if link.find('JPG') != -1:
            link.pop(links.index(link))
    return links


# request the homepage of wiki and search within a certain part of the HTML
links = []
p = str(requests.get('https://en.wikipedia.org/wiki/Main_Page').content)
pos = p.find('id="mp-upper"')

# find every reference to hyper references
for i in range( p[p.find('id="mp-upper"'):p.find('id="mp-middle"')].count('href="/wiki/')):
    links.append( p[p.find('href="/wiki/', pos) + 6: p.find('"', p.find('href="/wiki/', pos) + 7)] )
    # find intro to list, add length of list : find outro of list

# filter references to only websites
links = filter(links)

# loop for desired iterations
for depth in range(int(input("How deep will the rabbit hole go: "))):
    # request new website
    p = str(requests.get('https://en.wikipedia.org' + str(random.choice(links))).content)
    links = []
    # find all hrefs in the new site
    # start search at start of HTML of site (can be improved for faster load times # might add later)

    pos = 0
    for i in range( p.count('href="/wiki/')):
        links.append( p[p.find('href="/wiki/', pos) + 6:p.find('"', p.find('href="/wiki/', pos) + 7)])
    # filter references
    links = filter(links)
    
# post final website retreived
print('https://en.wikipedia.org' + random.choice(links))




