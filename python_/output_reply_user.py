# from twitter import Twitter, OAuth

#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

from requests_oauthlib import OAuth1Session
import json
import csv

### Functions                                                                                                                                                     
def main():
    print ('consumer_key: ')
    consumer_key = input('>>>  ')
    print ('consumer_secret: ')
    consumer_secret = input('>>>  ')
    print ('access_token: ')
    access_token = input('>>>  ')
    print ('access_token_secret: ')
    access_token_secret = input('>>>  ')

    oath_key_dict = {
        "consumer_key": consumer_key,
        "consumer_secret": consumer_secret,
        "access_token": access_token,
        "access_token_secret": access_token_secret
    }

    print ('target tweet author: ')
    author = input('>>> @')
    print ('target tweet id: ')
    id_str = input('>>>  ')
    
    tweets = tweet_search(f'@{author}', oath_key_dict, id_str)
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
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath

def tweet_search(search_word, oath_key_dict, id_str):
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