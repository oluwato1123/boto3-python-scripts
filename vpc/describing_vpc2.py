import boto3

client = boto3.client("ec2")

#Describe one vpc based on vpcid
vpcs = client.describe_vpcs(VpcIds = ["vpc-06f6b1337121f5e8c"])
print(vpcs)