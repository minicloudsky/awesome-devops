# set base image
FROM ubuntu:18.04
# author info
MAINTAINER minicloudsky
# install sshd service
RUN apt-get update
RUN apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd
RUN mkdir -p /root/.ssh

# cancel pam limit
RUN sed -ri 's/session required pam_loginuid.so/#session required pam_loginuid.so/g' /etc/pam.d/sshd
# copy file
ADD authorized_keys /root/.ssh/authorized_keys
ADD run.sh /run.sh
RUN chmod 755 /run.sh
# open port
EXPOSE 22
# set auto start
CMD ["/run.sh"]

