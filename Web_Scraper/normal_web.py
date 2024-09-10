import requests
from bs4 import BeautifulSoup
import uuid
# from Web_Scraper.models import News
import threading
import time
def WebScraper():
    url='https://www.imdb.com/news/movie/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    new_items=soup.find_all('div',class_='ipc-list-card--border-line')
    # arcticles=[]
    for item in new_items:
        title=item.find('a',class_='ipc-link ipc-link--base sc-bec740f7-3 gBbzGe')
        external_link=title['href']
        title=title.text.strip() if title else 'No Title'
        desc=item.find('div',class_="ipc-html-content-inner-div")
        desc=desc.text.strip() if desc else "No Descriptions "
        img=item.find('img',class_='ipc-image')
        if img and 'src' in img.attrs:
            img=img['src']
        else:
            img="No Image Avalabile"

        # print(f"Image: {img}")
        # arcticles.append({
        #     'Title':title,
        #     'Descriptions':desc,
        #     'External-Link':external_link,
        #     'Image':img
        # })
        # x=News(Title=title,desc=desc,External_link=external_link,img=img)
        # x.save()
        #For Downloading Images By Using Threading
        def downloader(url):
            response = requests.get(url).content
            with open(f"Images/{str(uuid.uuid4()).split('-')[0]}.jpg", 'wb') as f:
                f.write(response)

        if img != "No Image Available":
            start=time.time()
            p = threading.Thread(target=downloader, args=[img])
            p.start()
            p.join()  
            end=time.time()
            print(f"Total time taken: {end - start:.2f} seconds")
    # print('ALL DATA ADD SUCESSFULLY....')
WebScraper()