from ppadb.client import Client
import numpy as np
import time
import subprocess
import os


subprocess.run('adb start-server', stdout=subprocess.PIPE, shell=True)
x = 650
y = 350

client = Client(host='127.0.0.1' , port=5037)
client.remote_connect('127.0.0.1', 5725)
devices = client.devices()

#device = client.device("127.0.0.1:5725")
device = devices[0]
print (device)

device.shell(f'input touchscreen tap {int(x)} {int(y)}')
time.sleep(30)
#subprocess.run("adb kill-server", stdout=subprocess.PIPE, shell=True)