from bs4 import BeautifulSoup
import requests
url = 'http://www.youtube.com/results?search_query=%(q)s'
busca = {
    'q': raw_input('>> Buscar: '),
}
r = requests.get(url % busca)

soup = BeautifulSoup(r.text, "html.parser")
titulo = [(title.text, title.a) for title in soup.find_all('h3', class_="yt-lockup-title")]

i = 0
for t in titulo:
    i+=1
    print str(i)+')', t[0]
    try:
        print "Link para acesso: http://www.youtube.com" + t[1]['href']
    except TypeError:
        print "Sem link para acesso."
    print ""