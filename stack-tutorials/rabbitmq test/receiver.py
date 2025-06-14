#!/usr/bin/env python
import pika
import sys
import os

import mcfg


def main():
  connection = pika.BlockingConnection(mcfg.parameters)
  channel = connection.channel()

  channel.queue_declare(queue=mcfg.QUEUE_NAME)

  def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

  channel.basic_consume(queue=mcfg.QUEUE_NAME,
                        on_message_callback=callback,
                        auto_ack=True)

  print(' [*] Waiting for messages. To exit press CTRL+C')
  channel.start_consuming()


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Interrupted')
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)
