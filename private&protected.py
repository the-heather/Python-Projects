#
# Python:    3.10
#
# Author:    H.Shultz
#
# Purpose:   TTA - Python Course, Created a class that uses encapsulation by
#            making use of a private attribute and a protected attribute, then
#            created an object that uses both.



#creating class
class one:
    #creating instance
    def __init__(self):
        # Protected varabile
        self._protected = 2
        # Private varabile
        self.__private = 5

    def getPrivate(self):
        print(self.__private)
    
    def getProtected(self):
        print(self._protected)

test = one()
#call to private varabile
test.getPrivate
#call to protected varabile
test.getProtected




