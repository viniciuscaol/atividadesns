import boto3
from urllib.parse import urlparse

sns = boto3.client('sns', region_name='us-east-1') 

response = sns.create_topic(
    Name='Ada_Topic'
)

topic_arn = response['TopicArn']
print("Tópico criado com sucesso. ARN do Tópico:", topic_arn)