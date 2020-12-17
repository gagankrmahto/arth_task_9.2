#!/usr/bin/python3
import cgi
from subprocess import getoutput
from subprocess import getstatusoutput
print("content-type:text/html")
print()
form=cgi.FieldStorage()

print("<pre>")
btn = form.getvalue('btn')
if btn == "awsConfig":
    print(getstatusoutput("{ echo "+f"{form.getvalue('awsID')}; echo {form.getvalue('awsKey')}; echo {form.getvalue('awsRegion')}; echo {form.getvalue('awsOutput')};"+" } | aws configure "))
if btn == "launchInstance":
    tags = "{Key=Name,Value="+f"{form.getvalue('osName')}"+"}"
    print(getoutput(f"aws ec2 run-instances --image-id {form.getvalue('amiID')} --instance-type {form.getvalue('osType')} --key-name {form.getvalue('keyName')} --security-group-ids {form.getvalue('securityGroup')} --tag-specifications 'ResourceType=instance,Tags=[{tags}]'"))

if btn == "createKeyButton":
    print(getoutput(f'aws ec2 create-key-pair --key-name {form.getvalue("createKeyName")}'))

if btn == "descKeyPair":
    print(getoutput(f"aws ec2 describe-key-pairs --key-name {form.getvalue('createKeyName')}"))

if btn == "createSG":
    print(getoutput(f'aws ec2 create-security-group --group-name {form.getvalue("createSecurityGroup")} --description {form.getvalue("createSecurityGroupDesc")}'))

if btn =="showSG":
    print(getoutput(f"aws ec2 describe-security-groups"))

if btn =="addInboundRules":
    print(getoutput(f"aws ec2 authorize-security-group-ingress --group-name {form.getvalue('addInboundRules')} --protocol {form.getvalue('addInboundRulesProtocol')} --port {form.getvalue('addInboundRulesPort')} --cidr {form.getvalue('addInboundRulesIPRange')}"))

if btn == "newEBS":
    print(getoutput(f"aws ec2 create-volume --availabilty-zone {form.getvalue('createNewEbsAZ')} --size {form.getvalue('createNewEbsSize')}"))

if btn == "attachEBS":
    print(getoutput(f"aws ec2 attach-volume --instance-id {form.getvalue('attachEbsID')} --volume-id {'attachEbsVolId'} --device {form.getvalue('attachNewEbsDevName')}"))


print("</pre>")







