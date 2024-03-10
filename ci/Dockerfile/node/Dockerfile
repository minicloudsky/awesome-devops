FROM node:16

LABEL maintainer="minicloudsky <minicloudsky@gmail.com>"

ENV LD_LIBRARY_PATH /usr/local/lib

RUN mkdir -p /src/node
ADD ./data /data/node/
WORKDIR /data/node/
RUN npm config set registry https://registry.npmmirror.com && npm config set disturl https://npm.taobao.org/mirrors/node/  && npm ci

ENTRYPOINT exec npm start