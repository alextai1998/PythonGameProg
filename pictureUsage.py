"""
This program walks the use through several yes or no questions that will determine whether or not the user may use a picture.
This program will return a final verdict after all the questions are answered.
"""

import sys

print("Want to know if you can use a specific picture?")
print("Answer the following questions to find out!")
print(" ")  # Printing blank line


# Determines the verdict
if input("Did you take or create the image yourself? (y/n) ") == "y":
    if input("Was the picture you created an original idea? (y/n) ") == "y":
        sys.exit("Yes")
    else:
        sys.exit("No")
else:
    print("Ask yourself the Fair Use Questions")
    if input("Are you using the image for personal, non-profit, educational, research, or scholarly purposes AND are you using the image sparingly, only for limited purposes? (y/n) ") == "y":
        sys.exit("Yes")
    else:
        if input("Are you transforming or repurposing the image to create a new purpose or meaning? (y/n) ") == "y":
            sys.exit("Yes")
        else:
            if input("Are you publishing the image in a fact-based context or publication that benefits the public as a whole (such as in a news source where it is important that people see the image)? (y/n) ") == "y":
                sys.exit("Probably")
            else:
                if input("Would it be considered impossible to obtain permission from the original source? (y/n) ") == "y":
                    sys.exit("Yes")
                else:
                    answer = input("Will you be using the image for personal or commercial gain? (If you answered 'n' to all the fair use questions, the use of your image would most likely be considered for personal or commercial gain.) (y/n) ")
                    if answer == "y":
                        if input("Is the image in the public domain or protected by creative commons agreements? (y/n) ") == "y":
                            sys.exit("Yes")
                        else:
                            if input("Did you purchase the image or obtain permission from the original source? (y/n) ") == "y":
                                sys.exit("Yes")
                            else:
                                sys.exit("No")
                    else:
                        while answer != "y":
                            if input("Are you using the image for personal, non-profit, educational, research, or scholarly purposes AND are you using the image sparingly, only for limited purposes? (y/n) ") == "y":
                                sys.exit("Yes")
                            else:
                                if input("Are you transforming or repurposing the image to create a new purpose or meaning? (y/n) ") == "y":
                                    sys.exit("Yes")
                                else:
                                    if input("Are you publishing the image in a fact-based context or publication that benefits the public as a whole (such as in a news source where it is important that people see the image)? (y/n) ") == "y":
                                        sys.exit("Yes")
                                    else:
                                        if input("Would it be considered impossible to obtain permission from the original source? (y/n) ") == "y":
                                            sys.exit("Yes")
                                        else:
                                            answer = input("Will you be using the image for personal or commercial gain? (If you answered 'n' to all the fair use questions, the use of your image would most likely be considered for personal or commercial gain.) (y/n) ")
                        if input("Is the image in the public domain or protected by creative commons agreements? (y/n) ") == "y":
                            sys.exit("Yes")
                        else:
                            if input("Did you purchase the image or obtain permission from the original source? (y/n) ") == "y":
                                sys.exit("Yes")
                            else:
                                sys.exit("No")
