import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')


table = dynamodb.Table('Top_10_moviess')

#This will query for a movieID with imdb-01

response = table.query(
    KeyConditionExpression = Key('movieID').eq('imdb-01')
)

print(response['Items'])