import boto3
import topic

topic_arn = topic.topic_arn


response =topic.sns.publish(
    TopicArn=topic_arn,
    Message='Aluno Vinicius entregou o projeto',
    Subject='Entrega de projeto',
    MessageAttributes={
        'type': {
            'DataType': 'String',
            'StringValue': 'sms' # ou 'email'
        }
    }
)

print("Mensagem enviada com sucesso. ID da mensagem:", response['MessageId'])