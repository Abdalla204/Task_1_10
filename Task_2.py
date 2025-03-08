Name = "abdala"
age = "19"
country = "Egypt"

print('Hello\'' + Name +'\', How You Doing \\"""' "Yore Age Is"+" "+ "\"" +age + "\"""\"""" + " " +"And Your country Is:"+" "+country )

#
#التكليف الثاني
#  
print('Hello\'' + Name +'\', How You Doing \\"""' "Yore Age Is"+" "+ "\"" +age + "\"""\"""" + "\n" +"And Your country Is:"+" "+country )

#
#التكليف الثالث        
#
name = "Elzero"
print(name [1])
print(name[2])
print(name[-1])

# 
# التكليف الرابع 
# 

print(name[1:4])
print(name[::2])
print(name[-2::-2])

# 
#  التكليف الخامس
# 

Myname = "#@#@#@Abdalla@#@#@#"
print(Myname.strip("@#"))

# 
#  التكليف السادس
# 

a,b,c,d,e = "9","15","130","950","1500"

print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))

# 
#  التكليف السابع
# 

name_one = "Abdalla"
name_two = "Abdalla_Mohamed"
print(name_one.center(27,"@").rstrip("@"))
print(name_two.center(25,"@").rstrip("@"))

 

# 
#  التكليف الثامن
# 

Name_one = "ABdalla"
Name_two = "abdaLLA"
print(Name_one.swapcase())
print(Name_two.swapcase())


# 
#  التكليف التاسع 
# 

msg = "I Love Python And Although Love PHP"
print(msg.count("Love"))

# 
#  التكليف العاشر
# 

name = "Abdall"
print(name.index("d"))

# 
#  التكليف  الحادي عشر
# 

msg_2 = "I <3 python And Although <3 PHP"
print(msg_2.replace("<3","Love",1))

# 
#  التكليف الثاني عشر
# 
print(msg_2.replace("<3","Love"))


# 
#   النكليف الثالث عشر 
# 

Name = "abdala"
Age = 19
country = "Egypt"
print("Myname is, {:s} And My Age Is, {:d} And My country Is, {:s}".format(Name,Age,country))