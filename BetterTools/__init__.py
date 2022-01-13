import os
import time
    
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
    
    """
    TODO:
        ->
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
                
                
Binput(Input_message="test :", Input_type="int", error_message="You had to write a number", clear=True, delay=1)
print("yax")