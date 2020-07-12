print(["even" if(num%2==0) else "odd" for num in range(5)])



students=[['priya','mukki','dhana','mani'],['CSE','civil','ECE','IT'],[1999,1998,2000,1997]]
students=[[row[i] for row in students] for i in range (len (students[0]))]
print(students)
