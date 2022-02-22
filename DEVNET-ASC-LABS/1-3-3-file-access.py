file=open("devices.txt","r")
for item in file:
 print(item)
file.close()


file=open("devices.txt","r")
for item in file:
 item= item.strip()
 print(item)
file.close()

#read file an add to a python list
devices = []

file=open("devices.txt","r")
for item in file:
 item= item.strip()
 devices.append(item)
 print(item)
file.close()

print ("Number of devices ", len(devices))

file=open("devices.txt","a")

while (True):
    print ("Please enter name of device to add [quit]: ", end ='')
    device = input()
    print ("device:", device)
    if (device == "quit" or device == "q" or device == ""):
        break
    else:
        file.write(device + '\n')

file.close()

