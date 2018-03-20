# Unix Tips and Trics

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
