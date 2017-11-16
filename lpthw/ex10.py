#This is lesson 10 from "Learn Python the Hard Way"
#assign different escapes to variables
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm\\a\\cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#testing different escape sequences
# \\ : Backslash (\)
testBackslash = "h\\e\\l\\l\\o\\?"
test2Backslash = "h\e\l\l\o?"
print(testBackslash)
print(test2Backslash)

#\' : Single-quote (')
testSinglequote = 'It\'s my birthday on November 7th'
print(testSinglequote)

#\" : Double-quote (")
testDoublequote = "\"Testing\"."
print(testDoublequote)

#\a : ASCII bell (BEL)
testAB = "test\atest\atest"

#\b : Backspace (bs)
testBackspace = "BACK\bSPACE"
print(testBackspace)

#\f : Formfeed (ff)
testFormfeed = "formfeed\fformfeed"
print(testFormfeed)

#\n : Linefeed (lf)
testLinefeed = "Line\nfeed"
print(testLinefeed)

#\r : Return (cr)
testReturn = "Return1\rReturn2\rReturn3\rReturn4"
print(testReturn)

#\t : Tab (tab)
testTab = "TAB[\t]"
print(testTab)

#\v : Vertical Tab (vt)
testVerticaltab = "test\vtest\vtest"
print(testVerticaltab)
