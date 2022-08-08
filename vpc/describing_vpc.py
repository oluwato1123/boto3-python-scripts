import boto3

client = boto3.client("ec2")

vpcs = client.describe_vpcs()['Vpcs']
vpcs

for vpc in vpcs:
    print(vpc['VpcId'])