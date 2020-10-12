import requests
import api
import tweepy
import TwitterSearch
from twython import Twython
Username = {'Username': 'hfeitosa@grupoea.com.br'}
url = 'http://tweeps.locaweb.com.br/tweeps'
r = requests.get(url, headers=Username)
r.status_code


auth=tweepy.OAuthHandler('kbxw7zE8By1oIJFG6iBWiKhPf','9Zu1oLjNxqKcsSpkNEuVnUNOjpm3NoVoWiaRosGAd2McoGpknq')
auth.set_access_token('1153146166080614401-rbJxDrJGZWaQ3cso2JUleCJvHTMnCY'
                      ,'FvysFf4mOUxr152OIImNkpOMKPn6UHl4IpnmKWD4s839B')

api = tweepy.API(auth)#para autorizar a api

query_search= "Locaweb"  + " -filter:retweets"#usado para buscar mais o filtro que deseja

cursor_tweets = tweepy.Cursor(api.search,
            q=query_search,result_type='mixed').items(10)#o tanto de tweets que quer buscar

tweet = cursor_tweets#variavel

tweets_dict = {}#entrada para chaves

def most_relevants():
    query_search= "Locaweb"

    cursor_tweets = tweepy.Cursor(api.search,
                q=query_search,result_type='popular').items(15)#numero maior de busca

    for tweet in cursor_tweets:#chave para o texto
        print('proximo user','\n')
        print('followers_count : ',tweet.user.followers_count)
        print('screen_name : ',tweet.user.name)
        print('profile_link : ',tweet.user.url)
        print('created_at : ',tweet.created_at)
        print('link : "https://twitter.com/{}/status{}"'.format(tweet.user.name,tweet.id_str))
        print('retweet_count : ',tweet.retweet_count)
        print('text = ',tweet.text)
        print('favorite_counts : ',tweet.user.favourites_count)

def most_mentions ():
    query_search = "Locaweb" + " -filter:retweets" + '\n'  # busca

    cursor_tweets = tweepy.Cursor(api.search,
                                  q=query_search, ).items(15)  # numero maior de busca

    for tweet in cursor_tweets:  # chave para o texto
        print('proximo user', '\n')
        print('screen_name : ', tweet.user.name)
        print('profile_link : ', tweet.user.url)
        print('created_at : ', tweet.created_at)
        print('favorite_counts : ', tweet.user.favourites_count)
        print('followers_count : ', tweet.user.followers_count)
        print('text = ', tweet.text)
        print('link : "https://twitter.com/{}/status{}"'.format(tweet.user.name, tweet.id_str))
        print('retweet_count : ', tweet.retweet_count)

print('\most_relevants\n\most_mentions')
es = input('Escolha qual quer acessar: ')
if es == most_relevants:
    print(most_relevants)
if es == most_mentions():
    print(most_mentions())