from random import randint

from flask import Flask, render_template

from data import tours, departures

app = Flask(__name__)


@app.route('/')
def main():
    main_tours = {}
    while len(main_tours) < 6:
        tour = randint(1, len(tours))
        if tour not in main_tours.keys():
            main_tours[tour] = tours[tour]
    return render_template("index.html", departures=departures, main_tours=main_tours)


@app.route('/departures/<city>/')
def departures_view(city):
    tours_for_city = []
    for key, value in tours.items():
        if value['departure'] == city:
            value['id'] = key
            tours_for_city.append(value)
    name = departures[city].split()[1]
    return render_template('departure.html', city=tours_for_city, departures=departures, name=name)


@app.route('/tours/<int:id>/')
def tours_view(id):
    tour = tours[id]
    return render_template('tour.html', tour=tour, departures=departures)


if __name__ == '__main__':
    app.run()
