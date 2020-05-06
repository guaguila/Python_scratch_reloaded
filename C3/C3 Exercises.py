#TRY IT YOURSELF
invites = ['Jesus', 'wife', 'son', 'neighbor']
print ("\nDear " + invites[0]) + " I would like to invite you to my house."

print ("Dear " + invites[1]) + " I would like to go out with you."

print ("Dear " + invites[2]) + " I would like to be your best friend."

print ("\nOur dear " + invites[3] + " won't be able to attend.") 

del invites[3]

invites.append('Church')

print ("\nDear " + str(invites) + " we want to invite you to our party")

print ("\nDear " + str(invites[0]) + ", " 
				 + str(invites[1]) + ", " 
				 + str(invites[2]) + " and " 
				 + str(invites[3])  
				 + " we would like to invite you to our party")


invites.insert(0, 'GOD')
invites.insert(2, 'Holy Spirit')
invites.append('neighbors')

print ("\nDears " + str(invites[0]) + ", " 
				  + str(invites[1]) + ", " 
				  + str(invites[2]) + ", " 
				  + str(invites[3]) + ", "
				  + str(invites[4]) + " and " 
				  + str(invites[5]) 
				  + " we would like to invite you to our great party!")


print ("\nFriends we have some changes. We would invite just two groups")
popped_invite = invites.pop()
print (popped_invite)
print ("\nSorry " + popped_invite + " this will be a private event.")


popped_invite = invites.pop()
print ("\nSorry " + popped_invite + " this will be a private event.")

print ("\n\tMy beloved " + str(invites) + " you are on my heart and pray for the souls to love them")


print (len(invites), "invitados")



