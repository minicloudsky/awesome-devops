FROM golang:1.9 as builder
RUN mkdir -p /go/src/test
WORKDIR /go/src/test
COPY main.go .
RUN CGO_ENABLED=0 GOOS=linux go build -o app .

FROM alpine:latest as minicloudsky-go-image
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /go/src/test/app . 
CMD ["./app"]

FROM python:3 as python-env
RUN mkdir -p /code/python
WORKDIR /code/python
COPY main.py .
RUN python3 main.py
