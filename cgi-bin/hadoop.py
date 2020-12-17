#!/usr/bin/python3
import cgi
from subprocess import getoutput
print("content-type:text/html")
print()

print("This is the page for all the hadoop related works")

form = cgi.FieldStorage()
installSoftwares = form.getvalue("hadoopInstall")
nameNodeIP = form.getvalue("nameNodeIP")
# Namenode
nameNodeConfigIP = form.getvalue("nameNodeConfigIP")
nameNodePass = form.getvalue("nameNodePass")
nameNodeDir = form.getvalue("nameNodeDir")
# DataNode
dataNodeIP = form.getvalue("dataNodeIP")
dataNodeDir = form.getvalue("dataNodeDir")

print(form)


if nameNodeConfigIP is not "None":
  if installSoftwares == "on":
    print("installation started")
    getoutput(f"sudo sshpass -p '{nameNodePass}' scp /var/www/cgi-bin/jdk-8u171-linux-x64.rpm {nameNodeConfigIP}:/root")
    getoutput(f"sudo sshpass -p '{nameNodePass}' scp /var/www/cgi-bin/hadoop-1.2.1-1.x86_64.rpm {nameNodeConfigIP}:/root")
    getoutput(f"sudo sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} rpm -ivh /root/jdk-8u171-linux-x64.rpm")
    getoutput(f"sudo sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")

  getoutput(f"sudo sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} mkdir /{nameNodeDir}")
  hdfs = f'''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/{nameNodeDir}</value>\n</property>\n</configuration>'''
  core = f'''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{nameNodeConfigIP}:9001</value>\n</property>\n</configuration>'''        
  print("<pre>")
  print("this is hdfs iste",hdfs)
  hdfs=hdfs.format(hdfs)
  core=core.format(core)

  getoutput("sudo chmod +rwx /var/www/cgi-bin")        
  getoutput("sudo chmod +rwx /var/www/cgi-bin/hdfs-site.xml")
  getoutput("sudo chmod +rwx /var/www/cgi-bin/core-site.xml")
  getoutput("sudo chown apache /var/www/cgi-bin/hdfs-site.xml")
  getoutput("sudo chown apache /var/www/cgi-bin/core-site.xml")

  f = open("/var/www/cgi-bin/core-site.xml",'w')
  print(core)
  f.write(core)
  f.close()

  f=open("/var/www/cgi-bin/hdfs-site.xml",'w')
  f.write(hdfs)
  f.close()
  print("hiii now we will configure namenode")
  getoutput(f"sudo sshpass -p '{nameNodePass}' scp /var/www/cgi-bin/core-site.xml {nameNodeConfigIP}:/etc/hadoop/")
  getoutput(f"sudo sshpass -p '{nameNodePass}' scp /var/www/cgi-bin/hdfs-site.xml {nameNodeConfigIP}:/etc/hadoop/")
  getoutput(f"sudo sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} hadoop namenode  -format -force -nonInteractive")
  getoutput(f"sudo sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} hadoop-daemon.sh start namenode")


if nameNodeConfigIP is not "None":
  if installSoftwares == "on":
    print("installation started")
    getoutput(f"sudo sshpass -p '{nameNodePass}' scp /var/www/cgi-bin/jdk-8u171-linux-x64.rpm {nameNodeConfigIP}:/root")
    getoutput(f"sudo sshpass -p '{nameNodePass}' scp /var/www/cgi-bin/hadoop-1.2.1-1.x86_64.rpm {nameNodeConfigIP}:/root")
    getoutput(f"sudo sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} rpm -ivh /root/jdk-8u171-linux-x64.rpm")
    getoutput(f"sudo sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")

  getoutput(f"sudo sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} mkdir /{nameNodeDir}")
  hdfs = f'''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/{nameNodeDir}</value>\n</property>\n</configuration>'''
  core = f'''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{nameNodeConfigIP}:9001</value>\n</property>\n</configuration>'''        
  print("<pre>")
  print("this is hdfs iste",hdfs)
  hdfs=hdfs.format(hdfs)
  core=core.format(core)

  getoutput("sudo chmod +rwx /var/www/cgi-bin")        
  getoutput("sudo chmod +rwx /var/www/cgi-bin/hdfs-site.xml")
  getoutput("sudo chmod +rwx /var/www/cgi-bin/core-site.xml")
  getoutput("sudo chown apache /var/www/cgi-bin/hdfs-site.xml")
  getoutput("sudo chown apache /var/www/cgi-bin/core-site.xml")

  f = open("/var/www/cgi-bin/core-site.xml",'w')
  print(core)
  f.write(core)
  f.close()

  f=open("/var/www/cgi-bin/hdfs-site.xml",'w')
  f.write(hdfs)
  f.close()
  print("hiii now we will configure namenode")
  getoutput(f"sudo sshpass -p '{nameNodePass}' scp /var/www/cgi-bin/core-site.xml {nameNodeConfigIP}:/etc/hadoop/")
  getoutput(f"sudo sshpass -p '{nameNodePass}' scp /var/www/cgi-bin/hdfs-site.xml {nameNodeConfigIP}:/etc/hadoop/")
  getoutput(f"sudo sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} hadoop namenode  -format -force -nonInteractive")
  getoutput(f"sudo sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} hadoop-daemon.sh start namenode")

home="""

<div class="col-md-6">
    <a href="http://192.168.43.52/">Home</a>
  </div>



"""
print(home)
print("</pre>")