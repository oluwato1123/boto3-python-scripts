import boto3

s3 = boto3.client("s3")

response = s3.list_objects(
    Bucket='fade-tobi-08022022'
 
)

print(response["Contents"])
