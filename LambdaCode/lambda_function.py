import boto3
import json

def lambda_handler(event, context):

    print("Function Name:", context.function_name)
    response_data = "Hi this is Hello World for Pipeline Deployment :" + context.function_name
    return {"statusCode": 200, "body": json.dumps(response_data)}
