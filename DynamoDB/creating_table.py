import boto3

# replace the keys below

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='AKIATMXXXXXXXXXX',
    aws_secret_access_key='B6FGfXXXXXXX',
    region_name='us-east-1',
    )
    
table = dynamodb.create_table (
    TableName='Top_10_movies',
    KeySchema = [
        {
            'AttributeName': 'movieID',
            'KeyType': 'HASH'   # This is the partition key
        },
        
         {
            'AttributeName': 'Title',
            'KeyType': 'RANGE'   # This is the sort key
        }
        
        
    ],
    
    AttributeDefinitions = [
        {
            'AttributeName': 'movieID',
            'AttributeType': 'S'
        },
        
        {
            'AttributeName': 'Title',
            'AttributeType': 'S'
        },
        
  
        
    ],
    
    ProvisionedThroughput = {
        'ReadCapacityUnits': 15,
        'WriteCapacityUnits': 15
    }
)
    
    
print(table)

