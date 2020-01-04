Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import random
>>> random.rand
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    random.rand
AttributeError: module 'random' has no attribute 'rand'
>>> random.randint(1,20)
10
>>> import urllib.request
>>> urllib.request.urlopen('http://www.google.com')
<http.client.HTTPResponse object at 0x105927630>
>>> urllib.__path__
['/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib']
>>> 
