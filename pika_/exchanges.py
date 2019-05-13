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
    channel.exchange_declare(exchange='TES',
                             exchange_type='fanout')
    try:
        yield channel
    finally:
        conn.close()


def callback(name, ch, method, properties, body):
    print(ch._consumer_infos, method, properties.__dict__)
    print(name, body)


def consumerA():
    with man() as channel:
        r = channel.queue_declare('', exclusive=True)
        channel.queue_bind(exchange='TES', queue=r.method.queue)

        channel.basic_consume(queue=r.method.queue,
                              auto_ack=True,
                              on_message_callback=partial(callback, 'A'))
        channel.start_consuming()

def consumerB():
    with man() as channel:
        r = channel.queue_declare('TESTimkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk', exclusive=True)
        channel.queue_bind(exchange='TES', queue=r.method.queue)

        channel.basic_consume(queue=r.method.queue,
                              auto_ack=True,
                              on_message_callback=partial(callback, 'B'))
        channel.start_consuming()

def producer():
    with man() as channel:
        channel.basic_publish(exchange='TES',
                              routing_key='',
                              body='HELLO!')



threading.Thread(target=consumerA).start()
threading.Thread(target=consumerB).start()
# Если нет подписчиков, то сообщение удаляется 
time.sleep(3)
producer()