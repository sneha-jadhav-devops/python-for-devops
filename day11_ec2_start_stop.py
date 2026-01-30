import boto3

ec2 = boto3.client("ec2")

instance_id = "i-xxxxxxxxxxxx"

# Start instance
ec2.start_instances(InstanceIds=[instance_id])
print("EC2 instance starting")

# Stop instance
# ec2.stop_instances(InstanceIds=[instance_id])
# print("EC2 instance stopping")
