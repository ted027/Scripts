# from twitter import Twitter, OAuth

#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

from requests_oauthlib import OAuth1Session
import json
import csv

### Constants                                                                                                                                                     
oath_key_dict = {
    "consumer_key": "D05pRMHJrHoP4Vy2YXsCxa0r5",
    "consumer_secret": "XF0fp4MBnKncVFIkEIQXwFDSC9h5xAVtaHlKV1wugxEqaIEmr5",
    "access_token": "945419135697108992-UocgJBz2zeEC1onPwC5PQzUW6LujigD",
    "access_token_secret": "ejgD6xj4svxAZuiDA0TneBO9uKReXX4rCtoBow08VO7Pw"
}


### Functions                                                                                                                                                     
def main():
    print ('consumer_key: ')
    consumer_key = raw_input('>>>  ')
    print ('consumer_secret: ')
    consumer_secret = raw_input('>>>  ')
    print ('access_token: ')
    access_token = raw_input('>>>  ')
    print ('access_token_secret: ')
    access_token_secret = raw_input('>>>  ')

    print ('target tweet author: ')
    author = raw_input('>>> @')
    print ('target tweet id: ')
    id_str = raw_input('>>>  ')
    
    tweets = tweet_search(f'@{author}', oath_key_dict)
    f = open('output.csv', 'wb')
    writer = csv.writer(f, lineterminator=',')
    for tweet in tweets["statuses"]:
        if(tweet[u'in_reply_to_status_id_str']==id_str):
            text = tweet['text'].encode('cp932', 'ignore')
            created_at = tweet[u'created_at']
            screen_name = tweet[u'user'][u'screen_name']
            csvlist = []
            csvlist.append(created_at)        
            csvlist.append(screen_name)
            csvlist.append(text)
            csvlist.append('\n')
            writer.writerow(csvlist)
    f.close()
    return


def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )
    return oath

def tweet_search(search_word, oath_key_dict):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word,
        "result_type": "recent",
        "count": "100",
        "since_id": id_str,
        "max_id": "TODO"
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params=params)
    if responce.status_code != 200:
        print(responce.status_code)
        return None
    tweets = json.loads(responce.text)
    return tweets

### Execute                                                                                                                                                       
if __name__ == "__main__":
    main()