import copy
import requests
import bs4
import json

YEAR = 2019

thought = {
    "トレード": {
        "頻度": "おまかせ"
    },
    "新外国人獲得": {
        "頻度": "おまかせ",
        "獲得方針": "おまかせ"
    },
    "ドラフト": {
        "獲得方針": "おまかせ"
    },
    "FA交渉": {
        "他チームの選手に対して": "おまかせ",
        "獲得方針": "おまかせ",
        "人数": "おまかせ"
    },
    "ポスティング": {
        "承認": "おまかせ",
        "獲得方針": "おまかせ"
    },
    "自由契約選手獲得": {
        "獲得方針": "おまかせ"
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

thought_list = []

result = {}
for team in teams:
    result[team] = copy.deepcopy(thought)


def __conv_team_notate(team):
    return team.replace("広島東洋", "広島") \
                .replace("東京ヤクルト", "ヤクルト") \
                .replace("巨人", "読売") \
                .replace("横浜ＤｅＮＡ", "ＤｅＮＡ") \
                .replace("横浜DeNA", "ＤｅＮＡ") \
                .replace("DeNA", "ＤｅＮＡ") \
                .replace("埼玉西武", "西武") \
                .replace("福岡ソフトバンク", "ソフトバンク") \
                .replace("北海道日本ハム", "日本ハム") \
                .replace("千葉ロッテ", "ロッテ") \
                .replace("東北楽天", "楽天")


def __create_team_dic(teams, default):
    team_dic = {}
    for team in teams:
        team_dic[team] = default
    return team_dic

def ___chage_typical_teams_num(sorted_tuple_list):
    lead_num = follow_num = 3
    while 0 < lead_num:
        if sorted_tuple_list[lead_num-1][1] != sorted_tuple_list[lead_num][1]:
            break
        lead_num -= 1
    while 0 < follow_num:
        if sorted_tuple_list[12-follow_num][1] != sorted_tuple_list[12-follow_num-1][1]:
            break
        follow_num -= 1
    return lead_num,follow_num
        

def __sort_team_dic(team_dic):
    sorted_tuple_list = sorted(team_dic.items(), key=lambda x: -x[1])
    print(f"  {sorted_tuple_list}\n")
    lead_num,follow_num = ___chage_typical_teams_num(sorted_tuple_list)
    leader = [team_tuple[0] for team_tuple in sorted_tuple_list[:lead_num]]
    follower = [team_tuple[0] for team_tuple in sorted_tuple_list[12-follow_num:]]
    return leader,follower

def __update_result(result, update_items, leader, follower):
    """
    Parameters
    ----------
    update_items : list
        thoughtの親key, thoughtの小key, leaderのvalue, followerのvalue
        ex. ["トレード", "頻度", "積極的", "消極的"]
    """
    for lead_team in leader:
        result[lead_team][update_items[0]][update_items[1]] = update_items[2]
    for follow_team in follower:
        result[follow_team][update_items[0]][update_items[1]] = update_items[3]
    return result

def _trade_dic(teams):
    team_dic = __create_team_dic(teams, 0)
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
                team_dic[__conv_team_notate(team_td.text)] += 1
    return team_dic

def trade(teams, result):
    team_dic = _trade_dic(teams)
    print("trade:  ")
    leader,follower = __sort_team_dic(team_dic)
    update_items = ["トレード", "頻度", "積極的", "消極的"]
    return __update_result(result, update_items, leader, follower)

result = trade(teams, result)
print(result)

def _draft_dic():
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
