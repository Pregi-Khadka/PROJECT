import csv
print('.......................PHONE BOOK.......................')
check=0
with open('phonebook.csv','a+') as f:
    f.seek(0)
    while check!=3:
        print('''type  1  for view contact list \n type  2  for add contact number\n type  3  for exti''')
        check=int(input())
        f.seek(0)

        if check==1:

            checkall=input('Press  a  for view all contact list \n Press  p  for particular contact list:')
            if checkall=='a':
                print(f.read(),'\n press any key\n')
                enter=input()
                f.seek(0)
            else:
                name=str.lower(input('Enter name of particular person:'))
                t=0
                while t==0:
                    readed=f.readline()
                    readed=readed.split(',')
                    if readed[0]==name:
                        print('Phone no. of ','='.join(readed),'\n')
                        t=1


        elif check==2:
            nlist=str.lower(input('Name and Phone no.(For eg: John,9823542334) : '))
            nlist=nlist.split(",")
            writer=csv.writer(f)
            writer.writerow(nlist)
            f.seek(0)
print('\n press any key')
a=input()

           
from ANSWER_CRACKER import answercraker
print("\nSoo, of you are boored then let's play one intresting game , okay.\n")
a=input()
print('..................................ANSWER CRAKER..................................\n')
print(answercraker(a))

    
    


