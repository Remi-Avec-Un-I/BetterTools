This is a lib to improove input() fonction.

DOCS:
    cls() fonction :
        -> clear console

    Binput() fonction:
        -> take multiple arguments :
            - Input_message : By default it's "". This is the message which is going to be with the input()
            ex : Binput(Input_message = "Hey :")
            >>> Hey : (<- input)
        
            - Input_type : By default it's "str". Ths is the type of answer you're waiting in your input()
            This is the same things as doing this :
            Binput(Input_message = "Hey :", Input_type = "int") 
            <=> int(input("Hey :"))

            - error_message : By default it's "". This is the message which is going to be print in case of an error
            with the input, like if you write a string but you're waiting for an int. By default the message is :
            "You didn't write an {Input_type.__name__} !"
            ex: Binput(Input_message = "Hey :", Input_type = "int", error_message = "You had to write a integer !")
            >>> Hey : hello
            >>> You had to write a integer !

            - clear : By default it's False. This is if you want to clear the console after an error in an input()

            - delay : By default it's 0. This the time between the error message and the callback fonction

            - func :  By default it's False. This is the function you want to callback after an error on the Binput.

            - **kwargs : Are all the arguments you want to use for the callback function
            You have to write the var name before the argument !
            ex: Binput(Input_message="test :", ... ,clear=True, delay=1,
             func=function, First_Arg="yes", Second_Arg="an other one" ...) 
