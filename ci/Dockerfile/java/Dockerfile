FROM openjdk20:latest

LABEL maintainer="minicloudsky <minicloudsky@gmail.com>"

ENV PROJECT_NAME=user-service
ENV JAVA_OPTS="-Xmx2g -XX:+UseG1GC -Djava.awt.headless=true"
ENV JAVA_HOME=/user/local/java
ENV START_COMMAND="xxx"
ENV PROJECT_DIR=/data/my-service

WORKDIR $PROJECT_DIR

RUN mvn -Dmaven.test.skip=true clean package -U -DoutputDirectory=$PROJECT_DIR

ADD ./$PROJECT_NAME.jar /data/$PROJECT_NAME.jar
WORKDIR /data
ENTRYPOINT exec java -server -jar $JAVA_OPTS $START_COMMAND /data/$PROJECT_NAME.jar
