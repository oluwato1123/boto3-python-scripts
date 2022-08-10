import boto3


dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

table = dynamodb.Table('Top_10_moviess')

response = table.delete_item(
    Key={
        'movieID':'imdb-01', 'Title':' The GodFather'
        }
    )
print(response)