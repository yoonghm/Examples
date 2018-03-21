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
