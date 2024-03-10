#!/bin/bash
echo "start install nodejs-14.9.0"
wget https://nodejs.org/dist/v14.9.0/node-v14.9.0-linux-x64.tar.xz
tar -zxvf node-v14.9.0-linux-x64.tar.xz
mv  node-v14.9.0-linux-x64 /usr/local
cd /usr/local/
mv node-v14.9.0-linux-x64 node-v14.9.0
cd node-v14.9.0
echo "export PATH=$PATH:/usr/local/node-v14.9.0/bin" >> /etc/profile
source /etc/profile
ln -s /usr/local/node-v14.9.0/bin/npm /usr/local/bin/
ln -s /usr/local/node-v14.9.0/bin/node /usr/local/bin/
node -v
npm -v
echo "install nodejs completed ."

