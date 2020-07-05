def fun_test(x):
    return x ** 2
    
if(__name__ == "__main__"):
    print("start function tests")
    
    if(4 != fun_test(2)):
        print("error")
        
    if(9 != fun_test(-3)):
        print("error")
