import os
import time
    
"""
    TODO:
        ->  Bprint() with speed option
        ->  function to setup arguments that will always be the same for a function
        ->  Update docs
"""


def cls():
    if os.name in ('nt', 'dos'):
        os.system("cls")
    else:
        os.system("clear")


def Binput(Input_message = "", Input_type = "str", error_message = "", clear = False, delay = 0,
           func = False, **kwargs):
    """
    I recommend to write all arguments if you want to callback a func,
    for the function arguments you have to assign var to values, like :
    Binput(Input_message=..., ..., delay=..., func=function to callback, func_args="hahahahahaha", other_func_args="test")
    """
    try:
        return Input_type(input(Input_message))
    except:
        if clear:
            cls()
        if error_message:
            print(error_message)
            if delay > 0:
                time.sleep(delay)
        else:
            if delay > 0:
                time.sleep(delay)
            print(f"You didn't write an {Input_type.__name__} !")
        if func:
            func(**kwargs)
            
def Btype(var, print=False):
    """
    Like type()function but return the name only name of a var like: int, not <class 'int'>
    But can print automatically, or return
    """
    if print:
        print(type(var).__name__)
    else:
        return type(var).__name__

# some function to make coding faster, but not more easier to understand
def i(text):    
    return input(text)

def p(text):
    return print(text)
