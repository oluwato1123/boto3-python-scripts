import boto3

s3 = boto3.client('s3')

#s3.create_bucket(Bucket = "fade-test-bot03", CreateBucketConfiguration = {'LocationConstraint':'us-east-2'})

response = s3.list_buckets()

buckets = response["Buckets"]

for bucket in buckets:
    print(bucket["Name"])