# Unix Tips and Trics

## Find the top-10 largest files

<pre>
<b>$ sudo du -a / | sort -n -r | head -n 10</b>
7826444	/
3216280	/usr
3098852	/home
3098848	/home/spsy
2408640	/home/spsy/anaconda3
2178012	/home/spsy/anaconda3/pkgs
1539352	/usr/lib
1265372	/usr/share
838608	/var
731096	/usr/lib/x86_64-linux-gnu
</pre>
