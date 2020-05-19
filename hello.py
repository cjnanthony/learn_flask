from flask import Flask  # flask = package, #Flask = class

app = Flask(__name__)  # instantiating Flask class--> when running this file, __name__ will be = to __main__


@app.route('/')  # function is mapped to the '/' URL which is the home URL
def home():      # if the route was '/about/' the following home() function would display on the about page not home
    return "Hey there!"


if __name__ == '__main__':  # if the script is the one being executed
    app.run(debug=True)  # if this is True, the page will print errors TO THE PAGE (obv not for production)

