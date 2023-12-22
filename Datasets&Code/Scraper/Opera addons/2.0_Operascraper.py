import urllib.request

# import urllib2
import re
import requests
import bs4
f = open("Opera_Permissions2.txt","w+",encoding='utf-8')
for line in open("urlsmerge.txt"):
    # page = urllib2.urlopen(line)
    # res = requests.get(line)
    # res.text
    res = requests.get(line)
    res = res.text
    # print(res)

    soup = bs4.BeautifulSoup(res, "html.parser")
    for name in soup.find_all('meta', property='og:title'):
        r_name = name.get('content')
        print(r_name)
        f.write(r_name+';')
    for tag in soup.find_all('div', class_='span-two-third'):
       # print(tag)
        m_name = tag.find('h1').get_text()
 #       print(m_name)

    for downloads in soup.find_all('section', class_='about l-top-margin'):
    #    print(downloads)
        for downloads_dl in downloads.find_all('dl'):
           downloads_dd= downloads_dl.find('dd').get_text()
     #      print(m_name)
           print(downloads_dd)

     #      f.write(m_name + ";")
           f.write(downloads_dd + ";")
    for rating in soup.find_all('span', class_='rating'):
        app_rating=rating.get_text()
        print(app_rating)
        f.write(app_rating + ";")
    for downloads_tag in soup.find_all('section', class_='about l-top-margin', recursive=False):
        downloads_num1 = downloads_tag.find('dd')
        #       downloads_num2 = downloads_num1.find('dd')
        print(downloads_num1)
        f.write(downloads_num1 + ";")
    for category in soup.find_all('meta', {"property": "aoc:category"}):
        meanings = category['content']
        print(meanings)
        f.write(meanings + ";")

    for tag2 in soup.find_all('ul', class_='hidden'):  # works
            per_class = tag2.findAll('li')
            li_content = []
            for i in per_class:
                print(i.text)
                f.write(i.text + ";")



    f.write("\n")




  #          f.write(i.text + ";")

#    print(name)

       # print(tag)

f.close()
"""        for category in downloads.find_all('dl'):
           category_extension= category.find_all('dd')
           for each in category_extension:

            #   txtlist = each.find('a').get_text()
            #   print(txtlist)


               txtlist= each.find_all('a')
               for eachs in txtlist:
  #                 for x in range(1):
                        txtstr = eachs.string
                        print(txtstr)   #works, but some contents are useless like privacy policy'''
                        f.write(txtstr +";")


            #       txtstr = eachs.string
            #       print(txtstr)   #works, but some contents are useless like privacy policy'''
            #       f.write(txtstr +"\n") """




  #         f.write(category_extension.text + "\n")






 #   mmm = soup.find('ul', class_='hidden').get_text()
 #   print(mmm)

'''    permisson1 = per_class[0].contents[0]
        print(permisson1)
        permisson2 = per_class[1].contents[0]
        print(permisson2)
        permisson3 = per_class[2].contents[0]
        print(permisson3)
        permisson4 = per_class[3].contents[0]
        print(permisson4)
        permisson5 = per_class[4].contents[0]
        print(permisson5)
        permisson6 = per_class[5].contents[0]
        print(permisson6)
        permisson7 = per_class[6].contents[0]
        print(permisson7)
        permisson8 = per_class[7].contents[0]
        print(permisson8)   '''

        #      permission = tag2.find_all('li')# works for 1 permission

  #      print(permission) #this line works

    #    name = soup.find('span', class_='title').contents[0]
#   print(name)
 #   for tag in soup.find('h1', {"dir": "ltr"}):
 #       meanings=
        #m_rating_score = str(tag.find('span', class_='rating_num').get_text())
      #  meanings =tag.find('meta').get('content')
  #      print(tag)
       # m_name = tag.find('content').get_doc()


