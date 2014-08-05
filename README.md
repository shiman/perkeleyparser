perkeleyparser
==============

A python wrapper of Berkeley parser. You can create a parser instance,
and it will stay there waiting for your feed, and return the parsed tree.

Currently it's still in the primitive development stage, only taking the jar
file and the grammar file as its arguments. More features will be added 
later, including multi thread processing. :)


## Requirements

* python 2.7
* Java
* [BerkeleyParser](http://code.google.com/p/berkeleyparser/downloads/list) jar file and grammar files (make sure that it works under your java version)
* For linux/mac: Python package `pexpect` (install by `pip install pexpect`)
* For windows: Python package `winpexpect` (install by `pip install winpexpect`)

## Usage

```python
>>> from BerkeleyParser import parser
>>> p = parser(jar_path, gr_path)
>>> tree = p.parse("This is an apple")
>>> print tree
( (S (NP (DT This)) (VP (VBZ is) (NP (DT an) (NN apple)))) )
```

Initialization of the parser might take a short while, please don't be desparate.
