def perimRect(length,width):
   """
   Compute perimiter of rectangle
   >>> perimRect(2,3)
   10
   >>> perimRect(4, 2.5)
   13.0
   >>> perimRect(3, 3)
   12
   >>>
   """
   return ((2*length)+(2*width))


def areaRect(length,width):
   """
   compute area of rectangle
   >>> areaRect(2,3)
   6
   >>> areaRect(4, 2.5)
   10.0
   >>> areaRect(3,3)
   9
   >>>
   """
   return (length*width)


def isList(x):
   """
   returns True if argument is of type list, otherwise False

   >>> isList(3)
   False
   >>> isList([5,10,15,20])
   True
   """
   
   return ( type(x) == list )   # True if the type of x is a list



def isString(x):
    """"
    return True if x is a string, otherwise False
    """
    
    return (type(x)== str)



def isAdditivePrimaryColor(color):
    """
    return True if color is a string equal to "red", "green" or "blue", otherwise False
    >>> isAdditivePrimaryColor("blue")
    True
    >>> isAdditivePrimaryColor("black")
    False
    >>> isAdditivePrimaryColor(42)
    False
    >>>
    """
    
    return ( (color == "red" ) or (color == "green" ) or (color == "blue") )



def isSimpleNumeric(x):
   """
   returns True if x is has type int or float; anything else, False 
   >>> isSimpleNumeric(5)
   True
   >>> isSimpleNumeric(3.5)
   True
   >>> isSimpleNumeric("5")
   False
   >>> isSimpleNumeric([5])
   False
   >>> isSimpleNumeric(6.0221415E23)
   True
   >>>
   """
   
   return ((type(x) == int) or (type(x) == float)) 
