# Intro
Create Kafka project using Node.js

## Getting 
1. cd into `kafka/`
1. start zookeeper: `bin/zookeeper-server-start.sh config/zookeeper.properties`
1. start 3 brokers: `bin/kafka-server-start.sh config/server[0-2].properties`
1. create topic: `bin/kafka-topics.sh --bootstrap-server localhost:9092,localhost:9093,localhost9094 --create --replication-factor 3 --partitions 5 --topic animals`
1. `node producer.js`
1. `node consumer.js`

## Setup
- install kafka into `kafka/`
- `brew install node`
- `npm init`
- `npm install kafkajs chance`
  - chance: randomly seed test message

## Tips
- For new topic, producer will return error due to new topic creation, then subsequently produce the message.
