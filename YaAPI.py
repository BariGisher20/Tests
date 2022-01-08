import requests

ya_token = "AQAAAABZrWRJAADLW-uwe-vKvEiduk62H2ZU4gg"


def create_directory(dir_name: str):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        "Accept": "application/json",
        "Authorization": "OAuth " + ya_token
    }
    params = {
        'path': dir_name
    }
    r = requests.put(url=url, params=params, headers=headers)
    res = r.json()
    return res


if __name__ == '__main__':
    create_directory('New')
