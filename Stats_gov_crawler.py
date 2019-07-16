import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    resp = requests.get("http://www.stats.gov.cn/tjsj/zxfb/")
    # print(resp.content)
    soup = BeautifulSoup(resp.content)
    items = soup.find_all("div", {"class": "center_list"})

    #print(items)
    stats_gov = []
    
    for item in items:
        title_div = item.find("ul", {"class": "center_list_contlist"})
        li = item.find_all("font")
        for i in li:
            title = (i.attrs == {'class': ['cont_tit03']} and i.string)
            time = (i.attrs == {'class': ['cont_tit02']} and i.string)
            stats_gov.append((title and ("title is ", title) or ("time is", time)))
            print((title and ("title is ", title) or ("time is", time)))

    f = open('stats.gov.txt','a')
    for s in stats_gov:
        f.write(str(s)+"\n")
    f.close()
