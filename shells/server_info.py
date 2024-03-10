# coding=utf8
from __future__ import absolute_import
import logging
import paramiko
#from utils.SSH import SSHClient

# 设置logger
handler = logging.FileHandler("log.txt")
logger = logging.getLogger()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)
logger.setLevel(logging.DEBUG)


class ServerConfig(object):
    def __init__(self, ip, user, pwd, port=22):
        self.ip = ip
        self.user = user
        self.pwd = pwd
        self.port = port
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    """
    #获取cpu使用率
    cpuUsage=`top -n 1 | awk -F '[ %]+' 'NR==3 {print $2}'`
    #获取磁盘使用率
    data_name="/dev/sda1"
    diskUsage=`df -h | grep $data_name | awk -F '[ %]+' '{print $5}'`
    logFile=/tmp/jiankong.log
    #获取内存情况
    mem_total=`free -m | awk -F '[ :]+' 'NR==2{print $2}'`
    mem_used=`free -m | awk -F '[ :]+' 'NR==3{print $3}'`
    #统计内存使用率
    mem_used_persent=`awk 'BEGIN{printf "%.0f\n",('$mem_used'/'$mem_total')*100}'`
    """

    def get_cpu_status(self):
        cmd = "export TERM=dumb; top -b -n 1 | awk -F '[ %]+' 'NR==3 {print $1}'"
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        result = stdout.read()
        result = result.strip()
        if isinstance(result, bytes):
            result = result.decode("utf-8")
        logger.info("server cpu: %s" % (result.strip()))
        return result

    def get_disk_status(self):
        disk_name = '/dev/sda1'
        cmd = "df -h | grep %s | awk -F '[ %%]+' '{print $5}'" % (disk_name)
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        result = stdout.read()
        result = result.strip()
        if isinstance(result, bytes):
            result = result.decode("utf-8")
        logger.info("server disk: %s" % (result.strip()))
        return result

    def get_memory_status(self):
        """
        mem_total=`free -m | awk -F '[ :]+' 'NR==2{print $2}'`;
        mem_used=`free -m | awk -F '[ :]+' 'NR==2{print $3}'`;
        awk 'BEGIN{printf "%.0f\n",('$mem_used'/'$mem_total')*100}'
        """
        cmd = """
        free -m | awk -F '[ :]+' 'NR==2{print $2}'
        """
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        result = stdout.read()
        result = result.strip()
        if isinstance(result, bytes):
            result = result.decode("utf-8")
        cmd2 = """
        free -m | awk -F '[ :]+' 'NR==2{print $3}'
        """
        stdin, stdout, stderr = self.ssh.exec_command(cmd2)
        result2 = stdout.read()
        result2 = result2.strip()
        if isinstance(result2, bytes):
            result2 = result2.decode("utf-8")
        logger.info("server memory: %s, %s" % (result, result2))
        return result, result2

    def get_server_status(self):
        self.ssh.connect(hostname=self.ip, port=self.port,
                         username=self.user, password=self.pwd)
        cpu = self.get_cpu_status()
        # print(cpu)
        memory = self.get_memory_status()
        disk = self.get_disk_status()
        self.ssh.close()
        result = {
            "cpu": 0,
            "disk": 0,
            "memory": 0
        }
        try:
            return {
                "cpu": float(cpu),
                "disk": round(float(disk), 2),
                "memory": round(float((float(memory[1])/float(memory[0]))*100), 2)
            }
        except Exception as e:
            logger.error(str(e), exc_info=1)
            return result


if __name__ == '__main__':
    """
    "host":"",
    "port":22,
    "username":"",
    "password":"."
    """
    Server = ServerConfig("", "", "", 22)
    result = Server.get_server_status()
    print(result)
