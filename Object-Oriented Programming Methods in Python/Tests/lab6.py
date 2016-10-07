def find(text, string):
    if len(string) > len(text):
        return False
    for i in range(len(string)):
        if text[i] != string[i]:
            return find(text[1:], string)
    return True

print(find("Mississippi", "sip"))
print(find("HelloWorld", "Love"))
print(find("HelloWorld", "Hell"))


#output
"""
>>> ================================ RESTART ================================
>>> 
True
False
True
>>> 
"""
