def answercraker(b):
    ans=int(input('Enter no.  to be your answer :'))
    print('Now follow the procedure\n')

    print('Guess  a number\nif done press enter')
    enter=input()
    print('Double the guessed no.\nif done press enter')
    enter=input()
    print('Add ',ans*2,' to your last answer(i.e answerafter doubling the no.)\nif done press enter')
    enter=input()
    print('divide it by 2\nif done press enter')
    enter=input()
    print('Now, subtract firstly guessed no. from last answer you got(i.e answer after division)\nif done press enter')
    enter=input()
    print('     !!!!!!!!Surpeise!!!!!!!!    you got the answer =',ans,'  which you said me to be your answer. \n Its magic,  thank you!!!!')