import urllib.request as req
import bs4

# Mac才需要
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def get_data(URL:str, option:str):
    request = req.Request(URL, headers={
        "User-Agent" :
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
        }
    )

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")


    root = bs4.BeautifulSoup(data, "html.parser")

    if option=="title":
        titles = root.find_all("div", class_="title")

        for title in titles:
            if title.a!=None:
                print(title.a.string)
                text_url = "http://www.ptt.cc" + title.a["href"]
                get_data(text_url, "content")

        return

    elif option=="content":
        cont_ = root.find("meta", attrs={"name":"description"}).attrs["content"]

        print("摘要：")
        print(cont_+"\n")

        return            


# 起始網址
url = "https://www.ptt.cc/bbs/NBA/index.html"
get_data(url, "title")
