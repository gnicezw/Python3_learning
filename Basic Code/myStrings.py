#python3 code for Strings and Format strings
str_1 = "The first number is"
str_2 = "The second number is"
str_a = "aaa"
str_b = "bbb"
str_c = "ccc"
str_curly = "{}"
int_j = 7
int_k = 9
int_l = 24
str_metro ="Jakarta"
int_pop = 30000000

print("declaring other data types within strings")
#str_al = str_a + int_l
print("\r")
print("concatenating strings via the space operator")
str_space = "sss"  "jjj"\
"ooo" "qqq"\
        "zzz"
print(str_space)
print("\r")
print("Using the str() function only\ne.g print(str_1 +\" \" + str(int_j) + \" and \" + str(int_k))")
print(str_1 +" " + str(int_j) + " and " + str_2 + " " + str(int_k))
print("\r")
print("joining strings in sequence e.g print(str_a str_b str_c)")
print("^^ this does not work")
#print(str_a str_b str_c)
print("\r")
print("joining strings in sequence e.g print(\"ddd\" \"eee\" \"fff\")")
print("ddd" "eee" "fff")
print()
print("\r")
print("Using the format() function e.g print(\"{}{}\".format(str_1, int_j))")
print("{} {}". format(str_1, int_j))
print("\r")
str_cities = "{} with a population of {} is the main metropolis "\
"on Java island".format(str_metro, int_pop)  #used backslash op for readability
print(str_cities)

