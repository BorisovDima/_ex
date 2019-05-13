import threading
import pika
from functools import partial
from contextlib import contextmanager
import time

PARAM = pika.ConnectionParameters('localhost', port=5672)

@contextmanager
def man():
    conn = pika.BlockingConnection(PARAM)
    channel = conn.channel()
    channel.exchange_declare(exchange='TES_direct',
                             exchange_type='direct')
    try:
        yield channel
    finally:
        conn.close()


def callback(ch, method, properties, body):
    print(body)


def consumerA():
    with man() as channel:
        r = channel.queue_declare('', exclusive=True)
        channel.queue_bind(exchange='TES_direct', queue=r.method.queue, routing_key='black')

        channel.basic_consume(queue=r.method.queue,
                              auto_ack=True,
                              on_message_callback=callback)
        channel.start_consuming()

def consumerB():
    with man() as channel:
        r = channel.queue_declare('', exclusive=True)
        channel.queue_bind(exchange='TES_direct', queue=r.method.queue, routing_key='white')
        channel.queue_bind(exchange='TES_direct', queue=r.method.queue, routing_key='orange')

        channel.basic_consume(queue=r.method.queue,
                              auto_ack=True,
                              on_message_callback=callback)
        channel.start_consuming()

def producer():
    with man() as channel:
        channel.basic_publish(exchange='TES_direct',
                              routing_key='white',
                              body='HELLO! white')

        channel.basic_publish(exchange='TES_direct',
                              routing_key='black',
                              body='HELLO! black')



threading.Thread(target=consumerA).start()
threading.Thread(target=consumerB).start()
# Если нет подписчиков, то сообщение удаляется
time.sleep(3)
producer()