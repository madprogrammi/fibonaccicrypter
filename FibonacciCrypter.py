#!/usr/bin/python
import math
import sys
import time

def percent(part, total):
	return 100 * float(part)/float(total)

def WriteDataToFilePrompt(data, newline):
	filename = input("Filename: ")
	file = open(filename, 'w')
	location = 0
	while location < len(data):
		if newline == True:
			file.writelines(data[location] + "\n")
		else:
			file.writelines(data[location])
		location += 1
	file.close()
	
class Fibonacci():
	def __init__(self):
		pass
	def Single(self, n): # Returns a single Fibonacci number
		if n == 0: return 0
		elif n == 1: return 1
		else: 
			return self.Single(n-1)+self.Single(n-2)
	def SetOfFibonacci(self, start, end): # Returns a set of Fibonacci numbers from start to end.
		returnData = []
		location = start
		while location < end:
			returnData.append(str(self.Single(location)))
			location += 1
		return returnData

fib = Fibonacci()
encryptionList = fib.SetOfFibonacci(1,11)
class FibonacciEncryption():
	def __init__(self):
		pass
	def Encrypt(self, textToEncrypt):
		location = 0
		encryptedText = []
		offsetIndex = 0
		while location < len(textToEncrypt):
			if offsetIndex < 9:		# Let's make sure we keep it in-bounds.
				offsetIndex += 1
			elif offsetIndex == 9:
				offsetIndex = 0
			charValue = ord(textToEncrypt[location])
			offsetValue = encryptionList[offsetIndex]
			finalValue = int(charValue) + int(offsetValue)
			encryptedText.append(str(finalValue))
			location += 1
		location = 0
		finalString = ""
		while location < len(encryptedText):
			finalString += str(encryptedText[location])
			if location != len(encryptedText):
				finalString += " "
			location += 1
		return finalString
	def Decrypt(self, textToDecrypt): # Anything other than a string input will break this
		location = 0
		decryptedText = ""
		offsetIndex = 0
		nextwhitespace = 0
		while location < len(textToDecrypt):
			if offsetIndex < 9:
				offsetIndex += 1
			elif offsetIndex == 9:
				offsetIndex = 0
			nextwhitespace = textToDecrypt.find(" ", location)
			if nextwhitespace != -1:
				tempTextToDecrypt = textToDecrypt[location:nextwhitespace]
				offsetValue = encryptionList[offsetIndex]
				finalText = chr(int(tempTextToDecrypt) - int(offsetValue))
				decryptedText += finalText
			if nextwhitespace < location:
				return decryptedText
			else:
				location = nextwhitespace + 1
			
fibe = FibonacciEncryption()

print("Encryption list: " + str(encryptionList))
print(str(sys.argv))
# Before we go into user-mode, check for if we have commandline options or not.
try:
	outputFilename = ""
	inputFilename = ""
	final = []
	if sys.argv[1] == "--encrypt":
		if sys.argv[3] =="--output": # This will see if there's a third argument
			if sys.argv[4] == sys.argv[4]: # And a fourth
				outputFilename = sys.argv[4]
				inputFilename = sys.argv[2]
				inputFile = open(inputFilename, 'r')
				inputLines = inputFile.readlines()
				location = 0
				while location < len(inputLines):
					final.append(fibe.Encrypt(inputLines[location]))
					location += 1
	elif sys.argv[1] == "--decrypt":
		if sys.argv[3] == "--output":
			if sys.argv[4] == sys.argv[4]: 
				outputFilename = sys.argv[4]
				inputFilename= sys.argv[2]
				inputFile = open(inputFilename, 'r')
				inputLines = inputFile.readlines()
				location = 0
				while location < len(inputLines):
					final.append(fibe.Decrypt(inputLines[location]))
					location += 1
	elif sys.argv[1] == "--help":
		print("Usage: FibonacciCrypter.py [--encrypt/--decrypt] --output <filename>")
		print("Example: FibonacciCrypter.py --encrypt hello.txt --output hello-encrypted.txt")
		print("Example: FibonacciCrypter.py --decrypt hello-encrypted.txt --output hello.txt")
		print("--output specifies the file that the finished encryption/decryption will be written to.")
		print("--encrypt specifies that you want to encrypt a file. The following argument must be a filename.")
		print("--decrypt specifies that you want to decrypt a file. The following argument also must be a filename.")
	else:
		pass
	outputFile = open(outputFilename, 'w')
	location = 0
	while location < len(final):
		if sys.argv[1] == "--encrypt":
			outputFile.writelines(final[location] + "\n")
		elif sys.argv[1] == "--decrypt":
			outputFile.writelines(final[location])
		location += 1
	outputFile.close()
	sys.exit(1)
except IndexError:
	print("Error while parsing commandline options! Dropping into manual input mode.")
except FileNotFoundError:
	print("Error while parsing commandline options! FileNotFoundError. The input file could not be found. Please check your command arguments and try again!")
	sys.exit(2)
# From now on, we shall drop into usermode
while -1:
	edAnswer = input("(e)ncrypt or (d)ecrypt? ")
	if edAnswer == "e":
		sfAnswer = input("(s)tdin or (f)ile? ")
		if sfAnswer == "s":
			inputToEncrypt = input("Text: ")
			print("Finished! Encrypted data is: " + str(fibe.Encrypt(inputToEncrypt)))
		elif sfAnswer == "f":
			filename = input("Filename: ")
			file = open(filename, 'r')
			lines = file.readlines()
			final = []
			location = 0
			while location < len(lines):
				final.append(fibe.Encrypt(lines[location]))
				location += 1
				percentString = str(percent(location, len(lines)))
				percentString = percentString[:percentString.find(".")+2]
				sys.stdout.write(percentString + "%\r")
			#print(str(final))
			print("")
			while -1:
				outputToFile = input("Would you like to save this output to a file? (y)es/(n)o: ")
				if outputToFile.lower() == "y":
					WriteDataToFilePrompt(final, True)
					break
				elif outputToFile.lower() == "n":
					break
				else:
					pass
	elif edAnswer == "d":
		while -1:
			sfAnswer = input("(s)tdin or (f)ile? ")
			if sfAnswer.lower() == "s":
				inputToDecrypt = input("Text: ")
				print("Finished! Decrypted data is: " + str(fibe.Decrypt(inputToDecrypt)))
				break
			elif sfAnswer.lower() == "f":
				filename = input("Filename: ")
				file = open(filename, 'r')
				lines = file.readlines()
				final = []
				location = 0
				while location < len(lines):
					final.append(fibe.Decrypt(lines[location]))
					location += 1
					if 10 % location == 0:
						percentString = str(percent(location, len(lines)))
						percentString = percentString[:percentString.find(".")+2]
						sys.stdout.write(percentString + "%\r")
				#print(str(final))
				print("")
				while -1:
					outputToFile = input("Would you like to save this output to a file? (y)es/(n)o: ")
					if outputToFile.lower() == "y":
						WriteDataToFilePrompt(final, False)
						break
					elif outputToFile.lower() == "n":
						break
					else:
						pass
				break