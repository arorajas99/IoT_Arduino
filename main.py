import datetime, time

from pyfirmata import Arduino, util, STRING_DATA

port = 'COM4'
board = Arduino(port)


def current_time():
    while True:
        # time.sleep()
        a = datetime.datetime.now().strftime('%I: %M: %S')


        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(get_price(url)))

def live_price():
    while True:
        pass


def get_price(url):
    from bs4 import BeautifulSoup as BS
    import requests
    data = requests.get(url)
    soup = BS(data.text, 'html.parser')
    ans = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
    return ans


url = "https://www.google.com/search?q=nifty+50+price"

ans = get_price(url)


print(ans)


current_time()

