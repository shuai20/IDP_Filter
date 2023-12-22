import requests
import bs4

rooturl = "https://addons.opera.com"

categorie1 = [ "translation"]
categorie2 = ["music", "news-weather"]
categorie3 = [ "appearance", "downloads",  "search"]
categorie4 = ["accessibility","fun",  "shopping"]
categorie5 = ["privacy-security", "developer-tools", ]
categorie6 = ["social"]
categorie7 = ["productivity"]

f = open("trans.txt", "w+")
for x in categorie1:
    for i in range(1):
        url_str = "https://addons.opera.com/en/extensions/category/" + x + "/?page="
        # url_str  = "https://addons.opera.com/en/extensions/?page=" + x + "order="
        pagenum = str(i)
        final_url_str = url_str + pagenum + "&order=popular"
        res = requests.get(final_url_str)
        res.text
        print(final_url_str)

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        for link in soup.find_all('li', {"class": "package span-one-fourth s-top-margin"}):


            meanings = link.find_all('a')[0]['href']
            print(meanings)
    # print('a标签的href属性是：', meanings.a.attrs)
            f.write(rooturl + meanings + "\n")
f.close()

f = open("music-news.txt", "w+")
for x in categorie2:
    for i in range(1,3):
        url_str = "https://addons.opera.com/en/extensions/category/" + x + "/?page="
        # url_str  = "https://addons.opera.com/en/extensions/?page=" + x + "order="
        pagenum = str(i)
        final_url_str = url_str + pagenum + "&order=popular"
        res = requests.get(final_url_str)
        res.text
        print(final_url_str)

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        for link in soup.find_all('li', {"class": "package span-one-fourth s-top-margin"}):


            meanings = link.find_all('a')[0]['href']
            print(meanings)
    # print('a标签的href属性是：', meanings.a.attrs)
            f.write(rooturl + meanings + "\n")
f.close()

f = open("appearance-download-search.txt", "w+")
for x in categorie3:
    for i in range(1,4):
        url_str = "https://addons.opera.com/en/extensions/category/" + x + "/?page="
        # url_str  = "https://addons.opera.com/en/extensions/?page=" + x + "order="
        pagenum = str(i)
        final_url_str = url_str + pagenum + "&order=popular"
        res = requests.get(final_url_str)
        res.text
        print(final_url_str)

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        for link in soup.find_all('li', {"class": "package span-one-fourth s-top-margin"}):


            meanings = link.find_all('a')[0]['href']
            print(meanings)
    # print('a标签的href属性是：', meanings.a.attrs)
            f.write(rooturl + meanings + "\n")
f.close()

f = open("access-shopping-fun.txt", "w+")
for x in categorie4:
    for i in range(1,5):
        url_str = "https://addons.opera.com/en/extensions/category/" + x + "/?page="
        # url_str  = "https://addons.opera.com/en/extensions/?page=" + x + "order="
        pagenum = str(i)
        final_url_str = url_str + pagenum + "&order=popular"
        res = requests.get(final_url_str)
        res.text
        print(final_url_str)

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        for link in soup.find_all('li', {"class": "package span-one-fourth s-top-margin"}):


            meanings = link.find_all('a')[0]['href']
            print(meanings)
    # print('a标签的href属性是：', meanings.a.attrs)
            f.write(rooturl + meanings + "\n")
f.close()

f = open("privacy-developtools.txt", "w+")
for x in categorie5:
    for i in range(1,6):
        url_str = "https://addons.opera.com/en/extensions/category/" + x + "/?page="
        # url_str  = "https://addons.opera.com/en/extensions/?page=" + x + "order="
        pagenum = str(i)
        final_url_str = url_str + pagenum + "&order=popular"
        res = requests.get(final_url_str)
        res.text
        print(final_url_str)

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        for link in soup.find_all('li', {"class": "package span-one-fourth s-top-margin"}):


            meanings = link.find_all('a')[0]['href']
            print(meanings)
    # print('a标签的href属性是：', meanings.a.attrs)
            f.write(rooturl + meanings + "\n")
f.close()

f = open("social.txt", "w+")
for x in categorie6:
    for i in range(1,7):
        url_str = "https://addons.opera.com/en/extensions/category/" + x + "/?page="
        # url_str  = "https://addons.opera.com/en/extensions/?page=" + x + "order="
        pagenum = str(i)
        final_url_str = url_str + pagenum + "&order=popular"
        res = requests.get(final_url_str)
        res.text
        print(final_url_str)

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        for link in soup.find_all('li', {"class": "package span-one-fourth s-top-margin"}):


            meanings = link.find_all('a')[0]['href']
            print(meanings)
    # print('a标签的href属性是：', meanings.a.attrs)
            f.write(rooturl + meanings + "\n")
f.close()

f = open("productivity.txt", "w+")
for x in categorie7:
    for i in range(1,21):
        url_str = "https://addons.opera.com/en/extensions/category/" + x + "/?page="
        # url_str  = "https://addons.opera.com/en/extensions/?page=" + x + "order="
        pagenum = str(i)
        final_url_str = url_str + pagenum + "&order=popular"
        res = requests.get(final_url_str)
        res.text
        print(final_url_str)

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        for link in soup.find_all('li', {"class": "package span-one-fourth s-top-margin"}):


            meanings = link.find_all('a')[0]['href']
            print(meanings)
    # print('a标签的href属性是：', meanings.a.attrs)
            f.write(rooturl + meanings + "\n")
f.close()


