#inner class
#class date:
#    def __init__(product,day,month,year):
#        product.day=day
#        product.month=month
#        product.year=year
#    def getday(product):
#        return product.day
#    def getyear(product):
#        return product.year
#    def getmonth(product):
#        return product.month
#    def setday(product,day):
#        product.day=day
#    def setmonth(product,month):
#        product.month=month
#    def setyear(product,year):
#        product.year=year

#class car:
#    def __init__(my,name,model,product_day):
#        my.name=name
#        my.model=model
#        my.product_day=product_day
#    def getname(my):
#        return my.name
#    def getmodel(my):
#        return my.model
#    def getdate(my):
#        return my.product_day
#    def setname(my,name):
#        my.name=name
#    def setmodel(my,model):
#        return my.model

#def printcar(i):
#    print(i.name)
#    print(i.model)
#    print(str(i.getdate().getday())+" "+str(i.getdate().getmonth())+" "+str(i.getdate().getyear()))

##declaring object
#newday=date(13,6,2021)
#mycar=car("BMW","M3",newday)

##change date
#mycar.getdate().setday(23)
#print(mycar.getdate().getday())


#printcar(mycar)


#inher. with inner class
class student:
    def __init__(his,name,age,city):
        his.name=name
        his.age=age
        his.city=city

class male(student):
    def __init__(his,name,age,city):
        super().__init__(name,age,city)
    def setname(his,name):
        his.name=name
    def setage(his,age):
        his.age=age
    def setcity(his,city):
        his.city=city

class female(student):
    def __init__(her,name,age,city,grade):
        super().__init__(name,age,city)
        her.grade=grade
    def setname(her,name):
        her.name=name
    def setage(her,age):
        her.age=age
    def setcity(her,city):
        her.city=city
    def setgrade(her,grade):
        her.grade=grade

class teacher(student):
    def __init__(his,name,age,city,subject):
        super().__init__(name,age,city)
        his.subject=subject
    def setsub(his,sub):
        his.subject=sub

class classroom:
    def __init__(room,malestudents,femalestudents,teacher):
        room.malestudents=malestudents
        room.femalestudents=femalestudents
        room.teacher=teacher
    def insert_malestudent(room,males):
        room.malestudents.append(males)
    def insert_femalestudent(room,females):
        room.femalestudents.append(females)
    def by_malename(room,name):
        for male in room.malestudents:
            if male.name==name:
                return male
    def by_femalename(room,name):
        for female in room.femalestudents:
            if female.name==name:
                return female
    def remove_malestudent_by_name(room,name):
        room.malestudents.remove(room.by_malename(name))
    def remove_femalestudent_by_name(room,name):
        room.femalestudents.remove(room.by_femalename(name))
                

class school:
    def __init__(sc,classroom):
        sc.classroom=classroom
    def insert_classroom(sc,addclassroom):
        sc.classroom.append(addclassroom)
    def getclassroom(sc,teacher_name):
        for eachroom in sc.classroom:
            if eachroom.teacher.name==teacher_name:
                return eachroom
    def deleteclassroom(sc,teacher_name):
        sc.classroom.remove(sc.getclassroom(teacher_name))

            
        

#delcaring
Ana=female("Ana",32,"Orange",93)
Sally=female("Sally",33,"Chino",82)
Ian=male("Ian",25,"Gardena")
Jason=male("Jason",28,"Torrance")
Anson=teacher("Anson",45,"Irvine","math")

#put variable in list
malestudentlist=[Ian,Jason]
femalestudentlist=[Ana,Sally]

#send those info. to classroom1
classroom1=classroom(malestudentlist,femalestudentlist,Anson)
#send classroom1 in a list
allclassroom=[classroom1,]
some_college=school(allclassroom)

John=male("John",23,"San Diego")
some_college.classroom[0].insert_malestudent(John)

#-------------------------------------------------------------------------
#declaring
Uno=female("Uno",19,"sky",79)
Queen=female("Queen",24,"Santa Ana",90)
King=male("King",35,"xxx")
Cat=male("Cat",31,"somewhere")
me=teacher("me",56,"Hell","CS")

#put variable in list
malestudentlist1=[King,Cat]
femalestudentlist1=[Uno,Queen]

#send those info. to classroom2
classroom2=classroom(malestudentlist1,femalestudentlist1,me)
some_college.insert_classroom(classroom2)

some_college.classroom[0].teacher.setsub("History")


for classr in some_college.classroom:
    print("Teacher: "+classr.teacher.name+" "+classr.teacher.subject)
    for students in classr.femalestudents:
        print(students.name+" "+str(students.age)+" "+students.city+" "+str(students.grade))
    for students in classr.malestudents:
        print(students.name+" "+str(students.age)+" "+students.city)
    print()

print("-----------------------------------------------------------------------")

some_college.classroom[0].remove_malestudent_by_name("Jason")
some_college.classroom[1].remove_femalestudent_by_name("Uno")

for classr in some_college.classroom:
    print("Teacher: "+classr.teacher.name+" "+classr.teacher.subject)
    for students in classr.femalestudents:
        print(students.name+" "+str(students.age)+" "+students.city+" "+str(students.grade))
    for students in classr.malestudents:
        print(students.name+" "+str(students.age)+" "+students.city)
    print()

print("-----------------------------------------------------------------------")

some_college.deleteclassroom("me")
for classr in some_college.classroom:
    print("Teacher: "+classr.teacher.name+" "+classr.teacher.subject)
    for students in classr.femalestudents:
        print(students.name+" "+str(students.age)+" "+students.city+" "+str(students.grade))
    for students in classr.malestudents:
        print(students.name+" "+str(students.age)+" "+students.city)
    print()
