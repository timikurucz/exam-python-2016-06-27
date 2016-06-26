# Create a Rocket class
# It should take 3 parameters in it's constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9"
# 2nd parameter: the starting fuel level as a number
# 3rd parameter: number of launches as a number
#
# It should have 3 methods:
#
# launch()
# it should use 1 fuel if its a falcon1 and 9 if its a falcon9
# it should increment the launches by one
#
# refill()
# it should refill the rockets fuel level to 5 if falcon1 and to 20 if falcon9
# it should return the used fuel
# example: if the rocket is a falcon1 and has fuel level 3 than it should return 2
#
# getStats()
# it should return it's stats as a string like: "name: falcon9, fuel: 11"

# Create a SpaceX class
# it should take 1 parameter in it's constructor
# 1st parameter: the stored fuel
# 
# it shoild have 4 methods:
#
# addRocket(rocket)
# it should add a new rocket to SpaceX that is given in it's first parameter
#
# refill_all()
# it should refill all of it's rockets with fuel and substract the needed fuel from the storage
#
# launch_all()
# it should launch all the rockets
#
# getStats()
# it should return it's stats as a sting like: "rockets: 3, fuel: 100, launches: 1"


# The following code should work with the classes


space_x = SpaceX(100)
falcon1 = Rocket('falcon1', 0, 0)
falcon9 = Rocket('falcon9', 0, 0)
returned_falcon9 = Rocket('falcon9', 11, 1)

print(returned_falcon9.getStats()) # name: falcon9, fuel: 11

space_x.addRocket(falcon1)
space_x.addRocket(falcon9)
space_x.addRocket(returned_falcon9)

print(space_x.getStats()) # rockets: 3, fuel: 100, launches: 1
space_x.refill_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 1
space_x.launch_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 4
space_x.buy_fuel(50)
print(space_x.getStats()) # rockets: 3, fuel: 116, launches: 4

