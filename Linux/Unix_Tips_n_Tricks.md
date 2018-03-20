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
<b>$ sudo find -type f -exec du -Sh {} + | sort -rh | head -5</b>
552M	./Downloads/Anaconda3-5.1.0-Linux-x86_64.sh
71M	./anaconda3/pkgs/mkl-2018.0.1-h19d6760_4/lib/libmkl_avx512_mic.so
71M	./anaconda3/lib/libmkl_avx512_mic.so
63M	./anaconda3/pkgs/mkl-2018.0.1-h19d6760_4/lib/libmkl_avx512.so
63M	./anaconda3/lib/libmkl_avx512.so
</pre>
