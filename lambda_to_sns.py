import boto3
import json

sns = boto3.client('sns')

#Enter sns arn for the destination
sns_topic_arn = 'arn:aws:sns:us-east-1:901305956784:sns_testing'

#Data from the lambda trigger(a sqs queue) is inputed into the event parameter
#For loop below is parsing the dictionary for info and publishing it to SNS Topic
def lambda_handler(event,context):
    for i in event['Records']:
        print("test")
        payload = i['body']
        print(str(payload))
        
    response = sns.publish(
        TopicArn= sns_topic_arn,
        Message= payload)

