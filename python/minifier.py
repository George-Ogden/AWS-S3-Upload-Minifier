import json
import boto3
import requests
urls = {"html":'https://html-minifier.com/raw',"css":"https://cssminifier.com/raw","js":"https://javascript-minifier.com/raw"}
client = boto3.client("s3")
def lambda_handler(event, context=None):
    files = map((lambda record: {"Key":record["s3"]["object"]["key"],"Bucket":record["s3"]["bucket"]["name"]}),event["Records"])
    for location in files:
        file = client.get_object(**location)["Body"]
        print(file.read())
        extension = location["Key"].split(".")[-1]
        if not extension in urls.keys(): return 
        url = urls[extension]
        request = requests.post(url , {'input': file._raw_stream})
        client.put_object(**location,Body=request.text)
    return {"statusCode":200}