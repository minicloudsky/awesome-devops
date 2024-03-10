FROM go:1.20 AS builder
LABEL maintainer="minicloudsky <minicloudsky@gmail.com>"
ENV TIME_ZONE=Asia/Shanghai
ENV GOROOT=/usr/local/go1.21
ENV CGO_ENABLED=0
ENV GOPROXY=https://goproxy.cn,direct
ENV GOARCH=amd64
ENV GO111MODULE=on
ENV GOOS=linux
ENV GOROOT=${GOROOT}
ENV PATH=${GOROOT}/bin:\${PATH}
ENV GOCACHE=/home/go/pkg/mod/go-build/build

WORKDIR /src

RUN GOPROXY=https://goproxy.cn GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go mod download && go build -o /src/main


FROM debian:stable-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates  \
        netbase \
        && rm -rf /var/lib/apt/lists/ \
        && apt-get autoremove -y && apt-get autoclean -y

COPY --from=builder /src/bin /app
ENV TIME_ZONE=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TIME_ZONE /etc/localtime && echo $TIME_ZONE > /etc/timezone
RUN mkdir -p /data/logs

ADD ./main /data/main
WORKDIR /data
ENTRYPOINT exec ./main