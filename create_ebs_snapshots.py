from datetime import datetime

import boto3 


def lambda_handler(event, context):
    
    
    ec2_client = boto3.client('ec2')
    
    #Want to iterate across all instances in all regions, need a list of regions 
    regions = [region['RegionName']
              for region in ec2.describe_regions()['Regions']]
    
    #Sets up an EC2 resource object in each region          
    for region in regions:
        print('Instances in EC2 Region {0}:'.format(region))
        ec2 = boto3.resource('ec2', region_name=region)
        
    #Filters out all the EC2 instances with a specfic backup tag 
        instances = ec2.instance.filter(
            Filters=[
                {'Name': 'tag:backup':, 'Values': ['true']}
            ]
        )
            
        #Description were putting in backup, Timestamp in ISO 8601 format, grabbing current time
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
        
        #Iterating the instances in a region with specific backup tag
        #For each instance, want to iterate all the EBS volumes 
        for i in instances.all:
            for v in i.volumes.all():
                #Basically taking a backup of a particular instance ID, with an EBS volume ID, created with a timestamp 
                desc = 'Backup of {0}, volume {1}, created {2}'.format(
                    i.id, v.id, timestamp)
                print(desc)
                
                #Creating snapshot and passing the desc variable for each volume
                snapshot = v.create_snapshot(Description=desc)
                
                print("Created snapshot:", snapshot.id)
    