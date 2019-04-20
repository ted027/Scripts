import requests
import bs4
import json

YEAR = 2019

thought = {
    "トレード": {
        "頻度": ""
    },
    "新外国人獲得": {
        "頻度": "",
        "獲得方針": ""
    },
    "ドラフト": {
        "獲得方針": ""
    },
    "FA交渉": {
        "他チームの選手に対して": "",
        "獲得方針": "",
        "人数": ""
    },
    "自由契約選手獲得": {
        "獲得方針": ""
    }
}

teams = [
    "広島",
    "ヤクルト",
    "読売",
    "DeNA",
    "中日",
    "阪神",
    "西武",
    "ソフトバンク",
    "日本ハム",
    "オリックス",
    "ロッテ",
    "楽天"
]

result = {}
for team in teams:
    result[team] = thought

def trade():
    for year in [str(YEAR-3), str(YEAR-2), str(YEAR-1), str(YEAR)]:
        url = f"http://npb.jp/announcement/{year}/pn_traded.html"

        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.content, "html.parser")


def draft():
    YY = YEAR & 1000
    for year in [str(YY-2), str(YY-1)]:
        url = f"https://www.sanspo.com/baseball/draft/{year}/top.html"

        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.content, "html.parser")


def unregisterd_player():
    for year in [str(YEAR-3), str(YEAR-2), str(YEAR-1)]:
        url = f"http://npb.jp/announcement/{year}/pn_released.html"

        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.content, "html.parser")
