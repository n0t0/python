#   Print First Instance ID

import boto3

ec2 = boto3.client('ec2')


response = ec2.describe_instances(
    MaxResults=5
)

print response['Reservations'][0]['Instances'][0]['InstanceId']

#   Print First 5 Instances

import boto3

ec2 = boto3.client('ec2')


response = ec2.describe_instances(
    MaxResults=5
)

# print response['Reservations'][0]['Instances'][3]['InstanceId']

for reservation in response['Reservations']:
    print reservation['Instances'][0]['InstanceId']


#   Print Instance ID and Tags

import boto3


ec2 = boto3.client('ec2')


response = ec2.describe_instances(
    MaxResults=5
)

# print response['Reservations'][0]['Instances'][3]['InstanceId']

for reservation in response['Reservations']:
    i = reservation['Instances'][0]
    print i['InstanceId']
    for tag in i['Tags']:
        print tag['Key'], tag['Value']

#   Print Instance ID and Tags if Conditions are Met

import boto3


ec2 = boto3.client('ec2')


response = ec2.describe_instances(
    MaxResults=5
)

# print response['Reservations'][0]['Instances'][3]['InstanceId']

for reservation in response['Reservations']:
    i = reservation['Instances'][0]
    print i['InstanceId']
    for tag in i['Tags']:
        if tag['Key'] == 'Owner':
            if tag['Value'] == 'kachon.lei':
                print '\t' + tag['Key'], tag['Value']
