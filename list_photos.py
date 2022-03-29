import boto3
import os

AWS_KEY=os.environ['AWS_KEY']
AWS_SECRET=os.environ['AWS_SECRET']
BUCKET_NAME=os.environ['BUCKET_NAME']

client = boto3.client('s3', aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET)
film_contents = client.list_objects(Bucket=BUCKET_NAME, Prefix='film')
iphone_contents = client.list_objects(Bucket=BUCKET_NAME, Prefix='iphone')
film_img_files = os.listdir('static/img/film')
iphone_img_files = os.listdir('static/img/iphone')

for i in range(1, len(film_contents['Contents'])):
    img_name = film_contents['Contents'][i]['Key']
    if img_name not in film_img_files:
        client.download_file(BUCKET_NAME, img_name, f'static/img/{img_name}')
for i in range(1, len(iphone_contents['Contents'])):
    img_name = iphone_contents['Contents'][i]['Key']
    if img_name not in iphone_img_files:
        client.download_file(BUCKET_NAME, img_name, f'static/img/{img_name}')
