#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.) write a python for loop that prints the numbers from 1 to 10.

for number in range(1, 11):
    print(number)


# In[2]:


#2.)create a lists of fruits (e.g.,["apple,"banana","cherry"]) and write a  for loop to print each fruit in the list.
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# In[3]:


#3.)write a python program that calculates the sum of all even numbers from 1 to 50 using a for loop.

total_sum = 0
for number in range(1, 51):
    if number % 2 == 0:
        total_sum += number

print("The sum of even numbers from 1 to 50 is:", total_sum)


# In[5]:


#4.)create a list of integers and using a for loop find and print largest number in the list.

numbers = [1,23,67,2,45,134,76]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number
print("The largest number in the list is:", largest_number)


# In[6]:


#5.)write a python program that uses a for loop to find and print all the prime numbers between 1 and 100. A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
print("Prime numbers between 1 and 100:")
for num in range(1, 101):
    if is_prime(num):
        print(num)


# In[7]:


#6)write a python program that takes a list of dictionaries ,where each dictionary represents a person with keys "name" and "age"
#find and print average age of all the people in the list.

people = [
    {"name": "Aman", "age": 23},
    {"name": "Ravi", "age": 25},
    {"name": "Seema", "age": 35},
    {"name": "Rohit", "age": 17}
]

total_age = 0
count = len(people)

for person in people:
    total_age += person["age"]

average_age = total_age / count

print("The average age of all the people is:", average_age)


# In[ ]:




