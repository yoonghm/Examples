# bash Shell

Every operating system has at least one or more applications to allow user to interact with itself:

- Graphical user interface applications such as Windows Explorer in Microsoft Windows, Machintosh Finder in Machitosh operation system.

- Command-line interface such as DOS prompt in Microsoft Windows, Terminal in Unix, Linux and Machitosh operating systems.

Command-line interface applications use shell to allow users to interact with operating systems efficiently. Unix-like systems come with several type of shell applications:

- *sh* (Bourne Shell)

- *csh* (C Shell)

- *ksh* (Korn Shell)

- *bash* (Bourne Again Shell)

- *pdksh* (Public Domain Korh Shell)

*bash* is the standard shell comes with modern Linux distributions.  In Unix-like systems, such as Linux, a shell is started by the login process according to setting in `/etc/passwd`

<pre>
root:x:0:0:root:/root:<b>/bin/bash</b>
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
messagebus:x:106:110::/var/run/dbus:/bin/false
uuidd:x:107:111::/run/uuidd:/bin/false
lightdm:x:108:114:Light Display Manager:/var/lib/lightdm:/bin/false
whoopsie:x:109:116::/nonexistent:/bin/false
avahi-autoipd:x:110:119:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/bin/false
avahi:x:111:120:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
colord:x:112:123:colord colour management daemon,,,:/var/lib/colord:/bin/false
dnsmasq:x:113:65534:dnsmasq,,,:/var/lib/misc:/bin/false
hplip:x:114:7:HPLIP system user,,,:/var/run/hplip:/bin/false
kernoops:x:115:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false
pulse:x:116:124:PulseAudio daemon,,,:/var/run/pulse:/bin/false
rtkit:x:117:126:RealtimeKit,,,:/proc:/bin/false
saned:x:118:127::/var/lib/saned:/bin/false
usbmux:x:119:46:usbmux daemon,,,:/var/lib/usbmux:/bin/false
speech-dispatcher:x:120:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false
epmd:x:121:130::/var/run/epmd:/bin/false
</pre>

## Shell Prompt

The default bash shell prompt is `$`

<pre>
<b>$ ls</b>
a    a.c    Desktop    Documents    Downloads
</pre>

Most Linux distribution set the prompt in user's bash configuration file `(~/.bashrc)` as

```bash
# ...

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi

# ...
```

In essence, if `$color_prompt` is `yes`, then it uses a colorful prompt.

`${var:+value}` means that `if $var is defined; then use value; else do nothing`.

`${debian_chroot}` is an environment variable that is defined when user changes root directory (via *chroot*).

`\u`, `\h` and `\w` are instructions to *bash* to show user name, host name and current working directory, respectively.

`\$` is to escape `$`.

`\[\033[01;32m\]`, `\[\033[00m\]` and `\[\033[01;34m\]` are ASCII escape codes to display colors on terminals.

Below is an example of animated ASCII art from [https://www.cyberciti.biz/open-source/command-line-hacks/linux-unix-desktop-fun-christmas-tree-for-your-terminal/](https://www.cyberciti.biz/open-source/command-line-hacks/linux-unix-desktop-fun-christmas-tree-for-your-terminal/)

![ASCII animated Christmas Tree](./perl-tree.gif)

## Standard Output

The standard output of any shell is terminal.

<pre>
<b>$ echo Hello World!</b>
Hello World!
<b>$ echo Hello              World!</b>
Hello World!
<b>$ echo "Hello              World!"</b>
Hello              World!
<b>$ echo -n "No new line"</b>
No new line$
<b>$ printf 'Temperature = %6.2f\n\n' 34.1231</b>
Temperature =   34.12

<b>$ </b>
</pre>

We can redirect standard output (from terminal) a file. The standard output (`STDOUT`) has file descriptor number 1.

<pre>
<b>$ echo "This is a line." > ./file.txt</b>
<b>$ cat file.txt</b>
This is a line.
<b>$ echo "This is another line." > ./file.txt</b>
<b>$ cat file.txt</b>
This is another line.
<b>$ echo "This line is appended." >> ./file.txt</b>
<b>$ cat file.txt</b>
This is another line.
This line is appended.
<b>$ cat no_such_file >> ./file.txt</b>
cat: no_such_file: No such file or directory
<b>$ cat file.txt</b>
This is another line.
This line is appended.
</pre>

The error message is not appended to `file.txt` as it is output to standard error (`STDERR`) which is default to terminal and has file descriptor number 2.

<pre>
<b>$ cat no_such_file >> ./file.txt 2>&1</b>
<b>$ cat file.txt</b>
This is another line.
This line is appended.
cat: no_such_file: No such file or directory
<b>$ </b>
</pre>

## Variables

Variables are used to store string which could be recalled later.

Variable name must begin with alphabetical or underscore (`_`) chracters, followed by one or more alphanumeric or underscore characters.

Variable name is case sensitive.

Use equal sign (`=`) to assign value (on the right-hand side) to variable (on the left-hand side). There is no space on either side of the equal sign.


<pre>
<b>$ 1name = a</b>
No command '1name' found, did you mean:
 Command 'uname' from package 'coreutils' (main)
1name: command not found
<b>$ 1name=a</b>
1name=a: command not found
<b>$ name=a</b>
<b>$ echo name</b>
name
<b>$ echo $name</b>
a
<b>$ name="a"</b>
<b>$ echo $name</b>
a
<b>$ echo $Name</b>

<b>$ </b>
</pre>
