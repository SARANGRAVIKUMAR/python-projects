class greeting:
	x=["hai","holla","hoi","heya","hello hi","howdy","hey there","hi there","greetings","hey","hello","hello there","a god day"]
class python:
	py=["PYTHON","python","py","PY",".PY",".py"]
	class py_abt:
		py_ab=["about python","about py","about .py","python"]
	class py_down:
		py_d=["py download","python download","download python","download py"]
	class py_cou:
		py_c=["python cources","cources related to python","py cources","py cource","python cource"]
		class py_free:
			py_f=["free cources","python free cources","free cource","python free cource","py free cources","py free cource"]
		class py_paid:
			py_p=["paid cources","python paid cources","paid cource","python paid cource","py paid cources","py paid cource"]
class java:
	j=["java",".java"]
print("halo welcome to progro")
x=input()
for i in range(len(greeting.x)):
	if(x.lower()==greeting.x[i]):
 		print ("welcome to progro u can ask anyyting related to programing")
print ("Mention the language you wanna know about \n 1)python \n2)java \n 3)C")
language=input()
for i in range(len(python.py)):
	if (language==python.py[i]):
		print("What do u want to know in python")
		print("1)About python\n2)\n2)download python\n3)python cources")
		py_lang=input()
		for i in range(len(python.py_abt.py_ab)):
			if(py_lang==python.py_abt.py_ab[i]):
				print("Python is a popular programming language. It was created in 1991 by Guido van Rossum.\nIt is used for:\nweb development (server-side),\nsoftware development,\nmathematics,\nsystem scripting.")
				print ("to know more about python go to the link below")
				print ("https://www.w3schools.com/python/python_intro.asp")	
		for i in range(len(python.py_down.py_d)):
			if(py_lang==python.py_down.py_d[i]):
				print("https://www.python.org/downloads/")
				print("from the above site select the version of python and your respective operative system")
			
		for  i in range(len(python.py_cou.py_c)):
			if (py_lang==python.py_d.py_c[i]):
				print ("what kind of cources are you looking for\n1)free cources\n2)paid cources")
				i=0				
				py_cources=input()
				if(py_cources==python.py_cou.py_free.py_f[i]):
					print ("vist these sites for free python cources")
					print("python.org:https://www.python.org/doc/")
					print("data camp:https://www.datacamp.com/courses/intro-to-python-for-data-science")
					print("courcecera:https://www.codecademy.com/catalog/language/python")
i=0
for i in range(len(java.j)):
	if(language==java.j[i]):
		print("what do u want to know in java?")
		print("1)About java\n2)\n2)download java\n3)java cources")




