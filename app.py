from flask import Flask, render_template
from pages import pages

app = Flask(__name__)
app.register_blueprint(pages, url_prefix="")

if __name__ == "__main__":
    app.run(host= '10.0.0.223', port='5')