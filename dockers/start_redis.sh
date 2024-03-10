#!/bin/bash
docker pull redis
docker run -it   -p 6379:6379 -v /home/container/redis/data/:/data --name redis -d redis redis-server --appendonly yes 
