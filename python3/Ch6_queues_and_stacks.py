Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import queue
>>> q = queue.Queue()
>>> q.empty()
True
>>> q.put('bag1')
>>> q.empty
<bound method Queue.empty of <queue.Queue object at 0x1057632e8>>
>>> q.put('bag2')
>>> q.put('bag3')
>>> g.get()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    g.get()
NameError: name 'g' is not defined
>>> q.get()
'bag1'
>>> g.get()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    g.get()
NameError: name 'g' is not defined
>>> q.get()
'bag2'
>>> q.get()
'bag3'
>>> q = queue.Queue(2)
>>> q.empty()
True
>>> q.put('bag1')
>>> q.full()
False
>>> q.put('bag2')
>>> q.full()
True
>>> q.put_nowait('bag3')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    q.put_nowait('bag3')
queue.Full
>>> stack = list()
>>> stack.append('bill1')
>>> stack.append('bill2')
>>> stack.pop()
'bill2'
>>> stack.append('bill3')
>>> stack.append('bill4')
>>> stack.pop()
'bill4'
>>> stack.pop()
'bill3'
>>> stack.pop()
'bill1'
>>> stack.pop()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    stack.pop()
IndexError: pop from empty list
>>> 
