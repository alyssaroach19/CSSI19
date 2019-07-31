#Create a variable called story
story = """Hey diddle {0}
The {1} and the fiddle
The cow {2} over the moon
The little dog laughed to see such {3}
And the {4} ran away with the spoon
The spoon, the spoon, the spoon, the spoon """

#asking user inputs of removed parts
name = raw_input("Enter a name:")
noun = raw_input("Enter a noun:")
verb = raw_input("Enter a ver:")
ad = raw_input("Enter an adjective:")
place = raw_input("Enter a place:")


#Displays the story using string interpolation
print story.format(name,noun,verb,ad,place)

