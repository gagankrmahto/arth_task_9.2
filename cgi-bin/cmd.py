#!/usr/bin/python3
import cgi
from subprocess import getoutput
print("content-type: text/html")
print()

print("The ouput of command")
form=cgi.FieldStorage()
command=form.getvalue("command")
print(command)

print("<pre>")
print(getoutput(command))
print("</pre>")
home="""

<div class="col-md-6">
    <a href="http://192.168.43.52/">Home</a>
  </div>



"""
print(home)