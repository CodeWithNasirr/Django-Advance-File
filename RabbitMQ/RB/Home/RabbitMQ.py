import pika
import json

def publish_msg(message):
    parms=pika.URLParameters("amqps://qiejlosg:xwzSU6iuU_tKFiLp6Irx9XDnZ1yb4BjP@prawn.rmq.cloudamqp.com/qiejlosg")
    connection=pika.BlockingConnection(parms)
    channel=connection.channel()
    channel.queue_declare(queue="My_Queue")
    message = json.dumps(message)
    channel.basic_publish(
        exchange='',
        routing_key='My_Queue',
        body=message,
    )
    print(f'Message Published {message}')
    connection.close()
