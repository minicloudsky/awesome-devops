#!/bin/bash
echo "start pull elasticsearch  and kibana image "

nohup docker pull docker.elastic.co/elasticsearch/elasticsearch:7.9.0 &
docker run -it --name elasticsearch  -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -d  docker.elastic.co/elasticsearch/elasticsearch:7.9.0

nohup docker pull docker.elastic.co/kibana/kibana:7.9.0 &
docker run -it --name kibana  --link `docker ps -a| grep elasticsearch | awk '{print $1}' `:elasticsearch -p 5601:5601 -d  docker.elastic.co/kibana/kibana:7.9.0
echo "deploy es and kibana container completed."
