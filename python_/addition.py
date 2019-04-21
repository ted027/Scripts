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
    "ＤｅＮＡ",
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


def conv_team_notate(team):
    return team.replace("広島東洋", "広島") \
                .replace("東京ヤクルト", "ヤクルト") \
                .replace("巨人", "読売") \
                .replace("横浜ＤｅＮＡ", "ＤｅＮＡ") \
                .replace("横浜DeNA", "ＤｅＮＡ") \
                .replace("DeNA", "ＤｅＮＡ") \
                .replace("埼玉西武", "西武") \
                .replace("福岡ソフトバンク", "ソフトバンク") \
                .replace("北海道日本ハム", "日本ハム") \
                .replace("千葉ロッテ", "ロッテ").replace("東北楽天", "楽天")


def _create_team_dic(teams, default):
    team_dic = {}
    for team in teams:
        team_dic[team] = default
    return team_dic

def _sort_team_dic(team_dic):
    sorted_tuple_list = sorted(team_dic.items(), key=lambda x: -x[1])
    print(sorted_tuple_list)
    # if team3 == team4
    leader = [team_tuple[0] for team_tuple in sorted_tuple_list[:3]]
    follower = [team_tuple[0] for team_tuple in sorted_tuple_list[9:]]
    return leader,follower

def _update_result(result, leader, lead_word, follower, follow_word):
    # continue
    pass

def trade_dic(teams):
    team_dic = _create_team_dic(teams, 0)
    for year in [YEAR-3, YEAR-2, YEAR-1, YEAR]:
        url = f"http://npb.jp/announcement/{year}/pn_traded.html"

        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.content, "html.parser")
        tables = soup.find_all(class_="table_normal_noborder")

        for table in tables:
            if (table.find(class_="note")):
                continue
            team_tds = table.find_all(class_="trteam")
            for team_td in team_tds:
                team_dic[conv_team_notate(team_td.text)] += 1
    return team_dic

def trade(teams, result):
    team_dic = trade_dic(teams)
    leader,follower = _sort_team_dic(team_dic)


def draft():
    YY = YEAR & 1000
    for year in [YY-2, YY-1]:
        url = f"https://www.sanspo.com/baseball/draft/{year}/top.html"

        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.content, "html.parser")


def unregisterd_player():
    for year in [YEAR-3, YEAR-2, YEAR-1]:
        url = f"http://npb.jp/announcement/{year}/pn_released.html"

        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.content, "html.parser")
