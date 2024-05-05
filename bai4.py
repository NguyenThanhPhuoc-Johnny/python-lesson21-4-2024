score = 0
def question1():
    global score
    answer = input("When is the first computer invented?: A: 1822, B: 1975, C: 1834, D: 1823. ")
    if answer == "A":
        print("correct")
        score += 2
    else:
        print("incorrect")
        score -= 1
def question2():
    global score
    answer = input("What is the most important mechanic in Honkai Star Rail?: A: Gacha system, B: exploring, C: level up, D: IDK.  ")
    if answer == "A":
        print("correct")
        score += 1
    else:
        print("incorrect")
        score -= 1
def question3():
    global score
    answer = input("How to output onto the screen in python? A: input(), B: OUTPUT, C: print(), D: pintt(). ")
    if answer == "C":
        print("correct")
        score += 1
    else:
        print("incorrect")
        score -= 1
def question4():
    global score
    answer = input("Characteristic of living organism represented by S?: A: Reproduction, B: Sensitivity, C: Excretion, D: Growth. ")
    if answer == "B":
        print("correct")
        score += 1
    else:
        print("incorrect")
        score -= 1
def question5():
    global score
    answer = input("What function is not availiable in python but is availiable in Pseudocode?: A: REPEAT... UNTIL, B: WHILE DO... ENDWHILE, C: IF... ELSE... ENDIF, D: CASE OF... OTHERWISE. ")
    if answer == "A":
        print("correct")
        score += 1
    else:
        print("incorrect")
        score -= 1
def question6():
    global score
    answer = input("How much a programer earns?: A: $50,000 B: $2 million C: $61,116 D: $91,116. ")
    if answer == "D":
        print("correct")
        score += 1
    else:
        print("incorrect")
        score -= 2
def question7():
    global score
    answer = input("How much calories should a average person consumes?: A: 2358 B: 2200 C: 2000 D: 15,000. ")
    if answer == "C":
        print("correct")
        score += 2
    else:
        print("incorrect")
        score -= 2
def question8():
    global score
    answer = input("What is the fastest car in the world?: A: Koenigsegg Jesko Absolut B: Peel P50 C: Koenigsegg Regera D: SSC Tuatara. ")
    if answer == "A":
        print("correct")
        score += 1
    else:
        print("incorrect")
        score -= 2
def question9():
    global score
    answer = input("What happen if you don't drink water in 3 days?: A: dehydration eventually death B: headache C: stomach pain D: still survive. ")
    if answer == "A":
        print("correct")
        score += 1
    else:
        print("incorrect")
        score -= 3
def question10():
    global score
    answer = input("Do you have common sense?: A: 100% B: only 0.2% C: -200% D: 0%. ")
    if answer == "A" or "B" or "C" or "D":
        print("Are you sure you have common sense?")
        print("maybe yes.")
        score += 1000
    else:
        print("How can you even get this wrong?")
        score -= 2000
question1()
question2()
question3()
question4()
question5()
question6()
question7()
question8()
question9()
question10()
print("Score: ",score)
