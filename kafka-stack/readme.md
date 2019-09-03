# Kafka-stack

## TOC

- [Kafka-stack](#kafka-stack)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Useful commands](#useful-commands)

## Useful links

- [kafka-docker](https://github.com/wurstmeister/kafka-docker)
- [kafka-stack-docker-compose](https://github.com/simplesteph/kafka-stack-docker-compose)
- [python - kafka 1.3.5](https://pypi.org/project/kafka/)

## Useful commands

```sh
# Get into kafka container
$> docker exec -ti kafka /bin/bash
```

```sh
# List topics
$> /opt/kafka/bin/kafka-topics.sh --zookeeper zookeeper:2181 --list
```

```sh
# Create topic:
$> /opt/kafka/bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic sampleTopic
```

```sh
# Create a kafka console producer:
$> /opt/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic topic1
```

```sh
# Create a Kafka Console Consumer.
$> /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic1 --from-beginning
```
