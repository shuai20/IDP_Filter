import requests
import bs4

rooturl = "https://addons.mozilla.org"
categories = ["appearance","alerts-updates","bookmarks",
"download-management","feeds-news-blogging","games-entertainment",
"language-support","other","photos-music-videos","privacy-security",
"search-tools","shopping","social-communication","tabs","web-development"]

f = open("urls.txt","w+")

for x in categories:
	for i in range(135): 

		url_str  = "https://addons.mozilla.org/en-US/firefox/search/?category=" + x + "&sort=recommended%2Cusers&type=extension&page="
		pagenum = str(i)
		final_url_str = url_str + pagenum
		res = requests.get(final_url_str)
		res.text
		soup = bs4.BeautifulSoup(res.text, 'lxml')
		for link in soup.find_all('a', {"class":"SearchResult-link"}, href=True):
			f.write(rooturl + link['href'] + "\n")



f.close()



# this is the test of the vcs
# this is the test 2 for the vcs
