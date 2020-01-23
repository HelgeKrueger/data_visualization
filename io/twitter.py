import os
import tweepy


class Twitter:
    def __init__(self):
        self.oauth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET_KEY'])


    def auth(self):
        redirect_url = self.oauth.get_authorization_url()

        print("Please open the following url in a webbrowser and allow access")
        print(redirect_url)

        verify = raw_input("Please enter the token: ")

        self.oauth.get_access_token(verify)

        self.api = tweepy.API(self.oauth)

    def post_file(self, filename):
        self.api.update_with_media(filename)