import requests
import json
import time
import random

class Account:
    def __init__(self, nickname, token, genshin=True, honkai_star_rail=True, honkai_3=True):
        self.nickname = nickname
        self.token = token
        self.genshin = genshin
        self.honkai_star_rail = honkai_star_rail
        self.honkai_3 = honkai_3

        # Validate token format (example)
        if not self.validate_token(token):
            raise ValueError("Invalid token format!")

    def validate_token(self, token):
        # Implement your token format validation logic here
        # This example checks for a minimum length
        return len(token) >= 10

list_accounts = []

list_accounts.extend([
    Account("Haru", "your_actual_token_1", genshin=True, honkai_star_rail=True, honkai_3=True),
    Account("Man", "your_actual_token_2", genshin=False, honkai_star_rail=True, honkai_3=False),
    # ... add more accounts with nicknames
])

def main():
    for account in list_accounts:
        hoyolab_response = auto_sign_function(account)
        print(f"{account.nickname} : {hoyolab_response} ")

        # Introduce a slight delay between requests (avoid aggressive behavior)
        time.sleep(random.uniform(1, 5))

def auto_sign_function(account):
    sign_urls = {
        "genshin": "https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=vi-vn&act_id=e202102251931481",
        "honkai_star_rail": "https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=vi-vn&act_id=e202303301540311",
        "honkai_3": "https://sg-public-api.hoyolab.com/event/mani/sign?lang=vi-vn&act_id=e202110291205111"
    }

    headers = {
        "Cookie": account.token,
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "x-rpc-app_version": "2.34.1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
        "x-rpc-client_type": "4",
        "Referer": "https://act.hoyolab.com/",
        "Origin": "https://act.hoyolab.com"
    }

    response = ""

    for game, url in sign_urls.items():
        if getattr(account, game):  # Use getattr for dynamic game selection
            hoyolab_response = requests.post(url, headers=headers)
            response += f"\n {game}: {json.loads(hoyolab_response.text)['message']}"

    return response

# Call the main function
if __name__ == "__main__":
    main()
