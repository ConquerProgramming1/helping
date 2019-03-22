# Helping

*As my girlfriend's cat likes to say while knocking over my drink: "I'm HELPING!"*

This library is dedicated to providing helpful information about Python objects.
It's useful for everyone, but especially dedicated to those learning how to program.

This library is the result of teaching Python to thousands of students. 
Over time I found that the built-in ``dir()`` function was actively confusing
to people learning Python, and I developed this library to help the students.
Then I found myself using it for my own coding.

That's when I new I had something worthwhile.

The goal is "Readable information for real people."

## info()
The primary method is ``helping.info()``, which provides a readable summary of
an object. It separates out the methods, attributes, classes, and exceptions, 
and perhaps most importantly, doesn't show private items unless requested.

To see private items, pass the argument ``private=True``.

By default the items are listed vertically, which I've found to be most readable.
If you'd like a more compact form, pass ``compact=True``.

## functions()
Shows any functions defined in the script, and all built-in Python functions.

## methods()
Shows just the methods of the specified object.

## attributes()
Shows just the attributes of the specified object.

## classes()
Shows just the classes belonging to the specified object.

## exceptions()
Shows just the exceptions belonging to the specified object.