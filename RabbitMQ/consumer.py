import pika
import json
import pandas as pd
import uuid
def generate_Excel(message):
    message=json.loads(message)
    df=pd.DataFrame(message)
    df.to_excel(f"output_{str(uuid.uuid4())}.xlsx",index=False)
    print(type(message))
    

def callback(ch,method,properties,body):
    message = body.decode()
    generate_Excel(message)
    # print(f"body-{message}")

param=pika.URLParameters("amqps://qiejlosg:xwzSU6iuU_tKFiLp6Irx9XDnZ1yb4BjP@prawn.rmq.cloudamqp.com/qiejlosg")
connections=pika.BlockingConnection(param)
channel=connections.channel()
channel.queue_declare("My_Queue")
channel.basic_consume(queue="My_Queue",on_message_callback=callback,auto_ack=True)
print("Consuming Wating: ")
channel.start_consuming(

)