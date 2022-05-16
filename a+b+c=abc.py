#made by Ruben Bartelet in 5/2022
# this script checks what integer solutions there are for a+b+c = a*b*c
a,b = 0,0

true_list = []

itterations = 10
print("start")
for d in range(-itterations, itterations):
    for e in range(-itterations, itterations):
        a = d
        b = e

        print("a: " + str(a))
        print("b: " + str(b))

        if (a*b-1) != 0:
            c = (a+b)/(a*b-1) # a+b+c = a*b*c => a+b = a*b*c-c = c*(a*b - 1) => c = (a+b)/(a*b-1)
            if len(str(c)) == 3 and ((c >= 0 and str(c)[2] == '0') or (c < 0 and str(c)[3] == '0')): 
                print('c: ' + str(int(c)))
                bool = True
                for f in range(0, len(true_list)):
                    check = true_list[f]
                    if (check[0]+check[1]+check[2]) == (a + b + c):
                        bool = False
                if bool and (a + b + c) != 0:
                    true_list.append([a,b, int(c)])
            else:
                print('c: ' + str(c))
        else:
            print('c: undefined')
   
        print(" ")

print(true_list)
        
#this (kind of) confirms that there are no integer solution except 1,2 and 3 (not counting a+b+c = 0).