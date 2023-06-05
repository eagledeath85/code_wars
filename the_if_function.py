def truthy():
    print("True")


def falsey():
    print("False")


def _if(bool_value, truthy, falsey):
# prints 'True' to the console
    if not bool_value:
        return falsey()
    else:
        return truthy()


_if(False, truthy, falsey)