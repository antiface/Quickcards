from time import localtime, strftime
 
def f(): return strftime("%Y", localtime())
 
def g(): return strftime("%B", localtime())
 
def h(): return strftime("%d", localtime())
 
def i(): return strftime("%A", localtime())
 
def j(): return strftime("%X", localtime())
 
"""
>>> f()
'2014'
>>> g()
'June'
>>> h()
'26'
>>> i()
'Thursday'
>>> j()
'14:31:27'
 
"""
def k(): return [f(), g(), h(), i(), j()]
 
"""
>>> k()
['2014', 'June', '26', 'Thursday', '14:32:53']
"""
def l(): return raw_input("Context: ")
 
def m(): return raw_input("Qualia: ")
 
def n(): return [k(), l(), m()]
 
"""
>>> x = n()
Context: Sitting at computer.
Qualia: Enjoying myself.
>>> x
[['2014', 'June', '26', 'Thursday', '14:34:30'], 'Sitting at computer.', 'Enjoying myself.']
"""
 
###############################################
 
from Dee import *
 
"""
>>> print Relation(["Time", "Context", "Qualia"],
  [{"Time": "Fri", "Context": "At home", "Qualia": "Happy"},
  {"Time": "Sat", "Context": "Outside", "Qualia": "Stressed"},])
+------+---------+----------+
| Time | Context | Qualia   |
+======+=========+==========+
| Fri  | At home | Happy    |
| Sat  | Outside | Stressed |
+------+---------+----------+
>>> MORAL_TEMP = Relation(["Time", "Context", "Qualia"],
  [{"Time": "Fri", "Context": "At home", "Qualia": "Happy"},
  {"Time": "Sat", "Context": "Outside", "Qualia": "Stressed"},])
>>> print MORAL_TEMP.renderHTML()
<table><thead><th><em>Time</em></th><th><em>Context</em></th>
  <th><em>Qualia</em></th></thead><tbody><tr><td>Fri</td>
  <td>At home</td><td>Happy</td></tr><tr><td>Sat</td>
  <td>Outside</td><td>Stressed</td></tr></tbody></table>
"""
