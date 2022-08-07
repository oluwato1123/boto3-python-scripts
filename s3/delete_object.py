import boto3

s3 = boto3.client("s3")

#Deleting single object
s3.delete_object(Bucket = 'fade-tobi-08022022',
    Key = 'beach.jpg')