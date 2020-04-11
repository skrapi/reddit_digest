import praw
import grip
from secrets import REDDIT_OUATH_CLIENT_ID, REDDIT_OUATH_CLIENT_SECRET

class Markdown:
    @staticmethod
    def h1(text):
        return "# {}\n".format(text)
  
    @staticmethod
    def h2(text):
        return "## {}\n".format(text)

    @staticmethod
    def h3(text):
        return "### {}\n".format(text)
    
    @staticmethod
    def h4(text):
        return "#### {}\n".format(text)

    @staticmethod
    def text(text):
        return "{}\n".format(text)

    @staticmethod
    def link(text, link):
        return "[{}]({})\n".format(text, link)


# Log into reddit
reddit = praw.Reddit(client_id=REDDIT_OUATH_CLIENT_ID, client_secret=REDDIT_OUATH_CLIENT_SECRET, user_agent='my user agent')


subreddits = ["rust", "elm", "ProgrammerHumor"]

NUM_OF_POSTS = 5

with open('test.md', 'w') as file:
    file.write(Markdown.h1("Reddit Digest"))
    for subreddit in subreddits:
        file.write(Markdown.h2(subreddit.capitalize()))
        for post in reddit.subreddit(subreddit).top('week', limit=NUM_OF_POSTS):
            file.write(Markdown.h3(post.title))
            if (len(post.selftext) > 200):
                file.write(Markdown.text(post.selftext[:200] + ' ...'))
            else:
                file.write(Markdown.text(post.selftext))
            file.write("\n" + Markdown.link("link",post.url))

grip.export(path="test.md", quiet=True)


