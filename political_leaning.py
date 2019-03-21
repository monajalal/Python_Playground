import pandas as pd
from urllib.parse import urlsplit

#df = pd.read_csv("/Users/mona/Downloads/finalized_gv_ih_master_updated.csv")

#political_df = pd.read_csv("/Users/mona/Downloads/news-sites_political-leaning.csv")
df = pd.read_csv("/Users/mona/Downloads/CH-guns_filtered.csv")
#df = pd.read_csv("/Users/mona/Downloads/CH-guns_all.csv")
theme_df = pd.read_csv("/Users/mona/Downloads/CH-guns_frames_all.csv")

#go == abc
news_media = {'breitbart':0, 'dailycaller':0 , 'drudgereport':0,
              'foxnews':0 , 'newsmax':0 , 'theblaze':0 , 'buzzfeednews':0 ,
              'dailykos':0 , 'huffingtonpost':0 , 'motherjones':0,
              'msnbc':0, 'slate':0, 'theatlantic':0 ,'vox':0, 'go':0, 'cbsnews':0,
              'chicagotribune':0, 'cnn':0, 'latimes':0, 'nbcnews':0,
              'nytimes':0, 'newsweek':0, 'npr':0, 'pbs':0, 'politico':0,
              'thehill':0, 'usatoday':0, 'wsj':0, 'washingtonpost':0, 'yahoo':0}


print(list(df.columns.values))

print(len(news_media))
print(df.shape[0])
print(theme_df.shape[0])

count = 0
for i in range(theme_df.shape[0]):
    if theme_df.iloc[i]['Sentence/Title'] in df['Post Title'].values:
        #url = df.loc[df['Post Title'] == theme_df.iloc[i]['Sentence/Title']]['URL']
        #print(theme_df.iloc[i]['Sentence/Title'])
        count += 1

#for i in range(df.shape[0]):
#    if df.iloc[i]['Post Title']  in theme_df['Sentence/Title'].values:
#        print(df.iloc[i]['Post Title'])
#    domain = urlsplit(df.iloc[i]['URL']).netloc.split('.')[-2]
    '''count = 0
    for key in news_media.keys():
        if key not in domain:
            count += 1
    if count == 30:
        print(domain, df.iloc[i]['GUID'])'''

#    if domain in news_media.keys():
#        news_media[domain] += 1


    #print(df.iloc[i]['ID'], urlsplit(df.iloc[i]['news_URL']).netloc.split('.')[-2])

#print(news_media)