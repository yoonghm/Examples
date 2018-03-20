# Python 3

## History

Python is an interpreted high-level programming language for general-purpose programming.

Python was created by [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) and first released in 1991.

Python that emphasizes code *readability*, *expressive* syntaxes and code *reusability*.

**Python 2.0** was released on 16 October 2000. Python 2.7's end-of-life was set to 2020.

**Python 3.0** was released on 3 December 2008. For the forseen future, development and enhancements will be done on this version.

These two major versions are not 100% compatible.

## Python Implementations

Python currently has five production-quality implementations:
- CPython
- Jython
- IronPython
- Pypy
- MicroPython

### CPython

[CPython](https://en.wikipedia.org/wiki/CPython) is the most popular and the reference implementation of Python.

Python is written in C. It comes with a large standard libary which is written in C and Python.

It compiles Python programs into intermediate bytecode, which is then executed by its virtual machine.

It is available for Windows, Unix-like operation systems.

## Jython

[Jython](http://www.jython.org/) is an implementation of the Python to run on the Java platform.

It is the successor of JPython.

It can import and use any Java class.  Except for some standard modules which are implemented in C, Jython programs use Java classes instead of Python modules.

## IronPython

[IronPython](http://ironpython.net/) is an implementation of the Python targeting the .NET framework.

IronPython is written entirely in C# and Python.

### PyPy

[PyPy](https://en.wikipedia.org/wiki/PyPy)
is a just-in-time (JIT) compiler for Python. Hence Python programs run faster in PyPy than in CPython.

Most Python code runs well on PyPy, except for code that relies on CPython extensions.

## MicroPython

[MicroPython](https://en.wikipedia.org/wiki/MicroPython) is Pythan 3 variant, which is written in C and optimised for microcontrollers.

MicroPython has since been run on Arduino, ESP8266, SAMD21.

## Python Distributions

There are many [Python distribution](https://wiki.python.org/moin/PythonDistributions), the most popular distributions are mentioned here:

### Anaconda from Continuum Analytics

[Anaconda](https://www.anaconda.com/) is the most successful Python distributions.

Anaconda comes with thousand of Python modules and very suitable for data science and machine learning development.

Anaconda comes with `conda` package and virtual environment manager.


### Miniconda from Continuum Analytics

[Miniconda](https://conda.io/miniconda.html) is the stripdown version of Anaconda - it just comes with Python binary, `conda` and minimum packages.

## Anaconda Installation

We do not wish to disturb the existing Python binary and modules that come with the Linux distribution as some system programs may rely on it.  Some Python modules have dependency on the other modules. Changing the modules may affect this modules.  Hence Python comes with virtual environment.  However, we will not be using Python standard virtual environment here.

### Download an Anaconda installer for Linux (32-bit or 64-bit OS)

You need to download only one version that suits your system architecture:

1. [64-bit command-line installer for Linux](https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh)

2. [32-bit command-line installer for Linux](https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86.sh)

You can use `arch` or `uname -m` to check the architecture that your Linux OS is running on.

```bash
## Download the relevant installer using wget
#
# For 64-bit version
#
wget -t 0 -c https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh

#
# For 32-bit version
#
wget -t 0 -c https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86.sh

# Install it in your home directory (Answer Yes's for all questions)
bash ./Anaconda3-5.1.0-Linux*
```

Anaconda is installed in your home directory.

Microsoft Visual Code (VSCode) is installed in `/usr/share/code`. If your Linux has GUI, you may run VSCode via `code` from the command line.

### Re-read `~/.bashrc`
The new configuration may not be recognized by your current `bash` shell. You may open a new terminal or force your `bash` to re-read the configuration:

<pre>
<b> $ which python3</b>
/usr/bin/python3
<b> $ which python</b>
/usr/bin/python
. ~/.bashrc
<b> $ which python3</b>
/home/spsy/anaconda3/bin/python3
<b> $ which python</b>
/home/spsy/anaconda3/bin/python
</pre>

### Conda Environment

If there are multiple Python developement projects and multi-user using tje new Anaconda installation, you may want to create conda environment to separate them:

<pre>
<b>$ conda create --name demo python=3.6  # demo is created under ~/anaconda3/envs/</b>
<b>$ source activate demo                 # To activate the environment</b>
<b>(demo) $ source deactivate             # To deactivate the environment</b>
<b>$ conda env remove --name demo        # Remove demo environment</b>
</pre>

## Python Language Overview

Python is similar to `bash` except that it is more powerful and comes with many useful modules (i.e., libraries).

Example: `hello_world.py`

```Python
#!/usr/bin/env python3

print('Hello World!')
```

<pre>
<b> $ chmod u+x hello_world.py</b>
<b> $ ./hello_world.py</b>
</pre>

Example: Execute Python script using `-c` option:

<pre>
<b>$ python3 -c "import time; print(time.asctime())"</b>
</pre>

