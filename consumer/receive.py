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

def callback(ch, method, properties, body):
    print(" [x] Received: " + body.decode('utf-8'))

channel.basic_consume(queue='pythonQueue', on_message_callback=callback, auto_ack=True)

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