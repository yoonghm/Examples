# Unix Tips and Tricks

## Find the top-10 largest directories

<pre>
<b>$ sudo du -hs * 2>/dev/null | sort -rh | head -5</b>
3.1G	usr
3.0G	home
819M	var
517M	lib
66M	boot
</pre>

## Find the top-10 largest files
<pre
<b>$ sudo find / -type f -exec du -Sh {} + 2>/dev/null | sort -rh | head -5</b>
93M	/usr/lib/firefox/libxul.so
80M	/usr/share/code/code
73M	/usr/lib/thunderbird/libxul.so
71M	/home/spsy/anaconda3/pkgs/mkl-2018.0.1-h19d6760_4/lib/libmkl_avx512_mic.so
71M	/home/spsy/anaconda3/lib/libmkl_avx512_mic.so
</pre>

## Reduce swap partition in `/dev/sda5`

<pre>
<b>$ sudo swapoff /dev/sda5</b>
<b>$ # Split /dev/sda5 into 2 partition, say /dev/sda5 and /dev/sda6</b>
<b>$ # Mark /dev/sda5 as swap partition</b>
<b>$ sudo mkswap /dev/sda5</b>
<b>$ sudo swapon /dev/sda5</b>
<b>$ sudo mkfs ext4 /dev/sda6</b>
<b>$ # Update /etc/fstab for /dev/sda6</b>
</pre>
