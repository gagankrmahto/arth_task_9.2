#!/usr/bin/python3
print("content-type:text/html")
print()

from subprocess import getoutput
from subprocess import getstatusoutput
import cgi

form = cgi.FieldStorage()
btn = form.getvalue("btn")
print(btn)
print("<pre>")
if btn == "installDocker":
    repo_conf = """
[docker]
baseurl = https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0
    """
    getoutput("sudo touch docker.repo")
    getoutput("sudo chown apache docker.repo")
    getoutput("sudo chmod +rwx docker.repo")
    f = open("docker.repo","w")
    f.write(repo_conf)
    print(repo_conf)
    f.close()
    getoutput("sudo cp docker.repo /etc/yum.repos.d/docker.repo")
    print(getoutput("sudo dnf install docker-ce --nobest -y"))
    print(getoutput("sudo systemctl start docker"))
    print("<h2<br>#### Started Docker Services ####</h2><br>")

if btn == "enableDocker":
    print(getoutput("sudo systemctl enable docker"))
    print("Services are permanent now ")

if btn == "dockerStatus":
    print(getoutput('sudo systemctl status docker'))

if btn == "dockerImages":
    print(getoutput("sudo docker images"))

if btn == "dockerContainers":
    print(getoutput("sudo docker ps -a"))

if btn == "dockerRunningContainers":
    print(getoutput("sudo docker ps"))

if btn == "pullImages":
    print(getoutput(f"sudo docker pull {form.getvalue('pullImageName')}:{form.getvalue('version')}"))

if btn == "launchContainer":
    print(getoutput(f"sudo docker run -dit --name {form.getvalue('launchImageContName')} {form.getvalue('launchImageName')}:latest"))

if btn == "createImage":
    img_tag = form.getvalue("newTagName")
    if img_tag is not "None":
        pass
    else:
        newTagName = "latest"
    print(getoutput(f'sudo docker commit {form.getvalue("contName")} {form.getvalue("laucnImageName")}:latest'))
if btn == "startContainer":
    print(getoutput(f"sudo docker start {form.getvalue('startContainer')}"))

if btn == "stopContainer":
    print(getoutput(f"sudo docker stop {form.getvalue('stopContainer')}"))


if btn == "remImage":
    if form.getvalue("delImage") == "all":
        print(getoutput("sudo docker rmi `docker images -a -q`"))
    else:
        print(getoutput(f"sudo docker rmi {form.getvalue('delImage')}:latest"))
    
if btn == "remContainer":
    if form.getvalue("remContName") == "all":
        print(getoutput("sudo docker rm `docker ps -a -q`"))
    else:
        print(getoutput(f"sudo docker rm {form.getvalue('remContName')}"))
    



