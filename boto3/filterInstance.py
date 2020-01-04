#   Filter Instance on Tag

import boto3


ec2 = boto3.client('ec2', region_name='us-west-2')

response = ec2.describe_instances(
    MaxResults=10
)
reservations = response['Reservations']

while True:
    if 'NextToken' not in response:
        break
    else:
        response = ec2.describe_instances(
            MaxResults=10,
            NextToken=response['NextToken']
        )
        reservations += response['Reservations']


# print response['Reservations'][0]['Instances'][3]['InstanceId']

def filter_instance_on_tag(key, value):
    for reservation in reservations:
        i = reservation['Instances'][0]
        for tag in i['Tags']:
            if tag['Key'] == key:
                if tag['Value'] == value:
                    print i['InstanceId']
                    print '\t' + tag['Key'], tag['Value']


filter_instance_on_tag('Environment', 'prod')
for i in range(3):
    print '=' * 80

stage_instances = filter_instance_on_tag('Environment', 'stage')

#   Print Private IP on Filter Instance by Tags

import boto3


ec2 = boto3.client('ec2', region_name='us-west-2')

response = ec2.describe_instances(
    MaxResults=10
)
reservations = response['Reservations']

while True:
    if 'NextToken' not in response:
        break
    else:
        response = ec2.describe_instances(
            MaxResults=10,
            NextToken=response['NextToken']
        )
        reservations += response['Reservations']


# print response['Reservations'][0]['Instances'][3]['InstanceId']

def filter_instance_on_tag(key, value):
    instancesIds = []
    for reservation in reservations:
        i = reservation['Instances'][0]
        for tag in i['Tags']:
            if tag['Key'] == key:
                if tag['Value'] == value:
                    instancesIds.append(i['InstanceId'])
    return instancesIds


def print_instance_private_ip(instanceId):
    for instance in reservations:
        if instance['Instances'][0]['InstanceId'] == instanceId:
            print instance['Instances'][0]['PrivateIpAddress']


prod_instances = filter_instance_on_tag('Environment', 'prod')

for instanceId in prod_instances:
    print_instance_private_ip(instanceId)

#   Separate Funcs

import boto3


ec2 = boto3.client('ec2', region_name='us-west-2')

response = ec2.describe_instances(
    MaxResults=10
)
reservations = response['Reservations']

while True:
    if 'NextToken' not in response:
        break
    else:
        response = ec2.describe_instances(
            MaxResults=10,
            NextToken=response['NextToken']
        )
        reservations += response['Reservations']


# print response['Reservations'][0]['Instances'][3]['InstanceId']

def filter_instance_on_tag(key, value):
    instancesIds = []
    for reservation in reservations:
        i = reservation['Instances'][0]
        for tag in i['Tags']:
            if tag['Key'] == key:
                if tag['Value'] == value:
                    instancesIds.append(i['InstanceId'])
    return instancesIds


def print_instance_ips(instanceId):
    for instance in reservations:
        if instance['Instances'][0]['InstanceId'] == instanceId:
            if 'PrivateIpAddress' in instance['Instances'][0]:
                private_ip = instance['Instances'][0]['PrivateIpAddress']
            if 'PublicIpAddress' in instance['Instances'][0]:
                public_ip = instance['Instances'][0]['PublicIpAddress']
            else:
                public_ip = 'No public IP'
            print private_ip, public_ip


prod_instances = filter_instance_on_tag('Environment', 'prod')

for instanceId in prod_instances:
    print instanceId
    print_instance_ips(instanceId)
