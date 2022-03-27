
#Joseph Espiritu Roman Numeral Calculator: I could not get my calculator to work unfortunatelly in the allotted time.
# In the comments you can see a high level version of what I was attempting to due, but could not figure out.
# Thank you for your time.

# create a class to convert roman numerals to integer
class NumeralCalculator :
    # Method to convert the numerals

    def convertNumerals(self, iNumeral):

        
    # Attempt to create dictionary pair values for each roman numeral
        # dictRomanNumerals = {
        # "I" : 1,
        # "IV": 4,
        # "V" : 5,
        # "IX": 9,
        # "X" : 10,
        # "XL": 40,
        # "L" : 50,
        # "XC": 90,
        # "C" : 100,
        # "CD": 400,
        # "D" : 500,
        # "CM": 900,
        # "M" : 1000
        # }
    
    #Created two separate lists for Roman Numerals and Values
        listRomanNumerals = listRomanNumerals['I', 'IV', 'V', 'IX', 'X', 'XL', 'XC', 'C', 'CD', 'CM', 'M']
        listRomanNumeralValue = [5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        
    #Create loop that iterates throughboth lists to convert user input to the calculated integer
        iNumeral = input("Enter your roman Numerals: ")
        # This loop would go through the range of however big the Roman numeral is inputed in
        for i in range(0, len(iNumeral)):
            # This attempt is to see if the position of the value == the first value of the listRomanNumerals list
            if iNumeral[i] == listRomanNumerals[0]:
                # this would change the value of iNumeral to the value of the listRomanNumeralValuelist
                iNumeral[i] == listRomanNumeralValue[0]
                #This next line of code would theoretically go to the number on the list
                listRomanNumeralValue[0] = listRomanNumeralValue[0] + 1
            # These elif statement swould see if the iNumeral + the next character equalled to the double roman numerals 
            # listed, such as IV, IX, XL, XC, CD, or CM and change the value of the iNumeral to the listRomanNumeralValue
            elif iNumeral[i] + iNumeral[i] + 1 == listRomanNumerals[1]:
                iNumeral = listRomanNumeralValue[1]
            elif iNumeral[i] + iNumeral[i] + 1 == listRomanNumerals[3]:
                iNumeral = listRomanNumeralValue[3]
            elif iNumeral[i] + iNumeral[i] + 1 == listRomanNumerals[5]:
                iNumeral = listRomanNumeralValue[5]
            elif iNumeral[i] + iNumeral[i] + 1 == listRomanNumerals[6]:
                iNumeral = listRomanNumeralValue[6]
            elif iNumeral[i] + iNumeral[i] + 1 == listRomanNumerals[8]:
                iNumeral = listRomanNumeralValue[8]
            elif iNumeral[i] + iNumeral[i] + 1 == listRomanNumerals[9]:
                iNumeral = listRomanNumeralValue[9]
            else:
                listRomanNumerals[0] = listRomanNumerals[0] + 1 
        
        # print out calculated answer
        print("Your input is equal to: ", iNumeral)
        


    



