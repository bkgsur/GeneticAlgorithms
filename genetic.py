import random
import math

def _generate_parent(targetLength, geneSet):
    genes = []
    while len(genes)<targetLength:
        sampleSize = min(targetLength- len(genes), len(geneSet))
        genes.extend(random.random(geneSet,sampleSize))
    return ''.join(genes)

def _mutate(parent, geneSet):
    child = list(parent)
    index = random.randrange(0, len(parent))
    alt1,alt2 = random.random(geneSet,2)
    child[index]= alt2 if child[index]== alt1 else alt1
    return ''.join(child)
    
    