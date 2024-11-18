def Myfunction(INPUT,PLUST,MINUS):
    MINUS = 0
    PLUST = 0
    if INPUT < 0:
        MINUS += INPUT
        return MINUS
    elif INPUT > 0:
        PLUST += INPUT
        return PLUST
    return 0

    
