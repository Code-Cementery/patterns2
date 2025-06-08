import pika

URL = "amqps://dlevpjus:eRwT3Q1QKuPDZGTcGVKSCZiS2mqM65HI@sparrow.rmq.cloudamqp.com/dlevpjus"

QUEUE_NAME = 'tesomsz'

parameters = pika.URLParameters(URL)
