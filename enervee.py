#!/usr/bin/env python3.5
import string, unittest
from functools import wraps

"""
Top 10 reasons David would enjoy working for Enervee (he thinks) ...
"""

#######################################
"""
1. Please write a Python function called 'is_palindrome' that takes a single 
argument of a string. This function should determine if the given string is 
identical forward and backward, ignoring spaces, punctuation and character 
case. (Note: You are welcome to do problem 2 first, if you prefer.) 
For example: 
>>> is_palindrome('abba') == True 
>>> is_palindrome('race car') == True 
>>> is_palindrome('A man, a plan, a canal, Panama!') == True 
>>> is_palindrome('Not a palindrome') == False 
"""

def is_palindrome(s):
  s = ''.join([c for c in s if c in string.ascii_letters])
  s = s.lower()
  r = s[::-1]
  p = (r == s)
  print(s, r, p)
  return p

#######################################
"""
2. Please write the unittest class 'TestIsPalindrome' that extends 
unittest.TestCase that sufficiently tests the 'is_palindrome' function from 
problem 1. 
"""

class TestIsPalindrome(unittest.TestCase):
  def testFully(self):
    self.assertTrue(is_palindrome('abba'))
    self.assertTrue(is_palindrome('race car'))
    self.assertTrue(is_palindrome('A man, a plan, a canal, Panama!'))
    self.assertTrue(is_palindrome('Not a palindrome'))

#######################################
"""
3. Given the following base class: 
 
class Animal(object): 
  def breath(self): 
    print('Breathing.')
 
Please show what the class hierarchy would be for Man, Woman, Dog, Cat, Horse 
and Zebra. Feel free to create other intermediary classes as needed. Please 
include an example method for each class, such as 'speak' or 'eat'. 
"""

class Animal(object):
  def breath(self):
    print('Breathing.')

class Zebra(Animal):
  def speak(self):
    print('Zebras cannot be tamed while ... ') ; self.breath()

class Human(Animal):
  def speak(self):
    print('A Human who should be free while ... ') ; self.breath()

class Man(Human):
  def speak(self):
    print('A man is ... ')
    super().speak() 

class Woman(Human):
  def speak(self):
    print('A woman is ... ') ; super().speak() 

class Pet(Animal):
  def speak(self):
    print('A pet who can communicate with their Humans while ... ') ; self.breath();

class Dog(Pet):
  def speak(self):
    print('A dog is ... ') ; super().speak() 
     
class Cat(Pet):
  def speak(self):
    print('A cat is ... ') ; super().speak()

class Horse(Pet):
  def speak(self):
    print('A horse is ... ') ; super().speak() 

#######################################
"""
4. Please describe how to find the middle element of a linked list. Can it be 
found without iterating over any element in the list more than once? Please 
explain.
"""

def linkedList():
  """
  4. A singly linked list must provide direct access to its first element,
  which then provides a 'link' to the next element, and accessing the 
  next element provides access to the subsequent element, etc. Consequently
  one must traverse the list element by element in order to access the
  desired item. If the implementation includes a total-length attribute
  or property and if each element in the list includes an index, one can
  compare indices to the total length, so one need not traverse the entire
  list in order to find 'the middle element'. 

  A doubly linked list can be traversed from beginning to end or in reverse
  from end to beginning, are from anywhere in between, and thus helps optimize
  access to individual elements. That is, if the algorithm currently has access
  to an arbitrary element in the list, along with its index, the algorithm is
  free to traverse subsequent list items in whichever direction is shorter/quicker.
  """
  return linkedList.__doc__

#######################################

"""
5. In Python, what is list comprehension? Please give an example.
"""

def listComprehend():
  """
  5. Python list comprension is a kind of short-hand-syntactic-suger that allows
  one to create a list via a simple expression. The implementation of the func.
  'is_palindrome' uses list comprehension in its first statment.
  """
  # example:
  txt = listComprehend.__doc__ ; print(txt)
  lc = [c for c in txt] ; print(lc)

#######################################
"""
6. In Python, what is a decorator? Please give an example.

Brett Slatkin's excellent book 'Effective Python" provides a concise explanation
of decorators and recommends making use of functools.wraps in one's code. Frameworks 
like Django and Flask rely heavily on decorators, etc. I'll borrow and paraphrase
from Slatkin: decorators provide the ability to wrap functions with code that runs
before and/or after the code within the wrapped function.
"""

def decorate(func):
  @wraps(func)
  def wrapper(*args, **kwds):
    print('Calling decorated function')
    return func(*args, **kwds)
  return wrapper

@decorate
def fib(n):
  print('fin n: ', n)
  if n in (0, 1): return n
  return (fib(n-2) + fib(n-1))

#######################################
"""
7. What is the difference between a process and a thread? What are some 
advantages and disadvantages of each? 
"""

def pyThreads():
  """
  Python 'threads' are something of a misnomer -- they do not actually use multi-threaded
  code ... they actually refer to async. i/o features of the Python run-time.

  In the traditional definition of threads, a process is a single "main" thread, executing in
  a single CPU, using dedicated stack and heap space memory. A process main thread, however,
  can create multiple child threads that share the parent / main thread's memory and can in
  theory utilize other available CPUs and run in parallel. Some algorithms can greatly benefit
  from multi-threading, if there are lots of available CPUs and if access to the shared memory
  does not involve too much mutual exclusion locking, etc. The advantages and disadvanteges
  tend to derive from the extent that any shared resource(s) can be efficiently accessed, etc.
  """
  return pyThreads.__doc__

#######################################
"""
8. In Python, what is the difference between the '==' operator and the 'is' operator? 
"""

def pyCongruent():
  """
  This requires a discussion of refernces vs. values ... but I'll keep it brief ...
  A Python variable 'is' congruent with another variable if they reference the same 'thing'.
  Pythan variables which reference different 'things' that are in some way 'equal' (numerically
  or ?) yield True when compared via '==', etc.

  One can test congruent references vi id(thing) ...
  """
  return pyCongruent.__doc__

#######################################
"""
9. In Python, what is a module? What is it used for? 
"""

def pyModules():
  """
  Any legitimate Python source file can be used as a 'module'. A directory / folder of one or
  more Python modules is considered a 'package'. This enervee.py file is a module. I could have
  placed each of these 10 questions into its own file in one directory / folder to publish
  as a package of 10 modules, etc.

  It is considered a 'best practice' to organize one's Python code into well annotated / documented
  modules, making use of so-called docstrings, and comments ...
  """
  return pyModules.__doc__

#######################################
"""
10. Regarding web frameworks, please explain what an html template is and how is it related to a view?
"""

def templates():
  """
  HTML templates are text files that provide a mixture of plain HTML and markup with custom 'tags'.
  A run-time library is used to process the tags, inserting/generating replacement text. Python web
  frameworks like Django rely heavily on templates, and Flask has made jinja2 popular. There are,
  however, other uses of templates -- for output of JSON or YAML (for example Ansible processes template
  text into YAML).
  """
  return templates.__doc__

#######################################

if __name__ == "__main__":
  # 1. direct tests:
  p = is_palindrome('abba')
  p = is_palindrome('race car') 
  p = is_palindrome('A man, a plan, a canal, Panama!')
  p = is_palindrome('Not a palindrome')

  # 2.
  try:
    unittest.main()
  except: pass

  # 3.
  z = Zebra()
  m = Man()
  w = Woman()
  d = Dog()
  c = Cat()
  h = Horse()
  all = [z, m, w, d, c, h]
  for a in all:
    a.speak()

  # 4.
  help(linkedList)

  # 5.
  listComprehend()

  # 6.
  f = fib(6) ; print('fibunaci result: ', f)

  # 7.
  help(pyThreads)

  # 8.
  help(pyCongruent)

  # 9
  help(pyModules)

  # 10.
  help(templates)

