# BetterTools Docs

## Installation

To use [BetterTools](https://pypi.org/project/BetterTools/)
Install python 3 , open a **cmd** and write:
> pip install BetterTools

## How do i use it?

 > [cls()](#cls)   
[Bprint()](#bprint)   
[Btype()](#btype)   
[Binput()](#binput)   
[loading()](#loading)   
[logs()](#logs)   
[initLogs()](#initlogs)   
[All shortcut function](#shortfunction)

### cls

Function to clear console, whatever your OS is.   
To use this function :    
```>>> cls()```   


### Bprint

A better version of print native python function.   
Arguments:
* [text](#text)
* [speed](#speed)


##### text    
This is the text to print, can be a string, so it will be print letters by letters.   
If this is a list :

* the last item can be an int, which is the time  in second between the printing of all item from the list.

```
>>> Bprint(["1st", "2nd", "3rd", 2])
1st (wait 2 second) 2nd (wait 2 second) 3rd
```

* the last item can be "replace", and it will write, and replace the last printed item *(I recommend you to use the [speed](#speed) arguments)*
  
```
>>> Bprint(["1st", "2nd", "3rd", "replace"], speed=0.5)
3rd
```
* We can use both of them

```
>>> Bprint(["1st", "2nd", "3rd", "replace", 2], speed=0.5)
3rd
```

##### speed

By default speed=0.   
It represents the time between every printing of text characters.
```
>>> Bprint("One character every 0.5s", 0.5)
One character every 0.5s
```

### Btype

A better version of type native python function.   
Arguments:
* [var](#var)
* [out](#out)
  
##### var   
You need to put the variable that you want to know the type:
```
>>> a = 1
>>> print(Btype(a))
int
```

##### out   
By default out=False.   
To say if you want the function to return the type of a variable, or you want to print it.
```
>>> a = "wow"
>>> Btype(a, out=True)
str
```

### Binput
Better version of input native python function.   
Arguments:
* [message](#message)
* [Input_type](#Input_type)
* [error_message](#error_message)
* [clear](#clear)
* [delay](#delay)
* [func](#func)

##### message

By default message="".   
Represent the message that will be print with the input:

```
>>> answer = Binput("Do you like pizza ? ")
>>> print(answer)
Do you like pizza ? yes
yes
```

##### Input_type

By default Input_type=str   
Same as:

```
int(input())
#or
str(input())
#etc
```

You can give what type of input you want:

```
>>> age = Binput("How old are you ? ", int)
How old are you ? Hey
You didn't write an int !
```

##### error_message
By default, error_message="".   
This is the message that will be print when the user will put an invalid literal (=ValueError).
If you don't change error_message, the message will be 
```
You didn't write an # and the type you where waiting for
```
```
>>> age = Binput("How old are you ? ", int, "You need to write your age !")
How old are you ? Hey
You need to write your age !
```

##### clear
Same as cls() function, but in case of error during the Binput.
By default clear=False
```
>>> age = Binput("How old are you ? ", int, "You need to write your age !", True)
How old are you ? Hey
"""get clear"""
You need to write your age !
```

##### delay
By default delay=0.
If you want to put delay (in seconde) between the answer and the error message.
```
>>> age = Binput("How old are you ? ", int, "You need to write your age !", False, 2)
How old are you ? Hey
"""wait 2 secondes"""
You need to write your age !
```

##### func
By default func=False.
If you want to callback a function when there is an error during the input.
```
>>> def main():
...     print("This is a call")
...     age = Binput("How old are you ? ", int, "You need to write your age !", False, 2, main)
>>> main()
This is a call
How old are you ? Hey
You need to write your age !
This is a call
# etc
```
If your function has arguments, you can write them after the func arguments:
```
>>> def main(test):
...     print(test)
>>> age = Binput("How old are you ? ", int, "You need to write your age !", False, 2, main, test="This is a callback")
How old are you ? Hey
You need to write your age !
This is a callback
```

### loading   

Loading function is made to create a loading print, in percentage.
The load argument is the advancement of the loop. It needs to be between 0 and 100, like percentage.
```
>>> for i in range(10000):
...     loading(i/100)
| ██████████████████   | 100%
```
To clearly understand how does it works you should try it.

### logs

Function to easily create logs in a text file, or in the prompt.   

Arguments:
* [TextLogs](#TextLogs)
* [file](#file)
* [now](#now)

##### TextLogs

This is the text that you will use for your logs.
```
>>> logs(TextLogs="This is logs", file="", now="")
This is logs
```

##### file

In the exemple above, the text was printed because we didn't specify any files, if you want the logs to be write in a file you will need this argument.
```
>>> logs(TextLogs="This is logs", file="logs.txt", now="")
```
It can be .txt, .log, etc...   

##### now

***I recommend you to setup this one using the [initLogs](#initLogs) function***

This arguments is used to tell the current time.
Look how to use time.strftime().


### initLogs

This function is used to easily use logs function by creating global variable like [now](#now), [file](#file) and [TextLogs](#TextLogs).   
Arguments :
* [date](#date)
* [write_file](#write_file)
* [text](#text)

##### date

This arguments is for the [now](#arguments)

Need to be a list.  
The elements can be :   
* For the time
* As separator
* Or somethings else

By default the separator is ":", but you can change it by adding an element in your list, between some elements of the date or in the begining, like : 
```
["sep=/", "etc"]
```
If you don't want any seperator :   
```
["sep=", "etc"]
```
For the time :    
You have to put in an element, the classic (easier to understand) or the shortcut, depend of what you want.
|Date        | Classic   | Shortcut    |   
|:----------:|:----------:|:----------:|
| Day        | day       | d           |
| Month      | month     | m           |
| Year       | year      | y           |    
| Hour       | hour      | h           |
| Minute     | minute    | M           |
| Second     | second    | s           |
 
Or some premade:

| Date                  | Classic      |
|:---------------------:|:------------:|
| Hour Minute Second    | current time |
| Day Month Year        | current date |

Even the premade option will be separate if you setup one, or by the default one if you don't.

```
>>> initLogs(date=[
...     "sep=/", "day", "month"
... ]
23/01
```
```
>>> initLogs(date=[
...     "sep=/", "day", "month", "sep=:", "y"
... ]
23/01:2022
```
```
>>> initLogs(date=[
...     "sep=/", "current time"
... ]
20/28/49
```

##### write_file
This is the file where you want to write your logs. If you don't specify it it will be print
```
>>> initLogs(["sep=/", "current time"], "logs.txt")
```

##### text

This is the text that you want to write after the date.
```
>>> initLogs(date=["sep=/", "current time"], text="Wow, you did it !")
20/33/55 Wow you did it !
```

### Shortfunction

These function are just to code faster, but I make your code harder to understand

 > [p()](#p)   
[i()](#i)

##### p

Same as print native function, with all the same arguments

##### i

Same as print native function

  
 > **[My github](https://github.com/Remi-Avec-Un-I)**   
<img src="https://avatars.githubusercontent.com/u/74991151?v=4" alt="github image" width="100"/> 