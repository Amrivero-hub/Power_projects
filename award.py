#Practical Task 1

#Design a program that determines the award a person competing in a triathlon will receive.
#Your program should read in the times (in minutes) for all three events of a triathlon,
#namely swimming, cycling, and running, and then calculate and display the total time taken to complete the triathlon.
#The award a participant receives is based on the total time taken to complete the triathlon. The qualifying time for awards is 100 minutes.


swimming=float(input("Enter the time for swimming (in minutes):"))
cycling=float(input("Enter the time for cycling (in minutes):"))
running=float(input("Enter the time for running (in munites):"))

total_time=swimming+cycling+running
print(total_time)
if total_time<=100: 
    award= "Your award is Provincial Colours" # Within the qualifying time (0 - 100 minutes)
elif total_time<=105:
    award= "Your award is Provincial Half Colours" # Within 5 minutes of the qualifying time (101 -105 minutes)
elif total_time<=110:
    award= "Your award is Provincial Scroll" # Within 10 minutes of the qualifying time (106 - 110 minutes)
else:
    award= "No award"
print(f"The award that the participant will receive is {award}.")

