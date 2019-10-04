#Meddling with fruits and lists 
data= []
data_dict = {}
#open file
with open("fruits.txt") as infile:
    
    line= infile.readline()
    while line:
        print(line)
        
        print(data_dict)
        if line in data_dict:
            data_dict[line] +=1     
        else:
            data_dict[line] = 1 
        
        line = infile.readline()
  
  #  data= infile.readlines()







#Ignore below
#print(data)

#dictionaries

 

#for word in data:
#    print(word)
#    print(data_dict)
#    if word in data_dict:
#        data_dict[word] += 1
#    else:
#        data_dict[word] = 1

 