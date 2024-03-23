import datetime
import pika
import json
import time

# Connect to a RabbitMQ server running on the local machine
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="localhost",
     port=5672,
     virtual_host="/"))

channel = connection.channel()

transaction_file = open("transaction2.json")
transactions = json.load(transaction_file)
transaction_file.close()


# Declare a queue named 'hello'
channel.queue_declare(queue='movimentacao')


# Message attributes
properties = pika.BasicProperties(
    content_type='application/json',      # MIME-type of the message body
     app_id='proj_01producer.py',                 # Identifier for the application

)
for transaction in transactions:
    transaction["data"] = str(datetime.datetime.now())#incluindo valor no Dict transaction

# Publish a message to the 'hello' queue
    channel.basic_publish(exchange="amq.fanout",
                      routing_key="",
                      body= json.dumps(transaction), 
                      properties=properties)

    print(f"[x] Sent '{json.dumps(transaction)}'")
    time.sleep(1)
# Close the connection
channel.close()