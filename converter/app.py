from flask import Flask, render_template, request
from converter import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert', methods=['POST'])
def convert():
    choice = request.form['choice']
    value = float(request.form['value'])

    if choice == '1':
        result = inches_to_feet(value)
        unit_from = 'inches'
        unit_to = 'feet'
    elif choice == '2':
        result = feet_to_inches(value)
        unit_from = 'feet'
        unit_to = 'inches'
    elif choice == '3':
        result = feet_to_yards(value)
        unit_from = 'feet'
        unit_to = 'yards'
    elif choice == '4':
        result = yards_to_feet(value)
        unit_from = 'yards'
        unit_to = 'feet'
    elif choice == '5':
        result = meters_to_feet(value)
        unit_from = 'meters'
        unit_to = 'feet'
    elif choice == '6':
        result = feet_to_meters(value)
        unit_from = 'feet'
        unit_to = 'meters'
    elif choice == '7':
        result = miles_to_feet(value)
        unit_from = 'miles'
        unit_to = 'feet'
    elif choice == '8':
        result = feet_to_miles(value)
        unit_from = 'feet'
        unit_to = 'miles'
    elif choice == '9':
        result = kilometers_to_miles(value)
        unit_from = 'kilometers'
        unit_to = 'miles'
    elif choice == '10':
        result = miles_to_kilometers(value)
        unit_from = 'miles'
        unit_to = 'kilometers'
    elif choice == '11':
        result = pounds_to_kilograms(value)
        unit_from = 'pounds'
        unit_to = 'kilograms'
    elif choice == '12':
        result = kilograms_to_pounds(value)
        unit_from = 'kilograms'
        unit_to = 'pounds'
    elif choice == '13':
        result = fahrenheit_to_celsius(value)
        unit_from = 'Fahrenheit'
        unit_to = 'Celsius'
    elif choice == '14':
        result = celsius_to_fahrenheit(value)
        unit_from = 'Celsius'
        unit_to = 'Fahrenheit'
    elif choice == '15':
        result = feet_to_centimeters(value)
        unit_from = 'feet'
        unit_to = 'centimeters'
    elif choice == '16':
        result = centimeters_to_feet(value)
        unit_from = 'centimeters'
        unit_to = 'feet'
    elif choice == '17':
        result = gallons_to_liters(value)
        unit_from = 'gallons'
        unit_to = 'liters'
    elif choice == '18':
        result = liters_to_gallons(value)
        unit_from = 'liters'
        unit_to = 'gallons'
    elif choice == '19':
        result = ounces_to_grams(value)
        unit_from = 'ounces'
        unit_to = 'grams'
    elif choice == '20':
        result = grams_to_ounces(value)
        unit_from = 'grams'
        unit_to = 'ounces'
    elif choice == '21':
        result = hours_to_minutes(value)
        unit_from = 'hours'
        unit_to = 'minutes'
    elif choice == '22':
        result = minutes_to_hours(value)
        unit_from = 'minutes'
        unit_to = 'hours'
    elif choice == '23':
        result = days_to_hours(value)
        unit_from = 'days'
        unit_to = 'hours'
    elif choice == '24':
        result = hours_to_days(value)
        unit_from = 'hours'
        unit_to = 'days'
    elif choice == '25':
        result = miles_to_knots(value)
        unit_from = 'miles'
        unit_to = 'knots'
    elif choice == '26':
        result = knots_to_miles(value)
        unit_from = 'knots'
        unit_to = 'miles'
    else:
        return "Invalid choice"

    return render_template('result.html', result=result, unit_from=unit_from, unit_to=unit_to)

if __name__ == '__main__':
    app.run(debug=True)
