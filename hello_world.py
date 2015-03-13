
#
#  Hello World!
#
#  A basic Flask app to test the syntax of Flask
#
#  March 2015
#



from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
       <h1>
          Hello {}!
       </h1>
       <p>
          Here is a picture of a kitten. Awww...
       </p>
       <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())


@app.route("/jedi/<first>/<second>")
def jedi_name(first, second):
    return "Hello {s}{f}".format(s=second[0:3].title(), f=first[0:2])


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8080)
