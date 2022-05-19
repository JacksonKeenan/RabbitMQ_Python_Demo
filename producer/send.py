import pika, sys, os

rabbit_host = os.environ.get("RABBIT_HOST")
rabbit_port = os.environ.get("RABBIT_PORT")
rabbit_user = os.environ.get("RABBIT_USERNAME")
rabbit_password = os.environ.get("RABBIT_PASSWORD")

credentials = pika.PlainCredentials(rabbit_user, rabbit_password)
parameters = pika.ConnectionParameters(rabbit_host, rabbit_port, '/', credentials)

try:
    connection = pika.BlockingConnection(parameters)
except:
    print("Error: Could not connect to RabbitMQ")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

channel = connection.channel()

channel.queue_declare(queue='pythonQueue')

channel.basic_publish(exchange='', routing_key='pythonQueue', body='Hello World!')

print(" [x] Sent: Hello World!")

connection.close()