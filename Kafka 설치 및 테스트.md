## Kafka 설치 및 테스트

apache kafka in windows and test



#### 1) Apache Kafka 다운로드

http://mirror.navercorp.com/apache/kafka/1.1.0/kafka_2.11-1.1.0.tgz 에서 

다운로드 후, 아무 폴더에나 압축 해제



#### 2) Zookeeper server 시작

```
C:\kafka_2.11-2.1.0\bin\windows>zookeeper-server-start.bat      ../../config/zookeeper.properties
```



#### 3) Kafka server 시작

```
C:\kafka_2.11-2.1.0\bin\windows>kafka-server-start.bat ../../config/server.properties
```



#### 4) Topic 생성

```
C:\kafka_2.11-2.1.0\bin\windows>kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic [토픽명]
```



#### 5) Topic 목록 확인

```
C:\kafka_2.11-2.1.0\bin\windows>kafka-topics.bat --list --zookeeper localhost:2181
```

