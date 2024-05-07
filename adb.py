from ppadb.client import Client
import subprocess


subprocess.run('adb start-server', stdout=subprocess.PIPE, shell=True)

client = Client(host='127.0.0.1' , port=5037)
client.remote_connect('127.0.0.1', 5555)
devices = client.devices()

#device = client.device("127.0.0.1:5725")
device = devices[0]
print (device)

def tap(x, y):
    device.shell(f'input touchscreen tap {int(x)} {int(y)}')


def input(str):
    device.shell(f'input text "{str}"')


def screenshot():
    subprocess.run('adb exec-out screencap -p > screenshot.png', stdout=subprocess.PIPE, shell=True)
    


def stop():
    subprocess.run("adb kill-server", stdout=subprocess.PIPE, shell=True)