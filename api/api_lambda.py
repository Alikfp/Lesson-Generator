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
        
        
    
