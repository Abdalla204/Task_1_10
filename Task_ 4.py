#  
#  التكليف الاول
# 

frinds = ["Hosam" ,"Ali" , "Sayed" ,"Osama" ,"Hoda"]
print(frinds[0])
print(frinds.pop(0))
print(frinds[-1])
print(frinds.pop(-1))


# 
#  التكليف الثاني
# 

frinds = [ "Hosam" ,"Ali" , "Sayed" ,"Osama" ,"Hoda"]
print(frinds[0:3])
print(frinds[3:])

# 
#  التكليف الثالث
# 

frinds = [ "Hosam" ,"Ali" , "Sayed" ,"Osama" ,"Hoda"]
print (frinds[1:4])
print (frinds[-2:])

# 
#  التكليف الرابع
# 

frinds = [ "Hosam" ,"Ali" , "Sayed" ,"Osama" ,"Hoda"]
frinds.remove("Hoda")
frinds.remove("Osama")

frinds.insert(4,"Elzero")
frinds.append("Elzero")

print(frinds)


# 
#  التكليف الخامس
# 

Frinds = ["osama" ,"Ahmed" ,"Sayed"]
Frinds.insert(0,"Ali")
print(Frinds)
Frinds.append("Hosam")
print(Frinds)


# 
#  التكليف السادس
#
 
frinds = [ "Hosam" ,"Ali" , "Sayed" ,"Osama" ,"Hoda"]
frinds[0:2]
print(frinds)
frinds.remove("Hoda")
print(frinds)

#
#  التكليف السابع
# 

frinds = ['Ahmed' ,"Ali" ]
Game = ["rame" ,"Mohamed"]
School = ["Shady", "Hany"]

frinds.extend(Game)
frinds.extend(School)
print(frinds)

# 
#  التكليف الثامن
# 

frinds = ["Camal" , "Hosam" ,"Basma" ,"Shady" ,"Ahmed" , "Donea"]
frinds.sort(reverse=False)
print(frinds)

frinds.sort(reverse=True)
print(frinds)

# 
#  التكليف التاسع 
# 

frinds = ["Camal" , "Hosam" ,"Basma" ,"Shady" ,"Ahmed" , "Donea"]

print(len(frinds))

# 
#  التكليف العاشر
# 

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][-1])