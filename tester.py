#!/usr/bin/env python2.7
import traceback
import argparse
import time
import os
import re
import sys
from colorama import Fore
from colorama import Style
from cmd2 import Cmd


class testnavigator(Cmd):

    DEFAULT_PROMPT = 'testnavigator>'
    prompt = DEFAULT_PROMPT

    def __init__(self, testDirectory=None, testtest=None, testCase=None):
        Cmd.__init__(self)

        self.allow_redirection = False
        self.debug = True

        self.testcases = []

        # To remove built-in commands entirely, delete their "do_*" function from the
        # cmd2.Cmd class
        if hasattr(Cmd, 'do_load'):
            del Cmd.do_load
        if hasattr(Cmd, 'do_py'):
            del Cmd.do_py
        if hasattr(Cmd, 'do_pyscript'):
            del Cmd.do_pyscript
        if hasattr(Cmd, 'do_shell'):
            del Cmd.do_shell
        if hasattr(Cmd, 'do_alias'):
            del Cmd.do_alias
        if hasattr(Cmd, 'do_shortcuts'):
            del Cmd.do_shortcuts
        if hasattr(Cmd, 'do_edit'):
            del Cmd.do_edit
        if hasattr(Cmd, 'do_set'):
            del Cmd.do_set
        if hasattr(Cmd, 'do_quit'):
            del Cmd.do_quit
        if hasattr(Cmd, 'do__relative_load'):
            del Cmd.do__relative_load
#        if hasattr(Cmd, 'do_eof'):
#            del Cmd.do_eof
#        if hasattr(Cmd, 'do_eos'):
#            del Cmd.do_eos
        if hasattr(Cmd, 'do_unalias'):
            del Cmd.do_unalias

    def _ok(self):
        print('')
        print('[ok][%s]' % (time.ctime()))

    def _error(self, err=None):
        if err:
            print(str(err))
        print('')
        print('[error][%s]' % (time.ctime()))

    @staticmethod
    def xterm_message(msg, colour, oldmsg="", newline=False):
        if len(oldmsg):
            sys.stdout.write('\033[%sD' % (len(oldmsg)))
        sys.stdout.write(colour)
        sys.stdout.write(msg)
        sys.stdout.write(Style.RESET_ALL)
        if len(msg) < len(oldmsg):
            sys.stdout.write(' ' * (len(oldmsg) - len(msg)))

        if newline:
            sys.stdout.write('\n')
        sys.stdout.flush()

    def do_exit(self, args):
        'Exit the navigator - or move up a level of the context'
        if len(self.level) == 2:
            print ('exit to directory')
        elif len(self.level) == 1:
            print ('exit to top level')
        else:
            return True

    def complete_run(self, text, line, begidx, endidx):
        if len(text.split()) == 0:
            return self.tests
        
        result = []
        for item in self.tests:
            if item[0:len(text)] == text:
                result.append(item)
        result.sort()
        return result


    def complete_select(self, text, line, begidx, endidx):
        if len(text.split()) == 0:
            return self.testcases

        result = []
        for item in self.testcases:
            if item[0:len(text)] == text:
                result.append(item)
        result.sort()
        return result

    def do_select(self, args):
        'Select a File containing python unittests'

        if not os.path.exists('test_%s.py' % (args)):
            self.xterm_message('Unable to open test case %s from %s' %
                               (args, os.getcwd()), Fore.RED, newline=True)
            return False

        self.xterm_message('Loading file....', Fore.YELLOW) 
        found_import = False
        found_class = None
        self.tests = []

        regex_import = re.compile('^import unittest\s*$')
        regex_class = re.compile('^class (\S+)\(unittest\.unittest\):\s*$')
        regex_test = re.compile('^ {4}def test_([^\(]+)\(.*:\s*$')
        with open('test_%s.py' % (args)) as file:
            line = file.readline()
            while line != "":
                if regex_import.match(line):
                    found_import = True
                if regex_class.match(line) and found_class is None:
                    found_class = regex_class.sub('\g<1>', line)
                elif regex_class.match(line) and found_class is not None:
                    self.xterm_message('Constraint: only one unittest class supported.',
                                       Fore.RED, oldmsg='Loading file....', newline=True) 
                    return False
                if regex_test.match(line):
                    self.tests.append(regex_test.sub('\g<1>', line))
                line = file.readline()
        self.prompt = '%s(%s.%s)%% ' % (self.testdir, args, found_class)

        self.xterm_message('Loaded %s test(s)' % (len(self.testcases)), Fore.GREEN, oldmsg='Loading file....', newline=True) 


    def do_run(self, args):
        'Run a test'
        print ('dotest called', args)


if __name__ == '__main__':
    cli = testnavigator()
    if len(sys.argv) < 2:
        testnavigator.xterm_message("""Usage: %s <directory>""" % (sys.argv[0]), Fore.RED, newline=True)
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        testnavigator.xterm_message("""Usage: %s <directory>\n\n%s does not exist""" %
                                    (sys.argv[0], sys.argv[1]), Fore.RED, newline=True)
        sys.exit(1)
    testdir = sys.argv[1]
    os.chdir(testdir)
    sys.argv.pop(1)
    cli.testdir = testdir
    cli.testcases = []
    for test in os.listdir('./'):
        if test[0:5] == 'test_' and test[-3:] == '.py':
            cli.testcases.append(test[5:-3])
    cli.prompt = testdir + '% '
    cli.cmdloop(intro='Python Unittest Navigator')
