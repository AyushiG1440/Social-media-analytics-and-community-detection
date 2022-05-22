import json
#import heatmap
import networkx as net
import matplotlib.pyplot as plot
import csv

file = 'C:/Python Codes/FYP/Tweet data json/tweets.json'
i = open(file,'rb')
#i = i.replace("}   ", '},')
retweets=net.DiGraph()
#hashtag_net=net.Graph()
node_list = []
#node_name = []
edge_list = []
with open('node.csv', 'w', newline='') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(['ID','Name'])    
with open('edge.csv', 'w', newline='') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(['Source','Target'])
#{"id": 1527615131785510913, "conversation_id": "1527615131785510913", "created_at": "2022-05-20 17:10:03 India Standard Time", "date": "2022-05-20", "time": "17:10:03", "timezone": "+0530", "user_id": 1284031149657001985, "username": "1stpremiumcow", "name": "impressed", "place": "", "tweet": "Can handle upto 8million order per second why not start trading with @fibitpro  #cryptotrading #cryptocurrency #cryptocurrencies #Bitcoin #Litecoin #BNB  https://t.co/xIkCqQjglF", "language": "en", "mentions": [{"screen_name": "fibitpro", "name": "fibitpro exchange", "id": "1413034762428583936"}], "urls": [], "photos": ["https://pbs.twimg.com/media/FTMt24wWQAAegoA.jpg"], "replies_count": 0, "retweets_count": 0, "likes_count": 0, "hashtags": ["cryptotrading", "cryptocurrency", "cryptocurrencies", "bitcoin", "litecoin", "bnb"], "cashtags": [], "link": "https://twitter.com/1stpremiumcow/status/1527615131785510913", "retweet": false, "quote_url": "", "video": 1, "thumbnail": "https://pbs.twimg.com/media/FTMt24wWQAAegoA.jpg", "near": "", "geo": "", "source": "", "user_rt_id": "", "user_rt": "", "retweet_id": "", "reply_to": [], "retweet_date": "", "translate": "", "trans_src": "", "trans_dest": ""}

for tweet in i:
    js = json.loads(tweet)
    
    ### process tweet to extract information
    try:
        author = js['username']
        mentions = js['mentions']
        replied = js['reply_to']
        #hashtags=js['hashtags']
        
        if(node_list.count(js['user_id'])<1):
            node_list.append([js['user_id'],author])
            #node_name.append(author)
    
        for rt in mentions:
            alter=rt['screen_name']
            if(node_list.count(rt['id'])<1):
                node_list.append([rt['id'],alter])
                #node_name.append(alter)
            
            if retweets.has_edge(author,alter):
                retweets[author][alter]['weight']+=1
            else:
                retweets.add_edge(author,alter,weight=1)
                edge_list.append([js['user_id'],rt['id']])
        for rpy in replied:
            alter_2=rpy['screen_name']
            if(node_list.count(rpy['id'])<1):
                node_list.append([rpy['id'],alter_2])
                #node_name.append(alter_2)
            
            if retweets.has_edge(author,alter_2):
                retweets[author][alter_2]['weight']+=1
            else:
                retweets.add_edge(author,alter_2,weight=1)
                edge_list.append([js['user_id'],rpy['id']])
#        tags=[tag['text'].lower() for tag in hashtags]
#        for t1 in tags:
#            for t2 in tags:
#                if t1 is not t2:
#                    add_or_inc_edge(hashtag_net,t1,t2)      
    except KeyError:
        print ('key error')
        continue

#len(retweets)
with open('node.csv', 'w', newline='') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerows(node_list)
    
with open('edge.csv', 'w', newline='') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerows(edge_list)
#net.draw(retweets)
#undir_retweets=retweets.to_undirected()
#comps=net.connected_component_subgraphs(undir_retweets)
#len(comps)
#len(comps[0])
#net.draw(comps[0])

#degrees=net.degree(comps[0])

#degrees=sorted_degree(comps[0])
#degrees[:10] 

#plot.hist(net.degree(comps[0]).values(),50)

#core=trim_degrees(comps[0])

#len(core)
#len(hashtag_net)
#net.draw(hashtag_net)

#core=net.connected_component_subgraphs(hashtag_net)[0]
#net.draw(core)

#core.remove_node('earthquake')
#core2=trim_edges(hashtag_net, weight=2)
#net.draw(core2)

#core3=trim_edges(hashtag_net, weight=10)
#net.draw(core3)
