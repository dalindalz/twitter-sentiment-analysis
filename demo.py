import tweepy
from  textblob import TextBlob
import csv
from urlextract import URLExtract

consumer_key = "pysgg8ilW7KDmT0J3BrwXgHhB"
consumer_secret_key = "rCsF0eVDz0dHk3uQHnCywNzBy4k4LGXgJB26n8GWro34jbC8oO"

access_token = "2876133079-lTGTegSWROEeQivKXMh8V4Wl8Vezesu1tSjWGS4"
access_token_secret = "0VlSbDzpNaXrYLyib24hihLpRrSyWJe12Vh7yz4oHZU52"


auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweet = api.search('trump')

with open("twitter.csv",'w',newline= '') as output:

    # create var
    fileOut = csv.writer(output)
    data = ['Tweets', 'Polarity', 'Subjectivity', 'URL']
    fileOut.writerow(data)

    for tweet in public_tweet:
        analysis = TextBlob(tweet.text)
        polarityInt = analysis.sentiment.polarity
        subjectivityInt = analysis.sentiment.subjectivity

        if polarityInt > 0.0:
            polarityStr = 'Positive'
        else: polarityStr = 'Negative'

        if subjectivityInt > 0.5:
            subjectivityStr = 'Subjective'
        else: subjectivityStr = 'Objective'

        url = None
        words = tweet.text.split()
        link = URLExtract()
        urls = link.find_urls(tweet.text)
        for word in words:
            if 'http' in word:
                url = word

        fileOut.writerow([tweet.text, polarityStr, subjectivityStr, url])
        print(tweet.text)
        print('Polarity: ', polarityInt)
        print('Subjectivity:', subjectivityInt)

