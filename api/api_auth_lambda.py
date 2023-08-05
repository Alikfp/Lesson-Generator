import json

def lambda_handler(event, context):
    # Log the event
    print(event)
    
    if event['header']['authorization'] == '':
        response = {
            "isAuthorized" : True
        }
    else:
        response = {
            "isAuthorized" : False
        }
    return response