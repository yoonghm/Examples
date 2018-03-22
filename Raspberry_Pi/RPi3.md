# Raspberry Pi 3 (RPi3)

## Create a Bootable Headless Raspbian OS on a microSD Card (>8 GB)

### Download the Latest Raspbian OS Lite

The latest Raspbian OS could be download from [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/).

As of 2018 March, the latest Raspbian OS is Stretch.

### Flash Raspbian OS on a microSD Card (> 8GB)

Use any suitable flashing tools such as [Etcher](https://etcher.io/)

Re-insert the microSD card into your computer.  You should be to see a new drive labelled `boot`.

## Configuration Before First Boot

### Enable SSH within RPi3

Create an empty file `ssh` in the root directory of the microSD card.

### Configure WiFi

Create `wpa_supplicant.conf` in the root directory of the microSD card.
You may use the template below.

```
# File: /etc/wpa_supplicant/wpa_supplicant.conf

###
### Do not allow wpa_cli or wpa_gui to update it
###
update_config=0

###
### Directory for UNIX domain sockets and access control
###
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev


#######################################################################
# Home
#######################################################################

network={
  ssid="my_ssid"
  psk="my_passphrase"
  ## psk is in plain text and should be encrypted
  ## Use wpa_passphrase "ssid" "psk" to generate long psk
  ##   wpa_passphrase my_ssid my_passphase
  psk=long_hashed_psk_using_wpa_passphrase_on_ssid_and_passphrase
  key_mgmt=WPA-PSK
  priority=99
  id_str="home"
}

#######################################################################
# NPWirelessx
#######################################################################
network={
  ssid="NPWirelessx"
  key_mgmt=WPA-EAP
  eap=PEAP
  identity="user_id"
  # password="secret_password"
  password=hash:7da534016188e561da0546d3e8bf04de
  # Use md4 to hash password which is in plaintext
  #   echo 'your_plaintext_password' | iconv -t utf16le | openssl md4 | awk '{print $2}'
  phase1="peaplabel=0"
  phase2="auth=MSCHAPV2"
  priority=0
  id_str="work"
}

# Hashed password is obtained via
# echo 'your_plaintext_password' | iconv -t utf16le | openssl md4 | awk '{print $2}'
#
# You can do it via vi by putting the cursor after "hash:"
# :r !echo -n 'your_plaintext_password' | iconv -t utf16le | openssl md4 | awk '{print $2}'
#
# Restart your networking
# sudo service networking restart
```

## Boot RPi3

Insert the configured bootable microSD card into RPi3 and power it up.

The following information may be helpful for you to find your raspberrypi

- Hostname is `raspberrypi`
- MAC address has `b8:27:eb` prefix.

You may use `arp -a` to scan MAC addresses.

## Setup a Linux box hosted in a virtual machine from your computer

Use "Bridged Adapter" for the network adapter.  Take note of the IP address of the Linux.
Assume Linux box's IP address is **192.168.1.10**.

Create a file named `flask_web.py`

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!\n'

if __name__ == "__name__":
  app.run()
```

Run the flask web server:

<pre>
$ <b>FLASK_APP=flask_web.py flask run -h 0.0.0.0</b>
 * Serving Flask app "flask_web"
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
</pre>

If you use `flask` in Microsoft Windows, use the following command
<pre>
C:\><b>set FLASK_APP=flask_web.py</b>
C:\><b>flask run</b>
</pre>

## Configuration After First Boot

Login from the Linux box to RPi3 using `ssh`.  Assume RPi3's address is **192.168.1.9**

<pre>
$ <b>ssh pi@192.168.1.9</b>
</pre>

Make the following changes:

###  `sudo raspi-config`

- Change password for user `pi`
- Enable one-wire interface
- Change hostname to a unique and better name
- Expand filesystem to use all microSD card storage

### Change keyboard layout in `/etc/default/keyboard` from `"gb"` to `"us"`

After this changes, `ALT+F1` ... `ALT+F12` give you additional 11 terminal sessions.

### Set timezone to `Asia/Singapore`

<pre>
$ <b>sudo timedatectl set-timezone Asia/Singapore</b>
</pre>

### Set time synchronization server

Edit `/etc/systemd/timesyncd.conf`

```
#NP’s NTP server: 153.20.80.88 153
#time.windows.com: 52.163.118.68
NTP=153.20.80.88 153.20.81.88
FallbackNTP=52.163.118.68
```

### Update Raspbian, Install Necessary Pacakges and Clean Up Obsolete Packages

<pre>
$ <b>sudo apt update</b>
$ <b>sudo apt upgrade</b>
$ <b>sudo apt install python3-gpiozero festival
$ <b>sudo apt clean</b>
$ <b>sudo apt autoremove<b>
</pre>

### Raspberry Pi speaks outs its IP address using festival

Festival is a general purpose text-to-speech system. Raspberry Pi 3 has an audio output which could be used to output the audio.

Using your favourite text editor, add the following line before `fi` in `/etc/rc.local` script

```bash
hostname -I | /usr/bin/festival --tts
```

Alternatively used `sed` to change it:

```bash
sudo sed -i '
/^fi/i \
  /bin/hostname -I | /usr/bin/festival --tts' \
rc.local
```

### Test a http connection to the flask web server setup earlier

<pre>
$ <b>curl 192.168.1.10:5000</b>
</pre>

The terminal that run the flask web server shuld should you a new message:

```
192.168.1.9 - - [21/Mar/2018 01:48:43] "GET / HTTP/1.1" 200 -
```

It shows that they are connected.

### Create a startup script `/etc/init.d/inform_other.sh`

The script informs RPi3's IP address to the flask web server. The file should be owned by root and has its executable bits enable.


```bash
#! /bin/sh

### BEGIN INIT INFO
# Provides:          YoongHM
# Required-Start:    $local_fs $remote_fs $network $syslog
# Required-Stop:     $local_fs $remote_fs $network $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Inform other about my IP address obtained via DHCP
# Description: Inform other about my IP address obtained via DHCP
### END INIT INFO

# The IP address should be permanent to make the solution better
URL="192.168.1.10:5000"

/usr/bin/curl $URL/`/bin/hostname` --connect-timeout 20 --max-time 20 > /dev/null 2>&1

exit 0
```

<pre>
$ <b>sudo chmod a+x /etc/init.d/inform_other.sh</b>
$ <b>sudo update-rc.d inform_other.sh defaults</b>
</pre>

### Reboot

<pre>
$ <b>sudo reboot now</b>
</pre>
