import requests
import lxml.html as html

from lib.config import DataConfig as dc

def get_anime():
  try:
    request = requests.get(dc.URL.value)
    
    if request.status_code == 200:
      body = request.content.decode("utf-8")
      parsed = html.fromstring(body)
      animes = parsed.xpath(dc.XPATH_EPISODE.value)
      print(animes)
    else:
      raise ValueError

  except ValueError as err:
    print(err)