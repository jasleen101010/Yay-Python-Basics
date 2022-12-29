# Intro to OOPS 

`Object-Oriented Programming` is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.
For instance, an object could represent a person with properties like a name, age, and address and behaviors such as walking, talking, breathing, and running. 
Or it could represent an email with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.

Another common programming paradigm is procedural programming, which structures a program like a recipe in that it provides a set of steps, 
in the form of functions and code blocks, that flow sequentially in order to complete a task.

> Link - https://www.programiz.com/python-programming/object-oriented-programming

* Some Important Terminologies of OOPs - 

__Object__ `[Eg -> ram = Human()]`
An object is an entity that has attributes and behaviour. For example, Ram is an object who has attributes such as height, weight, color etc. and has certain behaviours such as walking, talking, eating etc.

__Class__
A class is a blueprint for the objects. For example, Ram, Shyam, Steve, Rick are all objects so we can define a template (blueprint) class Human for these objects. The class can define the common attributes and behaviours of all the objects.

__Methods__
As we discussed above, an object has attributes and behaviours. These behaviours are called methods in programming.

__Inheritance__
Inheritance is a way of creating a new class for using details of an existing class without modifying it. 
The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

__Encapsulation__
Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.

__Polymorphism__
Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.

__Class variable__ − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. 
Class variables are not used as frequently as instance variables are.

__Data member__ / __Instance variable__ − A class variable or instance variable that holds data associated with a class and its objects. 
A variable that is defined inside a method and belongs only to the current instance of a class.

> __Function overloading__ − The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.

__Instance__ − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.

__Instantiation__ − The creation of an instance of a class.

__Method__ − A special kind of function that is defined in a class definition.

> __Operator overloading__ − The assignment of more than one function to a particular operator.

`__init__()` is a special method. [Constructor]

`self` ->  `.self` is referring to the instance in which we were talking about context. 

__Static Methods__ => Want to create functions that organise functions together. add5 add10 etc etc. To keep the functions structured and keep them under a same class.
methods that we're able to use but are not specific to an instance. So, we don't have to make an instance of these methods.

* Primitive data structures—like numbers, strings, and lists—are designed to represent simple pieces of information,
such as the cost of an apple, the name of a poem, or your favorite colors, respectively. What if you want to represent something more complex?

For example, let’s say you want to track employees in an organization. You need to store some basic information about each employee, 
such as their name, age, position, and the year they started working.

Example - 

```
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]
```

## Summing Up

Classes are used to create user-defined data structures. Classes define functions called methods, 
which identify the behaviors and actions that an object created from the class can perform with its data.

A class is a blueprint for how something should be defined. It doesn't actually contain any data. 
The Dog class specifies that a name and an age are necessary for defining a dog, but it doesn't contain the name or age of any specific dog.

While the class is the blueprint, an instance is an object that is built from a class and contains real data. 
An instance of the Dog class is not a blueprint anymore. It’s an actual dog with a name, like Miles, who’s four years old.

Put another way, a class is like a form or questionnaire. An instance is like a form that has been filled out with information. 
Just like many people can fill out the same form with their own unique information, many instances can be created from a single class.

=> Creating a new object from a class is called instantiating an object. 


---------------------------------------------------------------------------------------------------------------------------------------------------