# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam= ['apples', 'bananas', 'tofu', 'cats']list to
# the function would return 'apples, bananas, tofu, and cats'.

def comma_code(l):
    commaCode = ""
    i=0
    while i< len(l)-1:
        commaCode += l[i] + ", "
        i+=1
    commaCode += "and " + l[i]
    return commaCode

if __name__ == "__main__":
    print(comma_code(["a", "b", "c"]))

