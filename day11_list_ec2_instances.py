import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print("Instance ID:", instance["InstanceId"])
        print("State:", instance["State"]["Name"])
        print("-" * 30)
