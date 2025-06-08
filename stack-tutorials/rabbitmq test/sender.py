#!/usr/bin/env python
import pika
import mcfg

connection = pika.BlockingConnection(mcfg.parameters)
channel = connection.channel()

channel.queue_declare(queue=mcfg.QUEUE_NAME)

channel.basic_publish(exchange='', routing_key=mcfg.QUEUE_NAME, body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
