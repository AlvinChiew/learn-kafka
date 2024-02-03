from kafka import KafkaConsumer

topic = 'names'

consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092','localhost:9093','localhost:9094'],group_id='consumer-group-digits')
for message in consumer:
  print(message)