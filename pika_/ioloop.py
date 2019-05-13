import pika

def callback(coon):
    print(conn)


PARAM = pika.ConnectionParameters('localhost', port=5672)
conn = pika.SelectConnection(PARAM, on_open_callback=callback)

conn.ioloop.start()


