import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

table = dynamodb.Table('Top_10_moviess')

table.delete()