"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <body>
        <h1>Hi! This is the home page.</h1>
        <p><a href="http://localhost:5000/hello">CLICK HERE</a></p>
      </body>
    </html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          Compliment
          <select name="compliment">
            <option value="terrific">Terrific</option>
            <option value="awesome">Awesome</option>          
            <option value="fantastic">Fantastic</option>
            <option value="pythonic">Pythonic</option>
            <option value="fantastic">Fantastic</option>
            <option value="fantastic">Fantastic</option>
          </select>
          <input type="submit" value="Submit"><br><br>
          </form><br><br>
          <form action="/diss">
          What's your name? <input type="text" name="person">
          Diss
            <input type="radio" name="diss" value="stinky">Stinky
            <input type="radio" name="diss" value="yucky">Yucky
            <input type="radio" name="diss" value="boring">Boring
            <input type="submit" value="Submit"><br><br>
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss")
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)

if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
