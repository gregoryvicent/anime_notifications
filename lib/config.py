from enum import Enum

class DataConfig(Enum):
  XPATH_EPISODE = "//ul[@class='episodes list-unstyled row']//article[@class='episode']//h3[@class='title' and contains(text(), 'Kawaii dake ja Nai Shikimori-san')]/text()"
  URL = "https://tioanime.com/"
