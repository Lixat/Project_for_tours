from flask import Flask, render_template

from data import tours, departures

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/departures/<departure>/')
def departure(departure):
    return render_template('departure.html', departure=departure)


@app.route('/tours/<int:id>/')
def tours_view(id):
    tour = tours[id]
    return render_template('tour.html', tour=tour, departures=departures)


if __name__ == '__main__':
    app.run()
