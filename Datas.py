import tweepy
from textblob import TextBlob

# Inserisci qui le tue credenziali API di Twitter
api_key = "your key"
api_secret_key = "your_secret_key"
bearer_token = "your_brearer_token"
access_token = "your_access_token"
access_token_secret = "your access_token_secret"
api = tweepy.Client(bearer_token,api_key,api_secret_key,access_token,access_token_secret,wait_on_rate_limit=True)


# Funzione per raccogliere i tweet
def get_tweets(query):
    # Raccogli i tweet recenti (fino a 7 giorni fa)
    tweets = api.search_recent_tweets(query=query,max_results=10)
    return tweets

# Funzione per analizzare il sentiment
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet.full_text)
    if analysis.sentiment.polarity > 0:
        return 'positivo'
    elif analysis.sentiment.polarity < 0:
        return 'negativo'
    else:
        return 'neutrale'

query = "sostenibilità"
tweets = get_tweets(query)

for tweet in tweets:
    print (tweet)
    a = tweet.get()
    sentiment = analyze_sentiment(tweet)
    print(f"Tweet: {tweet.full_text}")
    print(f"Sentiment: {sentiment}\n")
