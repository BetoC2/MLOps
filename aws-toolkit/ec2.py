#Create a EC2 instance t2.micro on virginiaregion
import boto3
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='XXXXXXXXXXXXXXXXXXXXX',
      InstanceType='t2.micro',
      MaxCount=1,
      MinCount=1)
