
# && sintaxe to import modules
# from greeter import greet
# greet("lucas");

# import greeter as gr
# gr.greet("Lucas")

# && Sintaxe to import packages
# from Package import greeter as gt,goodbye as bye;
# gt.greet("Lucas")
# bye.depart("lucas")

# import Package.greeter,Package.goodbye
# Package.greeter.greet("Lucas")
# Package.goodbye.depart("lucas")


from Package.SubPackage.Friends import people
from Package.greeter import greet

for person in people:
    greet(person)