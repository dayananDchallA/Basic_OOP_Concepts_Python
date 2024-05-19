'''
Polymorphism is the ability of an object to take on multiple forms.

It enables you to write generic code that can work with objects of multiple types, as long as they share a common interface.

A common way to achieve polymorphism is method overriding.

Method overriding is when a subclass provides a specific implementation of a method that is already defined in its parent class.

For example, let’s say we have an interface Document which defines a method show().
'''

class Document:
    def show(self)-> None:
        raise NotImplementedError("Subclass must implement abstract method")
    

class Pdf(Document):
    def show(self) -> None:
        print("Showing PDF Content")


class Word(Document):
    def show(self) -> None:
        print("Showing Word Content")


docs = [Pdf(), Word()]

for doc in docs:
    doc.show()


# Each subclass (Pdf, Word) of Document implement the show method differently (method overriding), 
# but the interface remains consistent giving the ability to iterate over both the classes using a single for loop.