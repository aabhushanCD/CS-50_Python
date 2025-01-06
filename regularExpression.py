"""{
        .           any character except a newline

        *           0 or more repetitions
        
        +           1 or more repetitions

        ?           0 or 1 repetition

        {m}         m repetitions

        {m,n}       m-n repetitions 

        ^           matches the start of the string

        $           matches the end of the string just before
                        the newline at the end of the string.

        []          Set of characters

        [^]         complementing the set
    }

    {
        \d          decimal digit

        \D          not a decimal digit

        \s          whitespace characters

        \S          not a whitespace character

        \w          word character....as well as 
                        number and the underscore

        \w          not a word character
    }

    {
        A|B         either A or B
        (....)      a group
        (?:..)      non-capturing version
    }
"""


import re

email = input("What's your email ?").strip()
# Username, domain = email.split("@")
# if (Username) and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")
            
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
