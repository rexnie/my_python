#!/usr/bin/env python
import os

def make_loop():
    dashes = '\n' + '-' * 50
    exec_dict = {
'f': """ # for loop
for %s in %s:
    print %s""",
    
's': """
%s = 0
%s = %s
while %s < len(%s):
    print %s[%s]
    %s += 1""",
    
'n': """
%s = %d
while %s < %d:
    print %s
    %s += %d"""
}

    ltype = raw_input('loop type? for/while:')
    dtype = raw_input('data type? num/seq:')
    if dtype == 'n':
        start = input('start=')
        end = input('end=')
        step = input('step=')
        seq = str(range(start, end, step))
    else:
        seq = raw_input("sequence:")

    var = 'var'
    seq_var = 'seq_var'
    if ltype == 'f':
        exec_str = exec_dict['f'] % (var, seq, var)
    elif ltype == 'w':
        if dtype == 's':
            exec_str = exec_dict['s'] % (var, seq_var, seq, var, seq_var, \
            seq_var, var, var)
        elif dtype == 'n':
            exec_str = exec_dict['n'] % (var, start, var, end, var, var, step)

    print dashes
    print 'u generated code:' + dashes
    print exec_str + dashes
    print 'exec result:'
    exec exec_str
    print dashes

if __name__ == '__main__':
    #make_loop()
