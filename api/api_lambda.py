import json
import uuid

GET_RAW_PATH = "/getImage"
CREAT_RAW_PATH = "/createImage"

def lambda_handler(event, context):
    print(event)
    if event["rawPath"] == GET_RAW_PATH:
        #GetPerson Path
        print("Start Request for GetPerson")
        #personId = event['queryStringParameters']['personId']
        return {"firstName" : "Daniel", "lastName": "G", "email":"something@gmail.com"}
        
    elif event['rawPath'] == CREAT_RAW_PATH:
        #Write to Database
        print("Start Request for CreatePerson")
        decodedEvent = json.loads(event['body'])
        firstName = decodedEvent["firstName"]
        return {"personId": str(uuid.uuid1())}
        
        
    
#######

import boto3

def lambda_handler(event, context):
    # Initialize the S3 client
    s3 = boto3.client('s3')

    # Define your S3 bucket and object key
    bucket_name = 'your-bucket-name'
    object_key = 'your-object-key'

    try:
        # Example: Get an object from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        data = response['Body'].read().decode('utf-8')
        print(data)

        # Example: Put an object to S3
        s3.put_object(Bucket=bucket_name, Key='new-object-key', Body='Hello from Lambda!')

        return {
            'statusCode': 200,
            'body': 'S3 access from Lambda successful'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error accessing S3: {str(e)}'
        }