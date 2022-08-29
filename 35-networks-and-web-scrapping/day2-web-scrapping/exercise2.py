# exercise 2
# make a request using the resource `users`
# to githubs API to https://api.github.com/users
# and print the username and the user api URL

import requests


def main(URL: str) -> str:
    res = requests.get(URL)
    users = res.json()

    for user in users:
        username = user["login"]
        user_url = user["url"]
        print(f"{username} {user_url}")


if __name__ == "__main__":
    main("https://api.github.com/users")
