from multiprocessing import parent_process
import random
import math

class Chromosome:
    genes=None
    score = None 
    def __init__(self,g,f):   
        self.genes=g
        self.score=f

def _generate_parent(target, geneSet, fitnessFn):
    genes = []
    while len(genes)<len(target):
        sampleSize = min(len(target)- len(genes), len(geneSet))
        genes.extend(random.sample(geneSet,sampleSize))
    g = ''.join(genes)
    f = fitnessFn(target,g)
    c = Chromosome(g,f)  
    return c

def _mutate(parent, geneSet, target, fitnessFn):
    child = list(parent.genes)
    index = random.randrange(0, len(parent.genes))
    alt1,alt2 = random.sample(geneSet,2)
    child[index]= alt2 if child[index]== alt1 else alt1
    g = ''.join(child)
    f = fitnessFn(target,g)
    c = Chromosome(g,f)  
    return c

def get_best(target, geneSet, fitnessFn, optimalScore, display,startTime):
    targetLength = len(target)
    random.seed()
    parent = _generate_parent(target, geneSet,fitnessFn)    
    if(parent.score>=optimalScore):
        display(parent,startTime)
        return
    while True:
        child = _mutate(parent,geneSet, target,fitnessFn)    
        if(parent.score>=child.score):
            continue
        display(child,startTime)
        if(child.score>=optimalScore):           
            return child
        parent = child        
    
    