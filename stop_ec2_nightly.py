import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    #Get a list of regions
    regions = [region['RegionName']]
    
    #Call describe Regions and for each Region we get the region name and assign it to the regions list
    for region in ec2.describe_region()['Regions'] 
    
    #Iterate over each region 
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        
        #This shows in CloudWatch logs, any print statement goes to CloudWatch
        print("Region:", region)
        
        #Get only running instances
        instances = ec2.instances.filter( #Using a filter we can get ec2 instance in a certain state 
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
            )
            
        #Iterate over list of running and stopping them instances
        for instance in instances:
            instances.stop()
            print('Stopped instance':, instance.id)