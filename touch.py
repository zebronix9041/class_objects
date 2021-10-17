class Employee:
    no_of_leaves=4
    pass
ankit=Employee()
alia=Employee()
ankit.name="ankit singh"
alia.name="alia bhatt"
Employee.no_of_leaves=8 #(it will change the class variable)
ankit.no_of_leaves=34    #(it will not change the class varible(it will create its own[personal]variable))
print(ankit.__dict__)     #(__dict__ is aattribute which returns dictionary)
print(Employee.nprint(Empl


