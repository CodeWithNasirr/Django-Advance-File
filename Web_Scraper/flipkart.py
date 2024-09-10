import requests
from bs4 import BeautifulSoup
import uuid
# from Web_Scraper.models import News
import threading
import time
import random
def WebScraper():
    # url='https://www.imdb.com/news/movie/'
     url = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY'
     user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    ]
    
     headers = {
        'User-Agent': random.choice(user_agents),
        'Referer': 'https://www.flipkart.com/',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    
    # Send the request
     response = requests.get(url, headers=headers)
    
    # Check the response status
     if response.status_code == 200:
        soup=BeautifulSoup(response.text,'html.parser')
        print(soup)
        new_items=soup.find_all('div',class_='_75nlfW')
        
        arcticles=[]
        for item in new_items:

            title=item.find('div',class_='KzDlHZ')
            # external_link=title['href']
            title=title.text.strip() if title else 'No Title'
            desc=item.find('li',class_="J+igdf")
            desc=desc.text.strip() if desc else "No Descriptions "
            img=item.find('img',class_='DByuf4')
            if img and 'src' in img.attrs:
                img=img['src']
            else:
                img="No Image Avalabile"

            # x=News(Title=title,desc=desc,img=img)
            # x.save()
            print(f'ALL {len(item)}DATA ADD SUCESSFULLY....')
        
        arcticles.append({
                'Title':title,
                'Descriptions':desc,
                # 'External-Link':external_link,
                'Image':img
            })
        # print(arcticles)
        # print(f"Image: {img}")
           
# Push The Data to DB
           

#For Downloading Images By Using Threading
        # def downloader(url):
        #     response = requests.get(url).content
        #     with open(f"Images/{str(uuid.uuid4()).split('-')[0]}.jpg", 'wb') as f:
        #         f.write(response)

        # if img != "No Image Available":
        #     start=time.time()
        #     p = threading.Thread(target=downloader, args=[img])
        #     p.start()
        #     p.join()  
        #     end=time.time()
        #     print(f"Total time taken: {end - start:.2f} seconds")
        
WebScraper()