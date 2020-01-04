Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
my_tuple = ('a','b','c',1,2,3)
>>> my_tuple
('a', 'b', 'c', 1, 2, 3)
>>> my_tuple[2]
'c'
>>> my_tuple[2] = 'd'
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    my_tuple[2] = 'd'
TypeError: 'tuple' object does not support item assignment
>>> 
