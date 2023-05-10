import requests
import abc


class AuthHandler:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expires_in = None

    def get_access_token(self):
        if not self.access_token or self.token_expires_in <= 0:
            auth_url = 'https://us.battle.net/oauth/token'
            data = {
                'grant_type': 'client_credentials'
            }
            auth = (self.client_id, self.client_secret)
            response = requests.post(auth_url, data=data, auth=auth)
            if response.status_code == 200:
                response_data = response.json()
                self.access_token = response_data['access_token']
                self.token_expires_in = response_data['expires_in']
            else:
                raise ValueError(f"Failed to get access token: {response.content}")
        return self.access_token


class BattleNetBase(abc.ABC):
    base_url = 'https://us.api.blizzard.com'

    def __init__(self, token):
        self.token = token

    def get(self, path: str, params: dict = None) -> dict:
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Battlenet-Namespace': 'static-us'
        }
        url = f'{self.base_url}{path}'
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            raise Exception(f'Request failed with status {response.status_code}: {response.text}')

        return response.json()

    @abc.abstractmethod
    def get_endpoint(self, **kwargs) -> dict:
        pass


class WowGuildMembers(BattleNetBase):
    def get_endpoint(self, realm: str, guild_name: str) -> dict:
        path = f'/data/wow/guild/{realm}/{guild_name}/roster'
        return self.get(path)

