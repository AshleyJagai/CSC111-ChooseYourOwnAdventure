# CSC111-ChooseYourOwnAdventure-

# Assignment 02 Readme File


## Intro: Choose your own adventure

In this assignment, you should present a series of questions for the user of your program. They should appear a prompts in the console.

Your program should assume that the user will input ONLY valid answers (you are not responsible for bad user input).

After every question and answer (Q&A), you should print a brief text about "what is happening in your story" and follow it up with a next question.

This should repeat until you reach an "Ending".

## Program Requirements

You will add all your code to `main.py`.

The following are rules that I will use to grade,  detailing characteristics that must be present in your program:

  - Your program should not encounter an error anywhere, when the user gives correct input.
  - Each question should have **AT LEAST** 2 possible answers.
  - The **DEPTH** of your story should include **AT LEAST** 3 levels. In other words, the user should encouter at least 3 questions regardless of which "path" they choose.
  - I will take **AT MOST** 10 minutes in grading each assignment, so don't go overboard with the number of options. One should be able to explorte ALL of your story in about 10 minutes.
  - Avoid circular paths!!! Every story should end.
  - You must force python to execute a **main() function**, where you will start your story.
  - You should use **functions** to group similar or related code, but do not use functions to do things that a built_in function can do. One option is to use one function for each story step. So, each one should contain a fragment of a story and a question at the end. The only ones that might be different might be the functions for the "Endings".
  - You **MUST** comment your code. It can be minimal (above each function or IF-statement), but it must be there.
  - (NOTE 1: you need at least 8 different paths to end your story, not necessarily 8 different endings)


## Rubric

  - The program uses conditional statements: 25%
  - The program follows the requirements (conditionals): 20%
  - The program uses functions appropriately: 25%
  - The program follows the requirements (functions): 20%
  - The program is commented correctly: 10%
  - The program has a compilation error: (-50%)

## Tips on how to program this  

  - FIRST draw the story using a diagram of choices (look at the grading problem in Lecture 08)
  - Try some possible input sequences with your diagram to make sure that the logic works (explore "normal cases", "rare cases", etc.) For the minimum number of outcomes (8), it is preferable to check all combinations.
  - Code in segments! That means that you should NOT try to code the whole thing in one go... you should bubild one part and test it wit a few inputs. When that part works, you go in deeper. So on and so forth.
  - You can use print statements as placeholders for the "resto of the program that yo have not coded yet". This allows you to see how far you reach into your program even when you are not done woth the whole task.


## Header and Footer
Note that you are asked to change the info in the "header":
```python
#        Name: <YOUR NAME HERE>
# Course Info: CSC111 - Fall 2021
# Description: Submission for Assignment 1
#        Date: <TODAY'S DATE HERE>
```

Remember that if you collaborated with someone, you should write both names in the header.

In addition, remember to add a block comment - at the very end -  indicating any references you checked when working on this assignment. The following is an example:

```python
# REFERENCES
# I googled "how to format output in python" and used
# <blah 01>.com.
# Also, I googled "how to use eval in python" and used
# <blah 02>.com.
# etc
```

#you've been sent on a quest into an abandon mine shaft
#by a nobel who's rival is plotting their assasination.
# choice - what weapon do you take (gun, knife, stick)
# choice - which type of path 
