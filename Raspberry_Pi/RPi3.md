# Raspberry Pi 3 (RPi3)

## Create a Bootable Headless Raspbian OS on a microSD Card (>8 GB)

### Download the Latest Raspbian OS Lite

The latest Raspbian OS could be download from [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/).

As of 2018 March, the latest Raspbian OS is Stretch.

We will use the **Lite** edition as we do not need graphical interface.

### Flash Raspbian OS on a microSD Card (> 8GB)

Use any suitable flashing tools such as [Etcher](https://etcher.io/)

Re-insert the microSD card into your computer.  You should be to see a new drive labelled `boot`.

Let's make changes to the contents within microSD card
1.  Create an empty file `ssh` in the root directory of the microSD card. This enables SSH so that we can remotely login to the RPi3 using SSH protocol.

1.  Create `wpa_supplicant.conf` in the root (`/`) directory of the microSD card.

```
update_config=0
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev

# The configuration below is for WPA/WPA2 Personal WiFi network
# You may encrypt the psk field (in double quotation) with wpa_passphrase
#   1. Comment out psk with '#' in front of psk
#   2. Generate encrypted psk on your unquoted ssid and psk values using wpa_passphase
#        wpa_passphase my_ssid my_passphrase
#   3. Copy the generated encrypted passphrase into psk. Do not enclosure it with double quotation
network={
  ssid="my_ssid"  # Replace it with your ssid
  #psk="my_passphrase"  # Replace it with your passphrase
  psk=07dc9a98201ab213131c3d2e6361628317317391391893193219  # Replace this value with encrypted passphrase
  key_mgmt=WPA-PSK
  priority=99    # Optional configuration: Lower value takes precedence
  id_str="home"  # Optional string to identify the network configuration
}

# The configuration below is for WPA2 Enterprise WiFi network for NPWirelessx
# You may encrypt the password field (in double quotation) with md4
#   1. Comment out password with '#' in front of password
#   2. Generate MD4 hashed password using the following command
#     echo -n 'secret_password' | iconv -t utf16le | openssl md4   
#   3. Copy encrypted password into password after 'hash:'. Do not enclosure it with double quotation
network={
  ssid="NPWirelessx"
  key_mgmt=WPA-EAP
  eap=PEAP
  identity="user_id"  # Replace it with your user id
  # password="secret_password"
  password=hash:7da534016188e561da0546d3e8bf04dead213  # Replace this value with MD4 encrypted password
  phase1="peaplabel=0"
  phase2="auth=MSCHAPV2"
  priority=0     # Optional configuration: Lower value takes precedence
  id_str="work"  # Optional string to identify the network configuration
}
```

This file will be copied to `/etc/wpa_supplicant/wpa_supplicant.conf` in the next bootup

**Note:** If the RPi3 is booted, you can change the file directly in `/etc/wpa_supplicant/wpa_supplicant.conf`.
You can restart the networking using the following commands

$ <b>sudo service networking restart</b>

## Boot RPi3

Insert the configured bootable microSD card into RPi3.

Connect USB keyboard and HDMI monitor to RPi3.

Power it up.

The IP address will be shown on the console or heard from audio output via a speaker or a pair of ear piece.

The following information may be helpful for you to find your raspberrypi in your network:
- Hostname is `raspberrypi`
- You may use `arp -a` to scan connected WiFi devices with MAC addresses begins with 'b8:27:eb`

## Configuration After First Boot

Login to the RPi3 using the keyboard and monitor with the following information

**User:** pi
**Password:** raspberry

If the network is properly configured, you may use SSH to login to the RPI3. Assume RPi3's address is **192.168.1.9**

<pre>
$ <b>ssh pi@192.168.1.9</b>
</pre>

Using `sudo raspi-config` to make the following changes:
- Change password for user `pi`
- Enable one-wire interface
- Change hostname to a unique and better name
- Change timezone to `Asia/Singapore`
- Change keyboard layout to "Generic 101-key PC" and then "English (US)" and then "The default for the keyboard input"
- Expand filesystem to use all microSD card storage

### Set time synchronization server

We do not need fake-hwclock from the distribution, we can delete it to save space:
<pre>
$ <b>sudo systemctl stop fake-hwclock</b>
$ <b>sudo apt-get -y remove fake-hwclock</b>
$ <b>sudo apt-get -y purge fake-hwclock</b>
</pre>

Edit `/etc/systemd/timesyncd.conf`

```
#153.20.80.88 153.20.81.88 are NP's NTP servers
NTP=153.20.80.88 153.20.81.88 0.debian.pool.ntp.org 1.debian.pool.ntp.org 2.debian.pool.ntp.org 3.debian.pool.ntp.org
FallbackNTP=0.debian.pool.ntp.org 1.debian.pool.ntp.org 2.debian.pool.ntp.org 3.debian.pool.ntp.org
```

To re-run `systemd-timesyncd`

<pre>
$ <b>sudo sudo systemctl restart systemd-timesyncd</b>
$ <b>sudo sudo systemctl daemon-reload</b>
</pre>

Check the time status 

<pre>
$ <b>timedatectl status</b>
      Local time: Fri 2018-03-30 11:34:32 +08
  Universal time: Fri 2018-03-30 03:34:32 UTC
        RTC time: n/a
       Time zone: Asia/Singapore (+08, +0800)
 Network time on: yes
NTP synchronized: yes
 RTC in local TZ: no
</pre>

The above output shows that network time is on and is syhchronized.  There is no real-time clock with RPi3.

### Update Raspbian, Install Necessary Pacakges and Clean Up Obsolete Packages

<pre>
$ <b>sudo apt update</b>
$ <b>sudo apt upgrade</b>
$ <b>sudo apt install python3-gpiozero festival</b>
$ <b>sudo apt clean</b>
$ <b>sudo apt autoremove</b>
</pre>

### Raspberry Pi speaks outs its IP address using festival

Festival is a general purpose text-to-speech system. Raspberry Pi 3 has an audio output which could be used to output the audio.

Using your favourite text editor, add the following line before `fi` in `/etc/rc.local` script

<pre>
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.
#
# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
<b>  /bin/hostname -I | /usr/bin/festival --tts</b>
fi

exit 0
</pre>

Alternatively used `sed` to change it:

<pre>
$ <b>sudo sed -i '</b>
><b> /^fi/i \</b>
><b>  /bin/hostname -I | /usr/bin/festival --tts' \</b>
><b>rc.local</b>
</pre>

ou can use `iwconfig` to find out WiFi network used by your RPi3.

### Reboot

<pre>
$ <b>sudo reboot now</b>
</pre>
