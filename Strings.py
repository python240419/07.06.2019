st = "hello python world!"

# print first half of string
print( st[ : len(st) // 2] )

# print second half of string
print( st[ len(st) // 2 : ] )

# uppercase
print( st.upper() )

# lowercase
print( st.lower() )

# check if contains only digits
print( "12345".isdigit() )

# check if contains only characters
print( "abcsew".isalpha() )

# replace "ab" with "12"
print( "abcabd".replace("ab", "12") )

# check if contains only digits
print( "    ".isspace() )

# check if ends with "nny"
print( "dmanydanny".endswith("nny") )

# check if contains "many"
print( "dmanydanny".index("many") > 0)

# switch upper to lower and vice versa
print( "abcsew".swapcase() )
print( "abcsew".swapcase().swapcase() )

# count how many leeters appear
print( len("a b c f r t".split()) )
