import boto3
import topic

topic_arn = topic.topic_arn

response = topic.sns.delete_topic(
    TopicArn=topic_arn
)

print("Tópico excluído com sucesso.")