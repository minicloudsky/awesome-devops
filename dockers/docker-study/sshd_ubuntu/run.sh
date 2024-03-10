#!/bin/bash
/usr/sbin/sshd -D
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub > authorized_keys
