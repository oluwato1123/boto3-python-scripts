import boto3

ec2 = boto3.client('ec2')
response = ec2.run_instances(
    ImageId='ami-090fa75af13c156b4',
    InstanceType = 't2.micro',
    KeyName = 'KeyName',  # KeyPair Name for EC2
    MinCount = 1,
    MaxCount = 1
)
print(response)