#Explain your work

#Question 1
first_list = list(range(0,10,2))
second_list = list(range(1,10,2))

new_list = first_list + second_list
new_list = [x*2 for x in new_list]

for i in new_list:
    print(type(i))
