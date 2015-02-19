# whileloops.py

# Guidelines:
    # Make sure you can get into a while loop
    # Do something in the while loop (must be indented)
    # Make sure you can get out of your while loop

import random

# Counter controlled while loop
# Repeat 10 times
count = 0 # set counter to 0
while count < 10:
    count += 1
    # comment
    print( count )

print( "Done counting" )


# Results Controlled Loop
    # You are looking for a specific condition
    # but you don't know how long it will take
# Simulated Battle
    # Loop until hero has no more health

health = 100
while health > 0:
    input("Press enter to attack")
    damage = random.randint(10, 20)
    health -= damage
    if health < 0:
        health = 0 # avoid having - health
    print("You took {} damage points.".format(damage))
    print("Your health is now {}.".format(health))
    
