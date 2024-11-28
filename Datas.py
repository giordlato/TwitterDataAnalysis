import tweepy
from textblob import TextBlob

# Inserisci qui le tue credenziali API di Twitter
api_key = "iFqgZaEjCf9PzwItk9rmXdoEN"
api_secret_key = "0g1bC5fXjFQ32VLprX5QYDos56Cz9jxMFKpcUfofNtuxeFQyMm"
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAOvwxAEAAAAAXDAbk%2BKc7JRu5UbUbkf%2BtHHNd4Q%3D7ewc8HdJAiUuaPNYdLO50bqmPaN8UjrKeOjiZ0UzNc7hsjuz0Z'
access_token = "1478756256739479562-MWrpRcG5Fcpi9uUdN3KYFIUn3vCdw0"
access_token_secret = "jrpVJzswBN8aCoxBHkTEY0tlxlcqYgFzlV134enKqHdez"
api = tweepy.Client(bearer_token,api_key,api_secret_key,access_token,access_token_secret,wait_on_rate_limit=True)


# Funzione per raccogliere i tweet
def get_tweets(query, count=100):
    # Raccogli i tweet recenti (fino a 7 giorni fa)
    tweets = api.search_recent_tweets(query=query,max_results=10)
    return tweets

# Funzione per analizzare il sentiment
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet.full_text)
    # Restituisce 'positivo', 'negativo' o 'neutrale' in base al sentiment
    if analysis.sentiment.polarity > 0:
        return 'positivo'
    elif analysis.sentiment.polarity < 0:
        return 'negativo'
    else:
        return 'neutrale'

# Main: raccogli i tweet e analizza il sentiment
query = "sostenibilità"  # Modifica la query per cercare tweet su un argomento di tuo interesse
tweets = get_tweets(query)

for tweet in tweets:
    print (tweet)
    sentiment = analyze_sentiment(tweet)
    print(f"Tweet: {tweet.full_text}")
    print(f"Sentiment: {sentiment}\n")
