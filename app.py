from flask import Flask
import requests

app = Flask(__name__)


@app.route('/starships')
def get_starships():
    starships_url = 'https://swapi.co/api/starships/'
    starships = {'starships': [],
          'starships_unknown_hyperdrive': []}

    while True:
        r = requests.get(url=starships_url)
        data = r.json()

        # Getting only name and hyperdrive_rating from starships
        for d in data['results']:
            if d['hyperdrive_rating'] == 'unknown':
                starships['starships_unknown_hyperdrive'].append({
                    'name': d['name']
                })
            else:
                starships['starships'].append({
                    'name': d['name'],
                    'hyperdrive': d['hyperdrive_rating']
                })
        # check if there's still starships to load
        if data['next'] is None:
            break
        else:
            starships_url = data['next']

    # Sorting by hyperdrive in ascending order
    starships['starships'].sort(key=lambda x: x['hyperdrive'], reverse=False)

    return starships


if __name__ == '__main__':
    app.run()
