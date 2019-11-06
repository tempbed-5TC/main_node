from temperatures import Temperature
import requests
import toml

config = toml.load('config.toml')

if __name__ == '__main__':
    while(True):
        t = Temperature.from_serial()
        print(t)
        json = t.to_json()
        print(json)
        answer = requests.put(config['server_url'] + '/api/v0.1/temperature',
                              json=json)
        print(answer)
