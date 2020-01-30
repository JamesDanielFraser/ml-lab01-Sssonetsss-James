
"""
Lab set 01 - Project 01 - Re-acquainting with Python

01.02 - 10 pts.
"""

# First let's try reading in and displaying the sonnets.

# Read in the file for all the sonnets along with the header and footer garbage
filename = "wssnt10.txt"

with open(filename) as f:
    dirtyContent = f.readlines()
'''singleSpacedContent = []
for eachLine in content:
    if len(eachLine) > 2:
        singleSpacedContent.append(eachLine)
        print(eachLine)
# you may also want to remove whitespace characters like `\n` at the end of each line
'''
def Get_Clean_Gluten(content):
    halfwaymark = len(content)//2
    print(halfwaymark)
    listOfGutenIndexes = []
    listOfUpperGutenIndexes = []
    listOfLowerGutenIndexes = []
    for eachIndex in range(len(content)):
        if "Project Gutenberg" in content[eachIndex]:
            listOfGutenIndexes.append(eachIndex)
        for eachGutenIndex in listOfGutenIndexes:
            if eachGutenIndex > halfwaymark:
                listOfLowerGutenIndexes.append(eachGutenIndex)
            if eachGutenIndex < halfwaymark:
                listOfUpperGutenIndexes.append(eachGutenIndex)
    beginningOfText = listOfUpperGutenIndexes[-1]
    beginningOfText += 2
    #print(beginningOfText)
    #print(content[beginningOfText])
    endOfText = listOfLowerGutenIndexes[0]
    endOfText -= 1
    #print(endOfText)
    #print(content[endOfText])
    cleanContent = content[277:2910]
    shitList = ["\n"]
    singleSpacedContent = []
    for eachLine in cleanContent:
        if len(eachLine) > 2:
            newText = ''
            for eachCharater in eachLine:
                if eachCharater not in shitList:
                    newText += eachCharater
            singleSpacedContent.append(newText)
            print(eachLine)
    return singleSpacedContent


print(Get_Clean_Gluten(dirtyContent))
'''content = [x.strip() for x in content]   # list comprehension !!!
'''

# equivalent to...
'''
content = []
for x in content:
    content.append( x.strip() )
'''
# print the number of lines in the file

# Print the entire sonnet file to the console, without the extra line breaks!







