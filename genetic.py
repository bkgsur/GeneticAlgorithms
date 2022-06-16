from multiprocessing import parent_process
import random
import math

def _generate_parent(targetLength, geneSet):
    genes = []
    while len(genes)<targetLength:
        sampleSize = min(targetLength- len(genes), len(geneSet))
        genes.extend(random.sample(geneSet,sampleSize))
    return ''.join(genes)

def _mutate(parent, geneSet):
    child = list(parent)
    index = random.randrange(0, len(parent))
    alt1,alt2 = random.sample(geneSet,2)
    child[index]= alt2 if child[index]== alt1 else alt1
    return ''.join(child)

def get_best(target, geneSet, fitnessFn, optimalScore, display,startTime):
    targetLength = len(target)
    random.seed()
    parent = _generate_parent(targetLength, geneSet)
    parent_score = fitnessFn(target,parent)
    if(parent_score>=optimalScore):
        display(parent, parent_score)
        return
    while True:
        child = _mutate(parent,geneSet)
        childScore = fitnessFn(target,child)
        
        if(parent_score>=childScore):
            continue
        display(child, childScore,startTime)
        if(childScore>=optimalScore):           
            return child
        parent = child
        parent_score = childScore
    
    