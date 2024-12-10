import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-count-table')

def lambda_handler(event, context):
    response = table.get_item(Key={'id':'1'})
    views = int(response['Item']['views']) 
    views += 1
    
    response = table.update_item(
        Key={'id':'1'},
        UpdateExpression='SET #v = :val',
        ExpressionAttributeNames={'#v': 'views'},
        ExpressionAttributeValues={':val': views}
    )

    return {
    'statusCode': 200,
    'body': json.dumps({'views': views})
}
