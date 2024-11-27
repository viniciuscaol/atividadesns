import boto3
import topic

topic_arn = topic.topic_arn

response = topic.sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='viniciuscaol@gmail.com',
    Attributes={
        'FilterPolicy' : '{"type": ["email"]}'
    },
    ReturnSubscriptionArn=True
)

response = topic.sns.subscribe(
    TopicArn=topic_arn,
    Protocol='sms',
    Endpoint='+5571999573945',
    Attributes={
        'FilterPolicy' : '{"type": ["sms"]}'
    },
    ReturnSubscriptionArn=True
)

print("Assinatura criada com sucesso. ARN da assinatura:", response['SubscriptionArn'])