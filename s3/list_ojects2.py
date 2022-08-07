import boto3

s3 = boto3.client("s3")

objects = s3.list_objects(
    Bucket='fade-tobi-08022022'
 
)["Contents"]

for object in objects:
    print(object["Key"])