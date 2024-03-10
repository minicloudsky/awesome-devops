#/usr/bin/bash
echo "start install Python-3.8.5"
yum -y install wget
cd ~
wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tar.xz
yes | sudo yum-builddep python
tar -zxvf Python-3.8.5.tgz
cp -r Python-3.8.5 /usr/local
cd /usr/local/Python-3.8.5
./configure
make
sudo make install
echo "complete install Python-3.8.5"
rm -rf ~/Python-3.8.5
rm -rf ~/Python-3.8.5.tar.xz
echo "cleaned python package."
