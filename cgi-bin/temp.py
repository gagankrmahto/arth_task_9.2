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

print("<pre>")
print(installSoftwares)
print(nameNodeDir)
print(nameNodeIP)

print("="*20)

if nameNodeConfigIP not "None":
  if installSoftwares == "on":
    getoutput(f"sshpass -p '{nameNodePass}' scp jdk-8u171-linux-x64.rpm {nameNodeConfigIP}:/root")
    getoutput(f"sshpass -p '{nameNodePass}' scp hadoop-1.2.1-1.x86_64.rpm {nameNodeConfigIP}:/root")
    getoutput(f"sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} rpm -ivh /root/jdk-8u171-linux-x64.rpm")
    getoutput(f"sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")

  getoutput(f"mkdir {nameNodeDir}")
  hdfs = f'''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>{nameNodeDir}</value>\n</property>\n</configuration>'''
  core = f'''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{nameNodeConfigIP}:9001</value>\n</property>\n</configuration>'''        
  hdfs=hdfs.format(hdfs)
  core=core.format(core)
  f = open("core-site.xml",'w')
  f.write(core)
  f.close()

  f=open("hdfs-site.xml",'w')
  f.write(hdfs)
  f.close()

  getoutput(f"sshpass -p '{nameNodePass}' scp core-site.xml {nameNodeConfigIP}:/etc/hadoop/")
  getoutput(f"sshpass -p '{nameNodePass}' scp hdfs-site.xml {nameNodeConfigIP}:/etc/hadoop/")
  getoutput(f"sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} hadoop namenode  -format -force -nonInteractive")
  getoutput(f"sshpass -p '{nameNodePass}' ssh {nameNodeConfigIP} hadoop-daemon.sh start namenode")



if dataNodeConfigIP not "None":
  if installSoftwares == "on":
    getoutput(f"sshpass -p '{dataNodePass}' scp jdk-8u171-linux-x64.rpm {dataNodeConfigIP}:/root")
    getoutput(f"sshpass -p '{dataNodePass}' scp hadoop-1.2.1-1.x86_64.rpm {dataNodeConfigIP}:/root")
    getoutput(f"sshpass -p '{dataNodePass}' ssh {dataNodeConfigIP} rpm -ivh /root/jdk-8u171-linux-x64.rpm")
    getoutput(f"sshpass -p '{dataNodePass}' ssh {dataNodeConfigIP} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")

  getoutput(f"mkdir {dataNodeDir}")
  hdfs = f'''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>{dataNodeDir}</value>\n</property>\n</configuration>'''
  core = f'''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{nameNodeIP}:9001</value>\n</property>\n</configuration>'''        
  hdfs=hdfs.format(hdfs)
  core=core.format(core)
  f = open("core-site.xml",'w')
  f.write(core)
  f.close()

  f=open("hdfs-site.xml",'w')
  f.write(hdfs)
  f.close()

  getoutput(f"sshpass -p '{nameNodePass}' scp core-site.xml {nameNodeConfigIP}:/etc/hadoop/")
  getoutput(f"sshpass -p '{nameNodePass}' scp hdfs-site.xml {nameNodeConfigIP}:/etc/hadoop/")






home="""

<div class="col-md-6">
    <a href="http://192.168.43.52/">Home</a>
  </div>



"""
print(home)
print("</pre>")