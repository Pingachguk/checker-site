import requests
import bs4
import copy
import pandas as pd
import time


url = "https://klimatprof.online/"
uri = "https://klimatprof.online"
urls = {url: False}

session = requests.Session()
count = 0

def get_sitemap(links):
    global count

    for link, is_visited in links.items():
        if is_visited:
            continue
        # print(link)
        # print(len(urls.keys()))
        page = session.get(link).text
        urls[link] = True
        soup = bs4.BeautifulSoup(page, "html.parser")
        all_link_page = soup.find_all("a")

        for a in all_link_page:
            try:
                if not (a["href"] in urls.keys()):
                    # print(a["href"])
                    if a["href"].find("youtube.com") != -1 and a["href"].find("#") != -1 or a["href"].find(":")!=-1:
                        continue
                    elif a["href"].find(url) != -1:
                        urls[a["href"]] = False
                        count += 1
                    else:
                        urls[uri+a["href"]] = False
                        count += 1
                    if count == 10:
                        df = pd.DataFrame(urls.keys(), columns=["url"])
                        df.to_csv("urls.csv", index=False)
                        # print("Sleep")
                        # time.sleep(1)
                        count = 0
            except Exception as e:
                print(e)

                
while True:
    links = copy.deepcopy(urls) 
    print(len(links))
    # print(len(urls.keys()))
    get_sitemap(links)

