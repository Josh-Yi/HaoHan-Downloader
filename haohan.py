import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
url = 'https://www.sohu.com/a/449542309_523187'
browser.open(url)
print(browser.get_url())

browser
page = browser.get_current_page()
all_images = page.find_all('img')

imgs = []
for img in all_images:
    img = img.get('src')
    imgs.append(img)
print(imgs)

imgs = [img for img in imgs if img.startswith('https')]
print(imgs)

import os
import wget

path = os.getcwd()
print(path)
path = os.path.join(path, 'imgs')
os.mkdir(path)

counter = 0
for img in imgs:
    save = os.path.join(path, 'img{}.jpg'.format(counter))
    wget.download(img, save)
    counter += 1
