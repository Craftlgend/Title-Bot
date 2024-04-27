from ppadb.client import Client
import numpy
import time
import subprocess
import os

subprocess.run('adb start-server', stdout=subprocess.PIPE, shell=True)


client = Client(host='127.0.0.1' , port=5037)
client.remote_connect('127.0.0.1', 5725)
devices = client.devices()

#device = client.device("127.0.0.1:5725")
device = devices[0]
print (device)

device.shell('input touchscreen swipe 200 400 500 600')
time.sleep(10)
subprocess.run("adb kill-server", stdout=subprocess.PIPE, shell=True)