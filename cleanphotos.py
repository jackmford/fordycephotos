from flask import Flask
app = Flask(__name__)

import boto3
import os
from flask import render_template

AWS_KEY=os.environ['AWS_KEY']
AWS_SECRET=os.environ['AWS_SECRET']
BUCKET_NAME=os.environ['BUCKET_NAME']

@app.route("/")
def hello():
    client = boto3.client('s3', aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET)
    contents = client.list_objects(Bucket=BUCKET_NAME)
    iphone_img_files = os.listdir('static/img/iphone')
    film_img_files = os.listdir('static/img/film')
    for i in range(len(contents['Contents'])):
        img_name = contents['Contents'][i]['Key']
        if img_name not in img_files and 'film' in img_name:
            client.download_file(BUCKET_NAME, img_name, f'static/img/film/{img_name}')
        elif img_name not in img_files:
            client.download_file(BUCKET_NAME, img_name, f'static/img/iphone/{img_name}')
    return render_template('index.html', images=img_files)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
