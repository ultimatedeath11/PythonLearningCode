from sys import argv

script, user_name = argv
#script is predetermined to be the name of the file
#username is the one thing to unpack 
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is, I will check google.
And you have a %r computer. Nice!!!
""" % (likes, lives, computer)
