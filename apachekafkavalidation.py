from confluent_kafka import Producer, Consumer
import random

p = Producer({'bootstrap.servers': 'localhost:9092'})

for i in range(1000):
    data = {'number': random.randint(1, 100)}
    p.produce('mytopic', str(data))

p.flush()

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup'})
c.subscribe(['mytopic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print('Error: {}'.format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))