import time
from kafka import KafkaProducer
from faker import Faker


fake = Faker()
topic = 'names'

producer = KafkaProducer(bootstrap_servers=['localhost:9092','localhost:9093','localhost:9094'])
while True:
  message = fake.name().encode('utf-8')
  print(message)
  producer.send(topic, message)
  time.sleep(1)
