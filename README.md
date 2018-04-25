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

An example of a test case actually running with bad results, and then running a single command each time.

```
~/pyunittest-cli $ ./tester.py test 'select zzz' 'run'
Python Unittest Navigator
select zzz
Loaded 4 test(s)
run
Running 3 tests(s)...
test_foo (test_zzz.x) ... ok
test_bar (test_zzz.x) ... ERROR
test_boo (test_zzz.x) ... ok

======================================================================
ERROR: test_bar (test_zzz.x)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/adam/pyunittest-cli/test/test_zzz.py", line 10, in test_bar
    a = 5/0
ZeroDivisionError: integer division or modulo by zero

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
test(zzz.x)%
test(zzz.x)% run bar
Running 1 tests(s)...
test_bar (test_zzz.x) ... ERROR

======================================================================
ERROR: test_bar (test_zzz.x)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/adam/pyunittest-cli/test/test_zzz.py", line 10, in test_bar
    a = 5/0
ZeroDivisionError: integer division or modulo by zero

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
test(zzz.x)% run foo
Running 1 tests(s)...
test_foo (test_zzz.x) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
test(zzz.x)%
```





#### TODO:

1. Extend to provide a basic summary after running and ~~provide a really quick/easy way of just re-running failed test cases one by one.~~
- Support reloading code/test case after a change.
- Save the status of the command-line history to a file (like ipython)
- Extended to inspect the results from the runner 
- Extend to behave test cases
- Run pylint tests
- Allow to run all testcases files without having to select an individual file
- Trends
- Some fuzzy logic to try decide which tests cases are most likely to fail
