#Declare a dictionary
ipAddress={"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}
print("Number of keys:", len(ipAddress), type (ipAddress))

#Add another key
ipAddress["R4"] = "10.4.4.1"
print("Number of keys:", len(ipAddress), type (ipAddress))
#update a key value
ipAddress["R1"] = "10.1.1.2"
#Access Values
print("ipAddres:", ipAddress)
print("ipAddess[R1]:", ipAddress["R1"])

for key in ipAddress:
    print (key)

for key in ipAddress:
    print (ipAddress[key])   

for key, value in ipAddress.items(): 
    print ("Key:", key, "Value:", value)   


ipAddress["R5"] = [ "10.5.5.1", "10.5.5.5"]

print(ipAddress["R5"])
print(ipAddress)

for key, value in ipAddress.items(): 
    print ("Key:", key, "Value:", value)
    if key == "R5":
        print ("length of list is ", len(value)) 
        print ("Firstitem in list is: ", value[0]) 
        for i in value:
            print ("R5 ipAddress", i)


devices = ["R1", "R2", "R3", "S1" , "S2" ]
switches = []

for i in devices:
    if "R" in i:
        print ("Router is detected", i)
    if "S" in i:
        switches.append(i)

print("Switches", switches)