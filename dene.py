from stop_words import StopWords
import re
from bs4 import BeautifulSoup
import requests
get = requests.get(
    "https://www.ntv.com.tr/galeri/turkiye/sultangazide-tekstil-atolyesinde-yangin-alevler-bitisikteki-ayakkabi-imalathanesine-sicradi,MlP4womgY0G5e1T-bjnIlg/Q9_OXjLpFUOHIrU6ANGNew")


def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    [s.extract() for s in soup(['iframe', 'script'])]
    stripped_text = soup.get_text()
    stripped_text = re.sub(r'[\r|\n|\r\n]+', '\n', stripped_text)
    return stripped_text


clean_content = strip_html_tags(get.content)
print(clean_content)
