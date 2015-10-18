#!/usr/bin/env python
from commandwrapper import WrapCommand

# ls -l | grep and | wc -l
if 1:
    Ls = WrapCommand( 'ls -l')
    GrepAnd = WrapCommand( 'grep and')
    Wc = WrapCommand( 'wc -l')
    Wc.stdin = GrepAnd
    GrepAnd.stdin = Ls
    Wc.start()
    Wc.join()
    print Wc.results

# ls -l | grep and | wc -l
if 1:
    Ls = WrapCommand( 'ls -l | grep and | wc -l', shell=True)
    Ls.start()
    Ls.join()
    print Ls.results

