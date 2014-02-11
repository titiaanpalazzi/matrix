def matrix():
	print "Will you take the blue pill or the red pill?"
	answer = raw_input("Type red or blue and hit enter.").lower()
	if answer == "red":
		print "Welcome to reality, Neo."
	else:
		print "Bzzzz. Bzzzz. Time to wake up for work!"
matrix()