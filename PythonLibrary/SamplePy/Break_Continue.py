'''ex1

a = [1, 3, 5, 7, 9, 10, 11, 13, 15]

has_even = False

for i in a:
    if(i % 2 == 0):
    
        has_even = True

print("List has even: " + str(has_even))

'''

'''ex2

a = [1, 3, 5, 7, 9, 10, 11, 13, 15]

has_even = False

for i in a:
    print(i) #NEW CODE
    
    if(i % 2 == 0):
        has_even = True
        break #NEW CODE
        
print("List has even: " + str(has_even))

'''

'''ex3

for i in range(1, 100):
    if(i % 3 == 0):
    
        if(i % 5 == 0):
        
            print(i)

'''

for i in range(1, 100):
    if(i % 3 == 0):
    
        continue
        
    if(i % 5 == 0):
        continue
        
print(i)
