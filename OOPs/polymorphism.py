class animal:
    def __init__(self,colour,age):
        self.colour=colour
        self.age=age

class dog(animal):
    def __init__(self, colour, age):
        self.colour = "Dog " + colour
        super().__init__(self.colour, age)
        

class cat(animal):
    def __init__(self, colour, age):
        self.colour="cat " + colour
        super().__init__(self.colour, age)
   

s1=animal("none",4)
s2=dog("brown",5)
s3=cat("white",3)

print(s1.colour, s1.age)
print(s2.colour,s2.age)
print(s3.colour,s3.age)





