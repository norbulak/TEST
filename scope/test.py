
d="bonjour"

def fun():
    global d
    d = 42
    return d

fun()
print(d)
