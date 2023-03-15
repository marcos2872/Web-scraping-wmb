import requests
from parsel import Selector
import json


url = "https://branham.org/pt/MessageAudio"


def fetch(url):
  try:
    response = requests.get(url, headers={"user-agent": "Fake user-agent"})
    return response.text
  except (requests.HTTPError, requests.ReadTimeout):
    print(requests.HTTPError, requests.ReadTimeout)
    return None


def listMessage(html):
  selector = Selector(html)
  messages = selector.css("div.messagebox").getall()
  list = []
  for curr in messages:
    div = Selector(curr)
    list.append({
      "title": div.css("span.prodtexttitle::text").get(),
      "datails": div.css("span.show-for-small-down::text").get(),
      "audio": div.css("a[title='Download Audio']::attr(href)").get() or '',
      "pdf": div.css("a[title='download PDF file']::attr(href)").get()
    })
  print(list)
  return list


def writeJson(list):
  with open('sermons.json', 'w', encoding='utf-8') as file:
    json.dump(list, file, ensure_ascii=False)


writeJson(listMessage(fetch(url)))
