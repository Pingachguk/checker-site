import pandas as pd 
import requests
import bs4

from datetime import datetime


session = requests.Session()

def main():
    data = pd.read_csv("urls.csv")
    count = 0

    for url in data.values:
        begin = datetime.now().timestamp()
        print(url[0])
        page = bs4.BeautifulSoup(session.get(url[0]).text, "html.parser")
        try:
            if page.find(itemprop="offers").find(itemprop="price") and page.find(itemprop="offers").find(title="Авторизуйтесь, чтобы совершать покупки"):
                data = data.append({"URL": url[0]})
                data.to_csv("products_url.csv", index=False)
                count += 1
                print(f"[+] Add {count}")
        except:
            pass
        end = datetime.now().timestamp()

        print("[*] Duration: %.2f s" % (end-begin))

if __name__ == "__main__":
    main()
