#!/usr/bin/python3
import cgi
print("content-type:text/html")
print()

from subprocess import getoutput
from subprocess import getstatusoutput

form = cgi.FieldStorage()
ch = form.getvalue("btn")
output=[0,'']
print("<pre>")

if ch == "createLG":
    vgname = form.getvalue("newVGName")
    print(vgname)
    getstatusoutput(f"sudo pvcreate {vgname}")
    diskName = form.getvalue("diskName")
    output=getstatusoutput(f"sudo vgcreate {vgname} {diskName}")
    print(output[1])

if ch == "createLV":
    vgname=form.getvalue('vgName')
    lvname=form.getvalue("newLvName")
    lvsize=form.getvalue("newSize")
    mountPath=form.getvalue("mountPath")
    print(mountPath)
    print(getoutput(f"sudo lvcreate -n {lvname} --size {lvsize} {vgname} ")[1])
    print(getoutput(f"sudo mkfs.ext4 /dev/{vgname}/{lvname}")[1])
    print(getoutput(f"sudo mkdir {mountPath}")[1])
    print(getoutput(f"sudo mount /dev/{vgname}/{lvname} {mountPath}")[1])
    print("*"*20,"Logical volume created and mounted successfully","*"*20)
    print(getoutput(f"sudo sudo lvdisplay")[1])

if ch == "modifyLV":
    vgname=form.getvalue("vgName")
    lvname=form.getvalue("lvName")
    newSize=form.getvalue("newSize")
    op=form.getvalue("lvOperation")
    print(op)
    if op == "reduce":
        mountPoint=getoutput(f"sudo findmnt -n -o TARGET /dev/{vgname}/{lvname}")
        getstatusoutput(f"sudo unmount /dev/{vgname}/{lvname}")
        getstatusoutput(f"sudo e2fsck -f -p /dev{vgname}/{lvname} ; sudo resize2fs /dev/{vgname}/{lvname}")
        getstatusoutput(f"sudo lvreduce -y -L {newSize} /dev/{vgname}/{lvname}")
        getstatusoutput(f"sudo mount /dev/{vgname}/{lvname} {mountPoint}") 
    
    if op == "extend":
        getstatusoutput(f"sudo lvextend -L {newSize} /dev/{vgname}/{lvname}")
        getstatusoutput(f"sudo resize2fs /dev/{vgname}/{lvname}")

if ch == "infoLvm":
    vgname=form.getvalue("vgName")
    print(getstatusoutput(f"sudo vgdisplay {vgname}")[1])

if ch == "delLvm":
    vgname=form.getvalue("vgName")
    print(getoutput(f"sudo vgchange -a -n {vgname}")[1])
    print(getoutput(f"sudo vgremove -y {vgname}")[1])

if ch == "lvInfo":
    vgname=form.getvalue("vgName")
    lvname=form.getvalue("lvName")
    print(getoutput(f"sudo lvdisplay {vgname}/{lvname}")[1])

if ch == "lvDel":
    vgname=form.getvalue("vgName")
    lvname=form.getvalue("lvName")
    print(getstatusoutput(f"sudo umount /dev/{vgname}/{lvname}")[1])
    print(getoutput(f"sudo lvremove -f /dev/{vgname}/{lvname}")[1])

if ch == "allDiskInfo":
    print(getstatusoutput("sudo fdisk -l")[1])

if ch == "allMountPointInfo":
    print(getstatusoutput("sudo df -h")[1])

if ch == "allVGinfo":
    print(getoutput("sudo vgdisplay"))
    
print("</pre>")