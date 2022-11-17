import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    sqs = boto3.client('sqs')
    
    #Get the current date & time
    response = "The date and time is: "
    date_time = datetime.now()
    
    ##This method formats data into a string 
    current_time = date_time.strftime("%m/%d/%Y, %H:%M:%S") 
    
    
    sqs_message = sqs.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/901305956784/Messages',
    MessageBody='current_time' 
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(current_time)
    }