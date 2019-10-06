#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("FirstName", "не задано")
text2 = form.getfirst("LastName", "не задано")
text1 = html.escape(text1)
text2 = html.escape(text2)

#отримання даних з полів 
if form.getvalue('maths'):
	maths_flag = "Так"
else:
    maths_flag = "Ні"	

if form.getvalue('physics'):
	physics_flag = "Так"
else:
    physics_flag = "Ні"

if form.getvalue('khimiya'):
	khimiya_flag = "Так"
else:
    khimiya_flag = "Ні"	

if form.getvalue('biolohiya'):
	biolohiya_flag = "Так"
else:
    biolohiya_flag = "Ні"	 

if form.getvalue('lang'):
	lang = form.getvalue('lang')
else:
    lang = "Не вибрано"	       


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обробка даних форм</title>
        </head>
        <body>""")

print("<h1>Обробка даних: </h1>")
print("<p>Прізвище: {}</p>".format(text1))
print("<p>Імя: {}</p>".format(text2))
print("<p>Математика: %s</p>" %maths_flag )
print("<p>Фізика: %s</p>" %physics_flag )
print("<p>Хімія: %s</p>" %khimiya_flag )
print("<p>Біологія: %s</p>" %biolohiya_flag )
print("<p>Мова: %s</p>" %lang)


print("""</body>
        </html>""")