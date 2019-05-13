import threading
import pika
import time


PARAM = pika.ConnectionParameters('localhost', port=5672)

def consumer(n_consumer):
    conn = pika.BlockingConnection(PARAM)
    channel = conn.channel()
    channel.queue_declare(queue='hello', durable=True)

    def callback(ch, method, properties, body):
        time.sleep(1)
        print(f'DONE {n_consumer}')
        """
        Подтверждение (ack) отправляется consumer для
        информирования RabbitMQ о том, что полученное сообщение было обработано и RabbitMQ может его удалить.
        Вместо auto_ack=True
        """
        ch.basic_ack(delivery_tag=method.delivery_tag)


    channel.basic_consume(queue='hello',
                         # auto_ack=True,
                          on_message_callback=callback)
    channel.start_consuming()

########################################################################


def produser():
    conn = pika.BlockingConnection(PARAM)
    channel = conn.channel()
    channel.queue_declare(queue='hello', durable=True)
    channel.basic_qos(prefetch_count=1) # one worker - one message
    channel.basic_publish(exchange='', #  one worker - one message
                          routing_key='hello',
                          body='Shalom',
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))


    conn.close()

#-------------------------------------------------------------------

for i in range(4):
    threading.Thread(target=consumer, args=(f'Consumer {i}',)).start()
time.sleep(2)
for i in range(11):
    produser()

