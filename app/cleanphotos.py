from flask import Flask, Blueprint
from flask import render_template
import glob
import os

#app = Flask(__name__)
bp = Blueprint('cleanphotos', __name__)


@bp.route("/")
def hello():
    film_img_files = glob.glob('app/static/img/film/*')
    film_img_files.sort(key=os.path.getmtime)
    for i in range(len(film_img_files)):
        film_img_files[i] = film_img_files[i].strip('app/')

    iphone_img_files = glob.glob('app/static/img/iphone/*')
    iphone_img_files.sort(key=os.path.getmtime)
    for i in range(len(iphone_img_files)):
        iphone_img_files[i] = iphone_img_files[i].strip('app/')
    return render_template('index.html', iphone_images=iphone_img_files,
                           film_images=film_img_files)


#if __name__ == "__main__":
    #app.run(host='0.0.0.0')
