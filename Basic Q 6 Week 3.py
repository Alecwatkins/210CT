##Week 3 Task 6

##Write the pseudocode for a function that reverses the words in a sentence

##PSEUDOCODE

#Ask user for a sentence to reverse
#INPUT.split()

#WHILE INPUT.length > 0
#OUTPUT = OUTPUT.append(INPUT.pop(-1))
#PRINT(OUTPUT)

sentence = str(input("input the sentence: This is awesome"))
sentence = sentence.split() #Split the sentence into individual words
result = [] #Create output

while len(sentence) > 0: #While there is a word in the original sentence
	result.append(sentence.pop(-1)) #Pop it onto the end of the output (reversing)
print(" ".join(result)) #Join the words back into a sentence

##Big O Runtime = O (N)
