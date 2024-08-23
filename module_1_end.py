grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johny','Bilbo','Steve','Khendrik','Aaron'}
dict_={}
new_stud=list(students)
new_stud.sort()
dict_.update({new_stud[0]:sum(grades[0])/len(grades[0]),new_stud[1]:sum(grades[1])/len(grades[1]),
              new_stud[2]:sum(grades[2])/len(grades[2]),new_stud[3]:sum(grades[3])/len(grades[3]),
              new_stud[4]:sum(grades[4])/len(grades[4]),})
print('Средний бал учеников в алфавитном порядке: \n',dict_)
#dict.update(new_stud[0]:grades[0])