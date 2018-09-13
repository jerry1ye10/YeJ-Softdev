# Jerry Ye and Ivan Zhang -- whatevez
# SoftDev1 pd07
# K #02: NO-body expects the Spanish Inquisition!
# 2018-09-07  

import random

# Allows the user to input a team (Cap sensitive)
team = input("What team shall it be(Please pick from w, m, or x): ")

if team in "wmx" and len(team) == 1: # Checks to make sure that user input is one of the teams ("w", "m", or "x")
	
	# Provided Dictionary {TEAM:LIST_PEOPLE, TEAM:LIST_PEOPLE, ...}
	KREWES = {
	        'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],
	        'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],
	        'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']
	}

	team_members = KREWES[team] # Gets the list of the members in the team

	rand_member = random.choice(team_members) # Chooses one of the members of the team

	print(rand_member) # Prints the random team member

else:
	print("Team does not exist") # User's input is not a valid team

