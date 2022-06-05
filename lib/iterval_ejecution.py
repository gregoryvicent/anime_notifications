import threading
import time

from lib.anime_request import get_anime


def timer():
    while True:
        get_anime()
        time.sleep(345600)


t = threading.Thread(target=timer)
t.start()
