import io
import json
import nltk
import twitter


CONSUMER_KEY = 'Input Your Consumer Key'
CONSUMER_SECRET= 'Input Your Consumer Secret Key'
OAUTH_TOKEN = 'Input Your OAUTH Token'
OAUTH_TOKEN_SECRET = 'Input Your OAUTH Token Secret'



QUERY = 'india'



OUT_FILE = QUERY + ".json"

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = twitter.TwitterStream(auth=auth)


print 'Filtering the public timeline for "{0}"'.format(QUERY)


stream = twitter_stream.statuses.filter(track=QUERY)

# Write one tweet per line as a JSON document.

with io.open(OUT_FILE, 'w', encoding='utf-8', buffering=1) as f:
    for tweet in stream:
        f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
        print tweet['text']



        "We have now gathered all the data"
