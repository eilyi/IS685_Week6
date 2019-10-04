#people array

people= [
            ["Jane Smith", 23, "123 Fake ST."],
            ["Slim Dusty", 44, "564 Cunnamulla St."],
            ["Albus Dumbledore", 100, "Hogwarts"],
        ]


#print(people[0])
         
for person in people:
    print(person)
    if person[0] == "Slim Dusty":
        print("here he is!")