
puncList = [".",";",":","!","?","/","\\",",","#","`","~","@","[","]","{","}","_","'","-","$","&",")","(","\""]

def isPalindrome(s: str) -> bool:
    s = s.lower().replace(' ', '')
    punc = ''
    for punc_ in puncList:
        punc += punc_

    string = ''
    for s_ in s:
        s_ = ''.join(s_.strip(punc))
        string += s_
    print(string)
    if string[::-1] == string:
        return True
    return False


        

# print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))