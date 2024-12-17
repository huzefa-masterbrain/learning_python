line = 'from stephen.marquard@uct.ac.za sat jan 5 09:14:16 2008'
words = line.split()
print(words)

# the double split pattern
# sometimes we split a line one way , and then grab one of the pieces of the line split that piece again

line = "From stephen.Marquard@uct.act.ac.za sat jan 5 09:14:16 2008"
words = line.split()
email = words[1]
print(email)

words = line.split()
email = words[1]
pieces = email.split("@")
print(pieces)

words =line.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])