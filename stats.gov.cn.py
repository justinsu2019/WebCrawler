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
        
        li = item.find_all("li",{"class":""})

        for i in li:
            url = i.a.attrs["href"]
            time = (i.find("font", {"class": "cont_tit02"}) is not None and i.find("font", {"class": "cont_tit02"}).string)
            title = i.font.string
            print("{} Title: {}, url is: {} \n".format(time, title, url))
            stats_gov.append("{} Title: {}, url is: {} \n".format(time, title, url))
 
        f = open('stats.gov.txt','a')
        for s in stats_gov:
            (("False" not in str(s)) and f.write(str(s)+"\n"))
        f.close()
 
