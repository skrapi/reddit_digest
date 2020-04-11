# Reddit Digest
A python script which generates an HTML file with the top posts from your favourite subreddits

# How to use

First you will need to get OUATH credentials from reddit. 
1. Go to (Reddit Apps)[https://www.reddit.com/prefs/apps]
2. Create a new app.
3. Use whatever name you want, and use https://www.reddit.com/ as your redirect url (it only really cares that you include the "https://" part)
4. Install all the dependencies using pipenv install
5. Create a file called secrets.py in your local repo and add your credentials like this

   ``` python
    REDDIT_OUATH_CLIENT_ID = 'value under personal use script on the Reddit Apps page'
    REDDIT_OUATH_CLIENT_SECRET = 'your apps secret'
    ```

6. Add your favourite subreddits in the subreddits array in reddit_digest.py
7. Run reddit_digest.py