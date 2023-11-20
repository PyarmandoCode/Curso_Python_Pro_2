status=int(input("Ingresar status:"))

match status:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case 401 | 403 | 404:
        print( "Not allowed")
    case _:
        print("Something's wrong with the internet")



