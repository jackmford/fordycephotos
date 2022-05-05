from flask import Flask
from flask import render_template
import glob
import os

app = Flask(__name__)


@app.route("/")
def hello():
    film_img_files = glob.glob('static/img/film/*')
    film_img_files.sort(key=os.path.getmtime)

    iphone_img_files = glob.glob('static/img/iphone/*')
    iphone_img_files.sort(key=os.path.getmtime)
    return render_template('index.html', iphone_images=iphone_img_files,
                           film_images=film_img_files)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
