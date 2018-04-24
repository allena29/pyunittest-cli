# pyunittest-cli

This utility is intended to simplify testing with [python's unittest](https://docs.python.org/2/library/unittest.html) by providing a simple command line interface. A key goal of the command line interface is to provide a developer fine grained control over which test cases they wish to execute.

The python library `Cmd2` provides the interface.


## Example

The interface is started by running the script - a single argument is required which specifies the directory where the test cases are stored.

```
~/pyunittest-cli $ ./tester.py test
Python Unittest Navigator
test% select <TAB COMPLETION>
123     1234    abc
test(abc.x)% select 1<TAB COMPLETEION>
123     1234
test(abc.x)% select abc
Loaded 3 test(s)
test(abc.x)% run <TAB COMPLETION>
bar    boo    foo

```


A developer could jump straight to a directory by providing the 'select abc' command on the command line.

```
~/pyunittest-cli $ ./tester.py test 'select abc'
Python Unittest Navigator
select abc
Loaded 3 test(s)
```


## 

There is fu


#### TODO:

1. Extend to provide a basic summary after running and provide a really quick/easy way of just re-running failed test cases one by one.
- Extend to behave test cases
- Run pylint tests


