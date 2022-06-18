# <a href="https://www.geeksforgeeks.org/python-oops-concepts/#:~:text=In%20Python%2C%20object%2Doriented%20Programming,in%20the%20programming.">Python OOP - geeksforgeeks.org</a>
<h4>Main Concepts of Object Oriented Programming (OOP)</h4>
<ul>
	<li>Class</li>
	<li>Objects</li>
	<li>Polymorphism</li>
	<li>Encapsulation</li>
	<li>Inheritance</li>
	<li>Data Abstraction</li>
</ul>

<h4>Class</h4>
<p>
A class is a collection of objects. 
A class contains the blueprints or the prototype from which the objects are being created. 
It is a logical entity that contains some attributes and methods. 
</p>
<pre>
<code>
class Dogs:
	pass
</code>
</pre>

<h4>Objects</h4>
<p>
The object is an entity that has a state and behavior associated with it. 
It may be any real-world object like a mouse, keyboard, chair, table, pen, etc. 
Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects. 
More specifically, any single integer or any single string is an object. 
The number 12 is an object, the string “Hello, world” is an object, a list is an object that can hold other objects, and so on. 
You’ve been using objects all along and may not even realize it.
</p>
<pre>
<code>
obj = Dog()
</code>
</pre>

<h4>The self</h4>
<p>
1. Class methods must have an extra first parameter in the method definition.
We do not give a value for this parameter when we call the method, Python provides it.<br/>
2. If we have a method that takes no arguments, then we still have to have one argument.<br/>
3. This is similar to this pointer in C++ and this reference in Java.
</p>


<h4>The __init__ method </h4>
<p>
The __init__ method is similar to constructors in C++ and Java. 
It is run as soon as an object of a class is instantiated. 
The method is useful to do any initialization you want to do with your object. 
</p>
<pre>
<code>
class Dog:

    # class attribute
    attr1 = "mammal"
 
    # Instance attribute
    def __init__(self, name):
        self.name = name
 
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
 
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
 
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
</code>
</pre>
