import requests
import pytest
from modules.api.clients.github import GitHub


class GitHub:

    def get_user_defunkt(self):
        r = requests.get('https://api.github.com/users/defunkt')
        body = r.json()

        return body
