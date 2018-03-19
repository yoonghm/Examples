# bash Shell

Every operating system has at least one or more applications to allow user to interact with itself:

- Graphical user interface applications such as Windows Explorer in Microsoft Windows, Machintosh Finder in Machitosh operation system.

- Command-line interface such as DOS prompt in Microsoft Windows, Terminal in Unix, Linux and Machitosh operating systems.

Command-line interface applications use shell to allow users to interact with operating systems efficiently.

Each command accepted by a shell would be executed in a child process.  A child process would inherit all settings from the shell.

Unix-like systems come with several type of shells:

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

## Standard Input

The stadard input is keyboard (or mouse if it is an GUI application).

<pre>
<b>$ read -p "What is your name? "</b>
What is your name? Yoong Hor Meng
<b>$ read -p "What is your name? " name</b>
What is your name? <b><i>Yoong Hor Meng</i></b>
<b>$ echo $name</b>
Yoong Hor Meng
<b>$ </b>
</pre>

The input could be redirected from a file using `<` following by file name.

<pre>
<b>$ echo "This is a line." > file.txt</b>
<b>$ echo "This is another line." >> file.txt</b>
<b>$ wc < file.txt</b>
 2  8 38
<b>$ </b>
</pre>

The input could also be redirected from command line using *here-document* with `<<` followed by a string delimiter. Subsequent data are inputs. The end of input must be terminated by the same string delimiter in a separate line.

<pre>
<b>$ wc << EOF
> This is a line.
> This is another line.
> EOF</b>
 2  8 38
<b>$ </b>
</pre>

## Variables

Variables are used to store string which could be recalled later.

Variable name must begin with alphabetical or underscore (`_`) chracters, followed by one or more alphanumeric or underscore characters.

Variable name is case sensitive.

Use equal sign (`=`) to assign value (on the right-hand side) to variable (on the left-hand side). There is no space on either side of the equal sign.

If there is ambiguity when variable is combined text, you may use use curly brackets to delimiter the variable name. For example, if `$PROJ` has value `TIF`and you want to create A running running of `TIF`such as `TIF1`, `TIF2`, etc., then you may use `${TIF}1`and `${TIF}2, etc.

### Local Variables

Examples below illustrate some concepts of local variable, which is valid in the current shell only.

Local variables are not passed to child processes forked by the shell.

Variables could be displayed using builtin command `declare -p`.

<pre>
<b>$ 1myname = a</b>
1myname: command not found
<b>$ 1myname=a</b>
1myname=a: command not found
<b>$ myname=a</b>
<b>$ echo myname</b>
myname
<b>$ echo $myname</b>
a
<b>$ myname="a"</b>
<b>$ echo $myname</b>
a
<b>$ echo $MyName</b>

<b>$ declare | grep myname</b>
myname=a
<b>$ declare -p | grep myname</b>
declare -- myname="a"
<b>$ </b>
</pre>

### Environment Variables

Environment variables are defined during the startup of `bash`, via `/etc/bash.bashrc`, and `~/.bashrc`.

Environment variable could be created using builtin command `export`.

Environment variables could be displayed using builtin commands `export -p` or `env`

Environment variables are passed to child processes forked by the shell.

<pre>
<b>$ export -p | grep myname</b>
<b>$ echo $myname</b>
a
<b>$ export MYNAME="Yoong Hor Meng"</b>
<b>$ echo $MYNAME</b>
Yoong Hor Meng
<b>$ env | grep MYNAME</b>
MYNAME=Yoong Hor Meng
<b>$ declare | grep MYNAME</b>
MYNAME='Yoong Hor Meng'
<b>$ export -p | grep MYNAME</b>
declare -x MYNAME="Yoong Hor Meng"
<b>$ export -p | grep myname</b>
<b>$ </b>
</pre>

## Bash Script

`bash` script should start with a *shh-bang* line that show full path name to bash shell.

<pre>
#!/bin/bash
</pre>

Below is a `bash` script named `hello.sh`

```bash
#!/bin/bash

echo "Hello World!"
```

There are two way to execute the script:

a. **Call the script via bash**<br>
   In this case, the *shh-bang* line is not important.

<pre>
<b>$ bash ./hello.sh</b>
Hello World!
</pre>

b. **Make the script executable**<br>
   In this case, the *shh-bang* line decides which program to run the script.

<pre>
<b>$ ls -l hello.sh</b>
-rw-rw-r-- 1 spsy spsy 34 Mar 19 02:01 hello.sh
<b>$ chmod u+x hello.sh</b>
<b>$ ls -l hello.sh</b>
-rwxrw-r-- 1 spsy spsy 34 Mar 19 02:01 hello.sh
<b>$ ./hello.sh</b>
Hello World!
<b>$ </b>
</pre>

## Arithmetic

It used to be complicated to perform arithmetic in shell.  New versions of `bash` have made it simpler.

Use builtin command `let` to perform arithmetic.

<pre>
<b>$ x=2</b>
<b>$ x=x+1</b>
<b>$ echo $x</b>
x=1
<b>$ x=2</b>
<b>let x=x+1</b>
<b>$ echo $x</b>
3
<b>$ x=2</b>
<b>x=x**3</b>
<b>$ echo $x</b>
x**3
<b>$ x=2</b>
<b>let x=x**3</b>
<b>$ echo $x</b>
8
<b>$ x=2</b>
<b>x+=1</b>
<b>$ echo $x</b>
21
<b>$ x=2</b>
<b>let x+=1</b>
<b>$ echo $x</b>
3
<b>$ x=2</b>
<b>$ y=3</b>
<b>$ let z=x+y</b>
<b>$ echo $z</b>
5
<b>$ let x=9</b>
<b>$ let q=x/4</b>
<b>$ let r=x%4</b>
<b>$ echo Quotion= $q remainder= $r</b>
Quotion= 2 remainder= 1
<b>$ </b>
</pre>

## Branching,Conditions and Loops

### `if` ... `then`... `elfi` `then` ... `else` ... `fi` Branchings

`bash` provides `if`, `elfi` and `else` blocks. Each block shall be grouped using `then` and `fi`.

Below is a `bash` script named `ask.sh`

```bash
#!/bin/bash

read -p "Enter a number: " number

if (( number > 100 ))
then
  echo "The number is greater than 100"
elif (( number < 100 ))
then
  echo "The number is less than 100"
else
  echo "The number is 100"
fi
```

It is necessary to place the expession for `if` and `elif` within double parentheses.
The spaces before and after the `>` and `<` are optional.

`bash` shell also provide `-lt` and `-gt` for `>` and `<` respectively. However, the double parentheses shall be replaced by single parentheses.

```bash
# ...
if [ $number -gt 100 ]
#...
elif [ $number -lt 100 ]
# ...
```

Let's make the script execuitable by the owner:

<pre>
<b>$ chmod u+x ask.sh</b>
</pre>

Run the script:

<pre>
<b>$ ./ask.sh</b>
Enter a number: 200
The number is greater than 100
<b>$ ./ask.sh</b>
Enter a number: 100
The number is 100
</pre>

### `while` ... `do` ... `done` Loop

`while` ... `do` ... `done` loop allow shell script to perform some actions repeatedly as long as some condition(s) is(are) met.

Below is the `hello_count.sh` script:

```bash
#!/bin/bash
count=0
MAX=5

while (( count < MAX ))
do
  printf 'Hello World for %4d\n' $count
  let count++
done
```

*Note: Double parentheses are used to evaluate arithmetic expression.*

<pre>
<b>$ chmod u+x hello_count.sh</b>
<b>$ ./hello_count.sh</b>
Hello World for    0
Hello World for    1
Hello World for    2
Hello World for    3
Hello World for    4
<b>$ </b>
</pre>

Let's create another script `ask2.sh` which is similar to `ask.sh` than repeatedly ask for number until user enter `q`.

There is no `do` ... `while` ... `done` loop syntax in `bash` shell. Hence it is necessary to perform `read` before the `while` loop.

```bash
#!/bin/bash

read -p "Enter a number( q to quit): " number

while [ "$number" != "q" ]
do
  if (( number > 100 ))
  then
    echo "The number is greater than 100"
  elif (( number < 100 ))
  then
    echo "The number is less than 100"
  elif (( number == 100 ))
  then
    echo "The number is 100"
  fi

  read -p "Enter a number( q to quit): " number
done
```

`Note: Non-arithmetic expressions are enclosed in square brackets`

<pre>
<b>$ chmod u+x ask2.sh</b>
<b>$ ./ask2.sh</b>
Enter a number( q to quit): 100
The number is 100
Enter a number( q to quit): q
<b>$ </b>
</pre>

### `for` loop

There are two versions of `for` loop.

1.  **Older Version: Interating Over A Fixed List of Items**

A example of older version of `for` loop: `forloop1.sh`

```bash
#!/bin/bash

for i in 1 2 3 4 5
do
  echo $i
done
```

<pre>
<b>$ chmod u+x forloop1.sh</b>
<b>$ ./forloop1.sh</b>
1
2
3
4
5
<b>$ </b>
</pre>


2.  **Newer Version: Similar to C/C++ Syntax**
For loop allows a shell script to perform some actions in a specific number of time.

The general syntax is

```bash
for (( expr1 ; expr2 ; expr3 ))
do
  actions
done
```

`expr1`, `expr2` and `expr3` are arithmetic expressions.

`expr1` is the initialization expression which may include one or more initialization separated by comma.

`expr2` is the stopping expression which may include one or more stopping conditions separated by comma.

`expr3` is the looping expression which may include one or more stopping conditions separated by comma.

*Note: Varriables inside double paretheses do not need to use **$** (such as `myname` except for arguments like `$1`).*

A example of older version of `for` loop: `forloop2.sh`

```bash
#!/bin/bash

for (( i=0, j=0;
       i+j<10, j<10;
       i++, j++
    ))
do
  printf '%2d * %2d = %4d\n' $i $j $((i*j))
done
```
