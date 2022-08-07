import boto3

s3 = boto3.client("s3")
response = s3.list_buckets()["Buckets"][0:7]
print(response)

name = s3.list_buckets()["Buckets"][0]["Name"]  #This displays the name of the first s3 Bucket
print(name)

creation_date = s3.list_buckets()["Buckets"][6]["CreationDate"] #This displays the creationDate of the fifth s3 Bucket
print(creation_date)
fixed_date = creation_date.strftime("%d-%m-%y_%H:%M:%s")
print(fixed_date)
