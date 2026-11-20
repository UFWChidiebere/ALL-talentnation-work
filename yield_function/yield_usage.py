def log_streamer():
    print("🎬 Factory starting...")
    yield "Log Entry A"          # PVM pauses here and returns this string
    
    print("🔄 Factory waking up...")
    yield "Log Entry B"          # PVM pauses here and returns this string
    
    print("🛑 Factory empty.")
    yield "Log Entry C"

# Activating the generator
stream = log_streamer()

# Asking for the first piece of data
print(next(stream)) 

# Asking for the second piece of data
print(next(stream))

print(next(stream))

"""this is just a code emphasizing on the usage of the usage of the yield() function, how it is like the return statement/keyword however different from the return....... in the sense that it is more patient than the return statement/keyword"""

'''this is the actual definition of the YIELD KEYWORD


The keyword yield is used in Python to create a Generator. It acts like a specialized, memory-saving return statement.
While a standard return statement destroys a function's state and hands back a final result all at once, yield pauses the function, sends back a single piece of data, and waits for you to ask for the next piece [1]. When asked, the function wakes up exactly where it left off, continues down its top-to-bottom path, and yields the next value.'''


#now to resume the yield(which is like a temporary pause to the running of your code, you will have to call the next() on it for without it the yielf will simply just sit there and not even resume.... also, you can use the for loop to resume.

#the yield generator will have to have it's own instance(object) just like in OOP when a class is created and an instace of the class is created too to call on the methods of the class)