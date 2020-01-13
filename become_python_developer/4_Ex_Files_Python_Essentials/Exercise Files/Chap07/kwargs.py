#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr') # this is a dictionary
    kitten(**x) # 2 asterisk (**) are necessary when passing a dictionary as argument into a function

def kitten(**kwargs): # argument dictionary (**kwargs) stand for 'Key word arguments'
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()

