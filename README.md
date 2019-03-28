# Helping

![Helping logo](helping_logo.jpg)

*As my girlfriend's cat likes to say while knocking over my drink: "I'm HELPING!"*

This library is dedicated to providing helpful information about Python objects.
It's useful for everyone, but especially dedicated to those learning how to program.

This library is the result of teaching Python to thousands of students. 
Over time I found that the built-in `dir()` function was actively confusing
to people learning Python, and I developed this library to help the students.
Then I found myself using it for my own coding.

That's when I knew I had something worthwhile.

The goal is "Readable information for real people."

## Installation
Run this command (note that Python 3.6 or greater is required):

`pip install helping`

## info()
The primary method is `helping.info()`, which provides a readable summary of
an object. It separates out the methods, attributes, classes, and exceptions, 
and perhaps most importantly, doesn't show private items unless requested.

If you call this without arguments, it provides info about the built-in Python functions, classes, and exceptions.

To see private items, pass the argument `private=True`.

By default the items are listed vertically, which I've found to be most readable.
If you'd like a more compact form, pass `compact=True`.

Here is the output from calling `helping.info(int)`:

	int (<class 'type'>)
	  methods:
	    bit_length()
	    conjugate()
	    from_bytes()
	    to_bytes()
	
	  attributes:
	    denominator
	    imag
	    numerator
	    real

Here is the output from calling `helping.info()`:

	builtins (<class 'module'>)
	  methods:
	    abs()
	    all()
	    any()
	    ascii()
	    bin()
	    breakpoint()
	    callable()
	    chr()
	    compile()
	    copyright()
	    credits()
	    delattr()
	    dir()
	    divmod()
	    eval()
	    exec()
	    exit()
	    format()
	    getattr()
	    globals()
	    hasattr()
	    hash()
	    help()
	    hex()
	    id()
	    input()
	    isinstance()
	    issubclass()
	    iter()
	    len()
	    license()
	    locals()
	    max()
	    min()
	    next()
	    oct()
	    open()
	    ord()
	    pow()
	    print()
	    quit()
	    repr()
	    round()
	    setattr()
	    sorted()
	    sum()
	    vars()
	
	  classes:
	    BaseException
	    bool
	    bytearray
	    bytes
	    classmethod
	    complex
	    dict
	    enumerate
	    filter
	    float
	    frozenset
	    GeneratorExit
	    int
	    KeyboardInterrupt
	    list
	    map
	    memoryview
	    object
	    property
	    range
	    reversed
	    set
	    slice
	    staticmethod
	    str
	    super
	    SystemExit
	    tuple
	    type
	    UnicodeDecodeError
	    UnicodeEncodeError
	    UnicodeTranslateError
	    zip
	
	  attributes:
	    Ellipsis
	    NotImplemented
	
	  exceptions:
	    ArithmeticError
	    AssertionError
	    AttributeError
	    BlockingIOError
	    BrokenPipeError
	    BufferError
	    BytesWarning
	    ChildProcessError
	    ConnectionAbortedError
	    ConnectionError
	    ConnectionRefusedError
	    ConnectionResetError
	    DeprecationWarning
	    EnvironmentError
	    EOFError
	    Exception
	    FileExistsError
	    FileNotFoundError
	    FloatingPointError
	    FutureWarning
	    ImportError
	    ImportWarning
	    IndentationError
	    IndexError
	    InterruptedError
	    IOError
	    IsADirectoryError
	    KeyError
	    LookupError
	    MemoryError
	    ModuleNotFoundError
	    NameError
	    NotADirectoryError
	    NotImplementedError
	    OSError
	    OverflowError
	    PendingDeprecationWarning
	    PermissionError
	    ProcessLookupError
	    RecursionError
	    ReferenceError
	    ResourceWarning
	    RuntimeError
	    RuntimeWarning
	    StopAsyncIteration
	    StopIteration
	    SyntaxError
	    SyntaxWarning
	    SystemError
	    TabError
	    TimeoutError
	    TypeError
	    UnboundLocalError
	    UnicodeError
	    UnicodeWarning
	    UserWarning
	    ValueError
	    Warning
	    ZeroDivisionError
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

*Logo by [Ericatures](https://www.ericatures.com)*