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
    "広島", "ヤクルト", "読売", "ＤｅＮＡ", "中日", "阪神", "西武", "ソフトバンク", "日本ハム", "オリックス",
    "ロッテ", "楽天"
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
        if sorted_tuple_list[lead_num -
                             1][1] != sorted_tuple_list[lead_num][1]:
            break
        lead_num -= 1
    while 0 < follow_num:
        if sorted_tuple_list[12 - follow_num][1] != sorted_tuple_list[
                12 - follow_num - 1][1]:
            break
        follow_num -= 1
    return lead_num, follow_num


def __sort_team_dic(team_dic):
    sorted_tuple_list = sorted(team_dic.items(), key=lambda x: -x[1])
    print(f"  {sorted_tuple_list}\n")
    lead_num, follow_num = ___chage_typical_teams_num(sorted_tuple_list)
    leader = [team_tuple[0] for team_tuple in sorted_tuple_list[:lead_num]]
    follower = [
        team_tuple[0] for team_tuple in sorted_tuple_list[12 - follow_num:]
    ]
    return leader, follower


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
    for year in [YEAR - 3, YEAR - 2, YEAR - 1, YEAR]:
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
    leader, follower = __sort_team_dic(team_dic)
    update_items = ["トレード", "頻度", "積極的", "消極的"]
    return __update_result(result, update_items, leader, follower)


def _foreign_dic(teams):
    f = open("../other/foreign_player.json", 'r')
    foreign_dic = json.load(f)

    num_of_people_dic = __create_team_dic(teams, 0)
    age_dic = __create_team_dic(teams, 0)
    for year in [YEAR - 2, YEAR - 1, YEAR]:
        for team in teams:
            foreign_list = foreign_dic[str(year)][team]
            for foreign in foreign_list:
                num_of_people_dic[team] += 1
                age_dic[team] += year - foreign["Born"]
    for team in teams:
        age_dic[team] = age_dic[team] * 1.0 / num_of_people_dic[team]
    return num_of_people_dic, age_dic


def foreign(teams, result):
    num_of_people_dic, age_dic = _foreign_dic(teams)
    print("foreign_player: ")
    num_leader, num_follower = __sort_team_dic(num_of_people_dic)
    num_update_items = ["新外国人獲得", "頻度", "積極的", "消極的"]
    result = __update_result(result, num_update_items, num_leader,
                             num_follower)
    age_leader, age_follower = __sort_team_dic(age_dic)
    age_update_items = ["新外国人獲得", "獲得方針", "ベテラン中心", "若手中心"]
    return __update_result(result, age_update_items, age_leader, age_follower)


def _draft_dic(teams):
    num_of_people_dic = __create_team_dic(teams, 0)
    age_dic = __create_team_dic(teams, 0)
    YY = YEAR % 1000
    for year in [YY - 2, YY - 1]:
        url = f"https://www.sanspo.com/baseball/draft/{year}/draft_table.html"

        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.content, "html.parser")
        trs = soup.find_all("tr")
        team_pointer = ""
        for tr in trs:
            tds = tr.find_all("td")
            if len(tds) < 5: continue
            td_top_text = __conv_team_notate(tds[0].text.replace("\u3000", ""))
            index_of_age_content = 4
            if td_top_text in teams:
                team_pointer = td_top_text
                index_of_age_content = 5
            num_of_people_dic[team_pointer] += 1
            age = int(tds[index_of_age_content].text)
            if not 16 < age < 45: raise BaseException()
            age_dic[team_pointer] += age
    for team in teams:
        age_dic[team] = age_dic[team] * 1.0 / num_of_people_dic[team]
    return age_dic


def draft(teams, result):
    team_dic = _draft_dic(teams)
    print("draft: ")
    leader, follower = __sort_team_dic(team_dic)
    update_items = ["ドラフト", "獲得方針", "即戦力重視", "将来性重視"]
    return __update_result(result, update_items, leader, follower)


def _free_agent_dic(teams):
    f = open("../other/free_agent_player.json", 'r')
    fa_dic = json.load(f)

    num_of_people_dic = __create_team_dic(teams, 0)
    age_dic = __create_team_dic(teams, 0)
    payment_dic = __create_team_dic(teams, 0)
    for year in [YEAR - 3, YEAR - 2, YEAR - 1]:
        for player in fa_dic.items():
            for team in player["Team"]:
                num_of_people_dic[team] += 1
                age_dic[team] += year - player["Born"]
                payment_dic += player["Payment"]
    for team in teams:
        age_dic[team] = age_dic[team] * 1.0 / num_of_people_dic[team]
        payment_dic[team] = payment_dic[team] * 1.0 / num_of_people_dic[team]
    return num_of_people_dic, age_dic, payment_dic


def free_agent(teams, result):
    num_of_people_dic, age_dic, payment_dic = _free_agent_dic(teams)
    print("free_agent_player: ")
    for k, v in num_of_people_dic.items():
        if v / 3 > 2:
            result[k]["FA交渉"]["人数"] = "複数人"
        elif v / 3 < 1:
            result[k]["FA交渉"]["人数"] = "一人"
    num_leader, num_follower = __sort_team_dic(num_of_people_dic)
    num_update_items = ["FA交渉", "他チームの選手に対して", "積極的", "消極的"]
    result = __update_result(result, num_update_items, num_leader,
                             num_follower)
    age_leader, age_follower = __sort_team_dic(age_dic)
    age_update_items = ["FA交渉", "獲得方針", "経験重視", "若さ重視"]
    result = __update_result(result, age_update_items, age_leader,
                             age_follower)
    pay_leader, pay_follower = __sort_team_dic(payment_dic)
    pay_update_items = ["FA交渉", "獲得方針", "目玉選手重視", "単独交渉重視"]
    return __update_result(result, pay_update_items, pay_leader, pay_follower)


result = trade(teams, result)
result = draft(teams, result)
result = foreign(teams, result)
print(result)


def _returned_dic(teams):
    f = open("../other/returned_player.json", 'r')
    returned_dic = json.load(f)

    team_dic = {}
    return team_dic


def returned(teams, result):
    team_dic = _returned_dic(teams)
    print("returned_player: ")
    leader, follower = __sort_team_dic(team_dic)
    update_items = ["ポスティング", "獲得方針", "積極的", "消極的"]
    return __update_result(result, update_items, leader, follower)


def _unregistered_dic(teams):
    f = open("../other/unregistered_player.json", 'r')
    unregistered_dic = json.load(f)

    num_of_people_dic = __create_team_dic(teams, 0)
    age_dic = __create_team_dic(teams, 0)
    for year in [YEAR - 2, YEAR - 1, YEAR]:
        for team in teams:
            unregistered_list = unregistered_dic[str(year)][team]
            for unregistered in unregistered_list:
                num_of_people_dic[team] += 1
                age_dic[team] += year - unregistered["Born"]
    for team in teams:
        age_dic[team] = age_dic[team] * 1.0 / num_of_people_dic[team]
    return age_dic


def unregistered(teams, result):
    age_dic = _unregistered_dic(teams)
    print("unregistered_player: ")
    leader, follower = __sort_team_dic(age_dic)
    update_items = ["自由契約選手獲得", "獲得方針", "経験重視", "のびしろ重視"]
    return __update_result(result, update_items, leader, follower)