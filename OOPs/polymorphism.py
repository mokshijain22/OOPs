# class animal:
#     def __init__(self,colour,age):
#         self.colour=colour
#         self.age=age

# class dog(animal):
#     def __init__(self, colour, age):
#         self.colour = "Dog " + colour
#         super().__init__(self.colour, age)
        

# class cat(animal):
#     def __init__(self, colour, age):
#         self.colour="cat " + colour
#         super().__init__(self.colour, age)
   

# s1=animal("none",4)
# s2=dog("brown",5)
# s3=cat("white",3)

# print(s1.colour, s1.age)
# print(s2.colour,s2.age)
# print(s3.colour,s3.age)




#Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
nums=[1,2,3,1]
def containsDuplicate(nums):
    