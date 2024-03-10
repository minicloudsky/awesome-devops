FROM nginx:latest

# env enum test,uat,prod
ENV CURRENT_ENV=prod
ENV PROJECT_DIR=/src
ENV WORKDIR=/src
ENV NGINX_CONF=prod_nginx.conf

RUN export NODE_OPTIONS="--max-old-space-size=8192" && yarn config set registry https://registry.npmmirror.com && npm config set registry https://registry.npmmirror.com
RUN yarn && yarn run build
RUN npm install && npm run build:$CURRENT_ENV
RUN cp -rf dist/ config/ $WORKDIR

RUN mkdir -p /data/logs

ADD dist/ /data

COPY config/$NGINX_CONF /etc/nginx/nginx.conf

WORKDIR /data