import threading
import time

from lib.anime_request import get_anime


def timer():
  while True:
    get_anime()
    time.sleep(3)


t = threading.Thread(target=timer)

t.start()
