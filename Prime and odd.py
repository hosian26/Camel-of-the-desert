# Number =(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)
 odd = 0
 for num in Number:
     if num % 2 == 0:
         odd += 1
         print("The Count of odd Number:",odd)

 numbers = 21
 odd_numbers = [num for num in range(1,numbers+1)
                if num % 2 !=0]
 print(odd_numbers)
 total_number = len(odd_numbers)
 print(numbers)


 total_students =int(input("Enter Total Student:"))
 odd_numbers = [num for num in range(1,total_students+1)
                if num % 2 !=0]
 num_of_students =  len(odd_numbers)
 print(num_of_students)


A = int(input("Enter The Number :"))
B = int(input("Enter The Number ;"))

