import os
import tweepy


class Twitter:
    def __init__(self):
        self.oauth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET_KEY'])

        if 'TWITTER_ACCESS_TOKEN' in os.environ:
            self.oauth.access_token = os.environ['TWITTER_ACCESS_TOKEN']
        if 'TWITTER_ACCESS_TOKEN_SECRET' in os.environ:
            self.oauth.access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    def auth(self):
        if not self.oauth.access_token:
            redirect_url = self.oauth.get_authorization_url()

            print("Please open the following url in a webbrowser and allow access")
            print(redirect_url)

            verify = input("Please enter the token: ")

            print(self.oauth.get_access_token(verify))

        self.api = tweepy.API(self.oauth)

    def post_file(self, filename, status=None):
        if status:
            self.api.update_with_media(filename, status)
        else:
            self.api.update_with_media(filename)

    def timeline(self, username):
        def convert_status(status):
            return {
                'text': status.text,
                'date': status.created_at
            }
        return list(map(convert_status, self.api.user_timeline(username)))
