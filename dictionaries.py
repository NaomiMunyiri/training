# #dictionary is a collection of related key value pairs
# workmates={
#     150 : "Maxwell Barno",
#     230 : "Khadija Mganda",
#     340 : "Naomi Munyiri",
#     450 : "Brian Kipkosgei",
#     1000 : ["mike","luke","john"]
# }

# #accessing values in dictionary
# # print(workmates[150])

# #adding to dictionary
# # workmates[680]="Nick Ochieng"
# # workmates[760]="Kevin Mwaniki"

# # print(workmates)

# # names=workmates[1000]
# # print(len(names))

# # print(len(workmates.keys()))


# #iterating through a dictionary
# #printing all keys one by one
# for mate in workmates:
#     print(mate)

# #printing all values one by one
# for mates in workmates:
#     people=workmates[mates]
#     print(people)

# #method to retrieve all keys
# print(workmates.keys())

# #method to retrieve all values
# print(workmates.values())

# #method to print both keys and values
# print(workmates.items())


# print("\n")
# for key,value in workmates.items():
#     print(f"{key}={value}")


# print("\n")
# #method to retun a specific value whos key has been passed 
# team_lead=workmates.get(150)
# print(team_lead)

# print("\n")
# #delete method
# del workmates[150]
# print(workmates)

# workmates.pop("Naomi Munyiri")
# print(workmates)


#nested dictionaries
myfamily={
    "child0":{
        "name":"Emily",
        "year":1990,
    },
    "child1":{
        "name":"Sarah",
        "year":2000
    },
    "child2":{
        "name":"Mike",
        "year":2012
    }
}

print(myfamily["child1"]["name"])

for i, obj in myfamily.items():
    print(i,obj)