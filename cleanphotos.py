from flask import Flask
app = Flask(__name__)

import os
from flask import render_template

@app.route("/")
def hello():
    film_img_files = os.listdir('static/img/film')
    iphone_img_files = os.listdir('static/img/iphone')
    return render_template('index.html', iphone_images=iphone_img_files, film_images=film_img_files)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
