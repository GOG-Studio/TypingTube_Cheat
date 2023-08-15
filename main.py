print("main.py [URL]")

import pyautogui
from sys import argv
from platform import system
from selenium import webdriver

#OS取得
os = system()
#OSごとにブラウザを自動選択する
def os_f():
    global driver
    if os == "Windows":
        driver = webdriver.Chrome()
    elif os == "Darwin":
        driver = webdriver.Firefox()
    elif os == "Linux":
        driver = webdriver.Safari()
    else:
        print("Not Supported Device")

#コマンドプロンプト引数からURL取得、できなければinput
def get_url():
    global url
    try:
        url = argv[1]
    except:
        url = input("Enter TypingTube URL:")

#入力場所を探す
def type_area():
    global area
    area = driver.find_element("id" , "main_content")

#歌詞を探す
def find_rylics():
    global rylics
    rylics = ""
    try:
        rylics1 = driver.find_element("id" , "first-color-roma")
        rylics2 = driver.find_element("id" , "typing-word-roma")
    except:
        pass
    try:
        if rylics == rylics1.text + rylics2.text:
            pass
        else:
            rylics = rylics1.text + rylics2.text
            print(rylics)
    except:
        pass
#歌詞を入力する
def typing():
    try:
        pyautogui.write(rylics)
    except:
        pass

###処理実行###

#URL取得
get_url()

#OSごとにドライバーを選択する
os_f()

#サイトを開く
driver.get(url)

#入力場所を設定
type_area()

#歌詞を探す
#歌詞を入力する
while True:
    find_rylics()
    typing()
    
