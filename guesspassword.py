import random
import genetic
import datetime



def fitness_score(target,guess):
    return sum (1 for correct, guessed in zip (guess,target) if correct == guessed)

def display(guess,startTime):
    diffTime = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(guess.genes,guess.score,diffTime))

def guess_helloWorld():
    target = "Hello World!"   
    guess_password(target)
        
def guess_password(target):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.1234567890"
    startTime = datetime.datetime.now()
    return genetic.get_best(target,geneSet,fitness_score,len(target),display,startTime)
    
    
    
if __name__ == '__main__':     
    guess_helloWorld()


    