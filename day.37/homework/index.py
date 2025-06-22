def greet(name):
    return "Hello " + name


def get_length(text=None):
    if text is None:
        return None
    return len(text)


print(greet("Aleksandre"))      
print(get_length("Python"))     
print(get_length())             
