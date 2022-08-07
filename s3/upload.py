import boto3

s3 = boto3.client("s3")
s3.upload_file(
    Filename = "beach.jpg",
    Bucket = "fade-tobi-08032022",
    Key = "uploadtest.jpg")
    