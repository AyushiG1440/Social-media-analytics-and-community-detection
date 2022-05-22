# https://www.youtube.com/watch?v=8Bf6-KtrlIo&t=314s
#git clone --depth=1 https://github.com/twintproject/twint.git
#cd twint
#pip3 install . -r requirements.txt
# pip install --upgrade aiohttp && pip install --force-reinstall aiohttp-socks
import twint

#configuration
config = twint.Config()
config.Search = "bitcoin"   #search word
config.Limit = 10000 #number of tweets to query
config.Store_json = True
#config.Store_csv = True

config.Output = "Tweet data json"
#running search
twint.run.Search(config)

#{"id": 1527615131785510913, "conversation_id": "1527615131785510913", "created_at": "2022-05-20 17:10:03 India Standard Time", "date": "2022-05-20", "time": "17:10:03", "timezone": "+0530", "user_id": 1284031149657001985, "username": "1stpremiumcow", "name": "impressed", "place": "", "tweet": "Can handle upto 8million order per second why not start trading with @fibitpro  #cryptotrading #cryptocurrency #cryptocurrencies #Bitcoin #Litecoin #BNB  https://t.co/xIkCqQjglF", "language": "en", "mentions": [{"screen_name": "fibitpro", "name": "fibitpro exchange", "id": "1413034762428583936"}], "urls": [], "photos": ["https://pbs.twimg.com/media/FTMt24wWQAAegoA.jpg"], "replies_count": 0, "retweets_count": 0, "likes_count": 0, "hashtags": ["cryptotrading", "cryptocurrency", "cryptocurrencies", "bitcoin", "litecoin", "bnb"], "cashtags": [], "link": "https://twitter.com/1stpremiumcow/status/1527615131785510913", "retweet": false, "quote_url": "", "video": 1, "thumbnail": "https://pbs.twimg.com/media/FTMt24wWQAAegoA.jpg", "near": "", "geo": "", "source": "", "user_rt_id": "", "user_rt": "", "retweet_id": "", "reply_to": [], "retweet_date": "", "translate": "", "trans_src": "", "trans_dest": ""}
