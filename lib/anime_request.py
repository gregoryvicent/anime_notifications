import requests
import lxml.html as html

from lib.config import DataConfig as dc
from lib.send_email import email
from lib.db_conn import HandleDB

def get_anime():
  try:
    request = requests.get(dc.URL.value)
    email_db = HandleDB()
    
    if request.status_code == 200:
      body = request.content.decode("utf-8")
      parsed = html.fromstring(body)
      animes = parsed.xpath(dc.XPATH_EPISODE.value)
      print("Animes List: %s" % animes)
      if animes:
        if not email_db.get_data():
          email(animes[0])
          email_db.update_data(1)
          print("------------ Send new cap ")
        else:
          print("------------ Email already ")
      else:
        print("------------ No new cap ")
        email_db.update_data(0)
    else:
      raise ValueError


  except ValueError as err:
    print(err)
