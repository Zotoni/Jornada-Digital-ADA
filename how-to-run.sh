#Como rodar o Projeto
#necessário Python com o Pip instalado
#com o Pip baixar a bilbioteca Pika para comunicação com RabbitMQ
pip install pika
#com o Pip baixar a bilbioteca Pika para comunicação com Redis
pip instal redis
#com o Pip baixar a bilbioteca minio para comunicação com MinIO
pip instal minio

#Containers do Docker
docker run --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management #RabbitMQ
docker run -it --rm --name redis-stack -d -p 6379:6379 -p 8001:8001 redis/redis-stack:latest #Redis
docker run -p 9000:9000 -p 9001:9001 quay.io/minio/minio server /data --console-address ":9001" #MinIO
