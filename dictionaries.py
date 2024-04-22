#dictionary is a collection of related key value pairs
workmates={
    150 : "Maxwell Barno",
    230 : "Khadija Mganda",
    340 : "Naomi Munyiri",
    450 : "Brian Kipkosgei",
    1000 : ["mike","luke","john"]
}

#accessing values in dictionary
print(workmates[150])

#adding to dictionary
workmates[680]="Nick Ochieng"
workmates[760]="Kevin Mwaniki"

print(workmates)

names=workmates[1000]
print(len(names))

print(len(workmates.keys()))