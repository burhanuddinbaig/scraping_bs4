from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())

#s = soup.title.name

#s = soup.title.string

#s = soup.title.parent.name

#s = soup.p	# to get a div

#s = soup.p['class']

#s = soup.a

#s = soup.find_all('a')

#s = soup.find('a')

#s = soup.find(id='link3')

s = soup.find_all(href="http://example.com/lacie")

print(s)