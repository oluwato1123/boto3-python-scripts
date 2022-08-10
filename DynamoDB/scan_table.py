import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Top_10_moviess')

response = table.scan()['Items']

print(response)