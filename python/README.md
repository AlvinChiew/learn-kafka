# Intro
Create Kafka project using Python

## Getting 
1. cd into `kafka/`
1. start zookeeper: `bin/zookeeper-server-start.sh config/zookeeper.properties`
1. start 3 brokers: `bin/kafka-server-start.sh config/server[0-2].properties`
1. create topic: `bin/kafka-topics.sh --bootstrap-server localhost:9092,localhost:9093,localhost9094 --create --replication-factor 3 --partitions 5 --topic names`
1. `node producer.js`
1. `node consumer.js`

## Setup
- install kafka into `kafka/`
- `pip install -r requirements.txt`
  - faker: randomly seed test message
