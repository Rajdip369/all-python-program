#that is call dictionary
info={
    "key" :"value",
    "name":"rajdip",
    "learning" : "python",
    "age" : 35,
    "is adult":"true",

    "marks":"94.4",
}

#that is call separate name in dictionary 
print(info["name"])
print(info["learning"])
print(info["age"])

#that is how to change a variable in dictionary
info["key"]="chabbi"#overwrite

print (info["key"])

#nested dictionary 
student={
    "name" : "rajdip",
    "score":{
        "chem":98,
        "phy":97,
        "math":95,
    }
}
print(info["age"])
print(student)#for all valu print 

print(student["score"]["math"])#for separate valu print