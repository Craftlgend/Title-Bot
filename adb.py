from ppadb.client import Client
import numpy
import time
import subprocess
import os

subprocess.run('adb start-server', stdout=subprocess.PIPE, shell=True)


adb = Client(host='127.0.0.1' , port=5037)
adb.remote_connect('127.0.0.1', 5725)

device = adb.device("127.0.0.1:5725")
print (device)


subprocess.run("adb kill-server", stdout=subprocess.PIPE, shell=True)