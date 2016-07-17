from flask import Flask, render_template, url_for, redirect
import json

# For now we're just reading from JSON until
# it's worth tossing everything in a database.
# That will probably be the same time the tracker's up

app = Flask(__name__)

def grab_torrents():
    with open('torrents/torrents.json', 'r') as f:
        return json.loads(f.read())

@app.route('/')
def index_view():
    return render_template('index.html', torrents=grab_torrents())

@app.route('/torrent/<torrent>')
def torrent_view(torrent):
    t = int(torrent)
    torrents = grab_torrents()
    torrents['torrents'][t]['downloads'] += 1
    url = torrents['torrents'][t]['link']
    torrents = json.dumps(torrents, indent=4)

    with open('torrents/torrents.json', 'w') as f:
        f.write(torrents)
    return redirect(url)

if __name__ == '__main__':
    app.debug = True
    app.run()
