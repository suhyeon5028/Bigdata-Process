from unittest import result
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def num_to_aid(num):
    num_str = str(num)
    return num_str.zfill(10)

# dependency -> num_to_aid(int:num)
def naver_craw(aid):
    result = {"title":"", "company":"국민일보", "createdAt":datetime.now()}

    response = requests.get(
        f"https://n.news.naver.com/mnews/article/005/{num_to_aid(num)}?sid=100"
    )

    html = response.text
    html_bs = BeautifulSoup(html, "html.parser")

    title = html_bs.select(".end_tit")[0].get_text().strip()

    result["title"] = title

    return result

aid = num_to_aid(1)
result = naver_craw(aid)
print(result)