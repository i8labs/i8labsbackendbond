import boto3
import json

def lambda_handler(event, context):
    response_data = "Hi this is Hello World fom AutoCheckin"
    return {"statusCode": 200, "body": json.dumps(response_data)}
