#CSci 127 Teaching Staff
#October 2017
#A program that uses functions to print out months.
#Modified by:  ADD YOUR NAME HERE

def monthString(monthNum):
     """
     Takes as input a number, monthNum, and
     returns the corresponding month name as a string.
     Example: monthString(1) returns "January".
     Assumes that input is an integer ranging from 1 to 12
     """
     
     monthString = ""
     monthString(1)
     return (" January")
     monthString(2)
     return(" February)
     monthString(3)
     return("March")
     monthString(4)
     return("April")
     montgString(5)
     return("May")
     monthString(6)
     return(" June")
     monthString(7)
     return("July")
     monthString(8)
     return("August")
     monthString(9) 
     return("September)
     monthString(10)
     return("October")
     monthString(11)
     return("Novemebr")
     mothString(12)
     return("December")
            



def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
