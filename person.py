class Person: # defines a class named person

    def __init__(self, first, last): # initializes the first and last name when a new object is created
        self.firstname = first
        self.lastname = last
    def __str__(self): ##overload the str to print first and last name
        return "First Name: " +self.firstname + "\nLast Name: " + self.lastname

    ##Add operator overload for print that prints
    ##First Name: firstname
    ##Last  Name: lastname
        

#Make derived class "Employee" that inherits the base class Person
#In the constructor, grab all the Person methods using the super() method
#(1) Add a new variable to hold date of birth called "dob" to the __init__
#   Overload __str__ with super and add "\nDOB: " + str(self.dob)
#(2) Also add a new variable "ssn" to the __init__ to hold the social security number
#    Add a new method called get_ssn that returns the ssn

class Employee (Person): #defines a class named person

    def __init__(self, first, last, dob, ssn): # reminder: space between def and __init
        super().__init__(first, last) # when using super, initializing line doesn't need self again
        self.dob = dob
        self.ssn = ssn
        
    def __str__(self): # overloads __str__ with super and adds "\nDOB: " + str(self.dob)
        return super().__str__() + "\nDOB" + str(self.dob)
    
    def get_ssn(self): #method to return ssn
        return self.ssn
        

if __name__=="__main__":
    

    ##Test situation
    
    boss = Person("Hamed", "Haq")
    empl = Employee("Ted", "McMaster", "03151970", 999999999)

    print(boss)
    print(empl)
    print(empl.get_ssn())
    


