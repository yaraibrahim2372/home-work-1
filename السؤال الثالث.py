def quiz():
    score=0
    questionsRight=0
    fileName = input("Please enter the name of the quiz file: ")
    quizFile = open(fileName,"r")
    quizData = quizFile.readlines()
    questionno=1
    for x in range(20):
        for x in quizData:
            data = x.split(",")
        random.shuffle(quizData)
        questions = data[0]
        CorrectAnswer = data[1]

        print("Question #",questionno)
        print(questions)
        answer = input("What is your answer? ")
        if answer == CorrectAnswer:
            print("Correct!")
            score=score+1
            questionsRight=questionsRight+1
            questionno = questionno+1

        else:
            print("Incorrect.")
            questionno = questionno+1

    totalScore = (score / 10) * 100
    print("You got ",score," questions right, and a score of ",totalScore,"%.")