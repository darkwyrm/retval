# retval

A MIT-licensed Python module for better function return values without exceptions.

## Description

This module provides RetVal, a class which powers up how you handle errors and return values. With RetVal you can:

- Use more specific error codes
- Pull from a small library of common errors
- Provide context information with errors
- Create your own errors quickly -- no more writing custom Exception classes
- Return a variable number of data values from functions

## Status

The module is production stable in active use.

## Usage

TODO

## History

This module exists because I was inspired to think about Python error-handling and return values after spending more than a little time learning Go. Go errors are little more than strings, which isn't great, but they are often paired with other return values. If no error is returned, then the other return value is safe to consider as valid. Go also doesn't have very many built-in error codes and are not very well documented. RetVal takes from the good and builds upon it. It integrates pretty easily into existing code and the extra contextual information makes debugging significantly easier.

## Building

This is a very simple but useful module. Running `python setup.py install` should be the thing needed.
