import boto3

s3 = boto3.resource('s3')

def get_pricing():
  print('Detail pricing')