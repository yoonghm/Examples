# `gpiozero` - GPIO in Python for Raspberry Pi

`gpiozero` is Python 2 and 3 packages for Raspberry Pi.  

Example program

```python
from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

The official document could be downloaded from https://gpiozero.readthedocs.io/en/stable/index.html#

## Installation

It is not included in the Rasbian Stretch lite image.

<pre>
$ <b>python3 -c 'import gpiozero'</b>
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'gpiozero'
</pre>

It could be installed via `apt install`

<pre>
$ <b>sudo apt update</b>
Get:1 http://archive.raspberrypi.org/debian stretch InRelease [25.3 kB]
Get:2 http://mirrordirector.raspbian.org/raspbian stretch InRelease [15.0 kB]
Fetched 40.2 kB in 2s (15.1 kB/s)
Reading package lists... Done
Building dependency tree       
Reading state information... Done
93 packages can be upgraded. Run 'apt list --upgradable' to see them.
$ <b>sudo apt install python3-gpiozero</b>
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  python3-pkg-resources python3-rpi.gpio python3-spidev
Suggested packages:
  python-gpiozero-docs python3-setuptools python-spidev-doc
The following NEW packages will be installed:
  python3-gpiozero python3-pkg-resources python3-rpi.gpio python3-spidev
0 upgraded, 4 newly installed, 0 to remove and 93 not upgraded.
Need to get 266 kB of archives.
After this operation, 1,132 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.raspberrypi.org/debian stretch/main armhf python3-rpi.gpio armhf 0.6.3~stretch-1 [23.0 kB]
Get:2 http://mirror.nus.edu.sg/raspbian/raspbian stretch/main armhf python3-pkg-resources all 33.1.1-1 [137 kB]
Get:3 http://archive.raspberrypi.org/debian stretch/main armhf python3-spidev all 20170223~145721-1 [26.3 kB]
Get:4 http://archive.raspberrypi.org/debian stretch/main armhf python3-gpiozero all 1.4.1 [79.8 kB]
Fetched 266 kB in 4s (55.8 kB/s)            
Selecting previously unselected package python3-pkg-resources.
(Reading database ... 34443 files and directories currently installed.)
Preparing to unpack .../python3-pkg-resources_33.1.1-1_all.deb ...
Unpacking python3-pkg-resources (33.1.1-1) ...
Selecting previously unselected package python3-rpi.gpio.
Preparing to unpack .../python3-rpi.gpio_0.6.3~stretch-1_armhf.deb ...
Unpacking python3-rpi.gpio (0.6.3~stretch-1) ...
Selecting previously unselected package python3-spidev.
Preparing to unpack .../python3-spidev_20170223~145721-1_all.deb ...
Unpacking python3-spidev (20170223~145721-1) ...
Selecting previously unselected package python3-gpiozero.
Preparing to unpack .../python3-gpiozero_1.4.1_all.deb ...
Unpacking python3-gpiozero (1.4.1) ...
Setting up python3-rpi.gpio (0.6.3~stretch-1) ...
Setting up python3-spidev (20170223~145721-1) ...
Setting up python3-pkg-resources (33.1.1-1) ...
Processing triggers for man-db (2.7.6.1-2) ...
Setting up python3-gpiozero (1.4.1) ...
$ <b></b> 
<pre>
