class AmazonOAuthClient:
    def __init__(self, client_id, client_secret, refresh_token, token_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.token_url = token_url
        self.session = None
        self.token = None

    def initialize_session(self):
        self.create_oauth_session()

    def create_oauth_session(self):
        client = BackendApplicationClient(client_id=self.client_id)
        self.session = OAuth2Session(client=client)
        self.refresh_access_token()

    def get_new_access_token(self):
        extra = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
            'grant_type': 'refresh_token',
        }
        try:
            token = self.session.fetch_token(token_url=self.token_url, **extra)
            token['expires_at'] = time.time() + token.get('expires_in')
            return token
        except TokenExpiredError:
            logger.error("The refresh token has expired.")
        except RequestException as e:
            logger.error(f"Failed to fetch new access token: {e}")

    def is_token_expired(self):
        return time.time() > self.token.get('expires_at', 0)

    def refresh_access_token(self):
        if not self.token or self.is_token_expired():
            self.token = self.get_new_access_token()
            if self.token:
                self.session.token = self.token
            else:
                raise Exception("Unable to refresh access token.")

