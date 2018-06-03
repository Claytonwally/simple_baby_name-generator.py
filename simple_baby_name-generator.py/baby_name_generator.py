from random import randrange

def baby_name():
    print('''This is a very simple program that helps you pick a baby name for a
        girl or a boy ''')
    child_sex=input('Please enter boy for a boy name or girl for a girl name: ')



    def boy_name():
        boys=['Sam', 'Mark', 'William', 'David', 'Stanley', 'Brent', 'Arthur', 'Walter','Clayton', 'Timothy', 'John','James','Ryan','Robert','Zack','Jack','Harry','Don', 'Albert',]
        random_index=randrange(0,len(boys))
        print(boys[random_index])


    def girl_name():
        girls=['Carol','Katrina','Heather','Katherine','Dianne','Wendy','Susan','Penny','Darlene','Sylvia','Sandra','Amelia','Abigail','Audrey','Arianna','Anna','Adeline',
        'Arianna','Annabel','Angela','Bella','Bree','Betty','Belinda','Beatrice', 'Barbara', 'Bethany','Camilla','Crystal','Celine']
        random_index=randrange(0,len(girls))
        print(girls[random_index])


    if child_sex == 'boy':
        boy_name()
    elif child_sex == 'girl' :
        girl_name()
    else:
        print("I don't understand that statement. Please try again.")

    another=input("Would you like to find another baby name: ")
    if(another=='yes'):
        baby_name()
    elif(another=='no'):
        print("I hope we helped you pick the best baby name. ")
    else:
        print("I don't understand that. Please try again")





baby_name()
