from brain import *
from random import randint, randrange
import csv

#Setup Functions

def setupSmolBrain(n=0):
    smolBrain = Brain(n)
    smolBrain.addNeuron()
    n0 = smolBrain.neurons[0]
    smolBrain.addNeuron()
    n1 = smolBrain.neurons[1]
    smolBrain.addNeuron()
    n2 = smolBrain.neurons[2]
    n1.surgery(n0, n2)
    return smolBrain

def setupRandomBrain(n=0, minNeurons=100, maxNeurons=500, minAxons=100, maxAxons=500):
    randBrain = Brain(0)
    for i in range(randrange(minNeurons, maxNeurons)):
        randBrain.addNeuron()
    for i in range(randint(minAxons, maxAxons)):
        randBrain.neurons[randrange(0, randBrain.size())].surgery(randBrain.neurons[randrange(0, randBrain.size())], randBrain.neurons[randrange(0, randBrain.size())])

def generateBrainData(brain=setupSmolBrain(), maxTime=100, minCount=10, maxCount=100):
    firingList = []
    for i in range(randrange(minCount, maxCount)):
        for i in range(randint(0, len(brain.neurons))):
            time = randrange(1, maxTime)
            firingList.append((time, brain.neurons[i].id, "fire"))
    with open('randomSmolBrainData.csv', 'w', newline='') as csvfile:
        brainwriter = csv.writer(csvfile)
        brainwriter.writerows(firingList)
    print("Generated Data")
    return firingList

#Processing Functions
def processBrainData(data):
    with open('outputData.csv', 'w', newline='') as csvfile:
        brainwriter = csv.writer(csvfile)
        brainwriter.writerows(data)
    print("Processed Output Data")

def readFileData(file):
    with open(file, 'r', newline='') as csvfile:
        brainreader = csv.reader(csvfile)
        for i in brainreader:
            results.append(i)
        return brainreader.readrows()

#Test Functions

def brainGenDiagnostics():
    #Generate brain
    smolBrain = Brain(0)
    assert(smolBrain.id == 0)
    assert(smolBrain.size() == 0)
    #Generate neuron
    smolBrain.addNeuron()
    assert(len(smolBrain.neurons) == 1)
    n0 = smolBrain.neurons[0]
    assert(n0.id == 0)
    assert(n0.inputs == [])
    assert(n0.outputs == [])
    assert(n0.threshold == 0)
    assert(smolBrain.size() == 1)
    #Generate second neuron
    smolBrain.addNeuron()
    assert(len(smolBrain.neurons) == 2)
    n1 = smolBrain.neurons[1]
    assert(n1.id == 1)
    assert(n1.inputs == [])
    assert(n1.outputs == [])
    assert(n1.threshold == 0)
    assert(smolBrain.size() == 2)
    #Generate third neuron
    smolBrain.addNeuron()
    assert(len(smolBrain.neurons) == 3)
    n2 = smolBrain.neurons[2]
    assert(n2.id == 2)
    assert(n2.inputs == [])
    assert(n2.outputs == [])
    assert(n2.threshold == 0)
    assert(smolBrain.size() == 3)
    #Attach neurons 0 –> 1 –> 2
    n1.surgery(n0, n2)
    assert(n0.inputs == [])
    assert(n0.outputs == [n1])
    assert(n1.inputs == [n0])
    assert(n1.outputs == [n2])
    assert(n2.inputs == [n1])
    assert(n2.outputs == [])
    print("Brain generates successfully")

def shockBrain():
    #Setup brain
    smolBrain = setupSmolBrain()
    n0 = smolBrain.neurons[0]
    n1 = smolBrain.neurons[1]
    n2 = smolBrain.neurons[2]
    #Shock n0
    assert(n0.threshold == 0)
    n0.applySHOCK(1)
    assert(n0.threshold == 1)
    assert(n1.threshold == 0)
    assert(n2.threshold == 0)
    #Fire n0
    n0.fire()
    assert(n0.threshold == 0)
    assert(n1.threshold == 1)
    assert(n2.threshold == 0)
    #Fire n1
    n1.fire()
    assert(n0.threshold == 0)
    assert(n1.threshold == 0)
    assert(n2.threshold == 1)
    #Shock n0 x6, inducing a fire
    n0.applySHOCK(6)
    assert(n0.threshold == 0)
    assert(n1.threshold == 1)
    assert(n2.threshold == 1)
    print("Brain stimulates correctly")

#Test Suites

def axonTestSuite():
    #Setup brain
    return

def brainTestSuite():
    #Test setups
    brainGenDiagnostics()
    setupSmolBrain()
    setupRandomBrain()
    print("All brain tests passed")

def fullTestSuite():
    print("Testing Neural Structures...")
    print()

    brainTestSuite()
    shockBrain()
    axonTestSuite()
    
    print()
    print("All tests passed")

#Visualizations

def visualizeSmolBrain():
    print()
    smolBrain = setupSmolBrain()
    smolBrain.visualizeStatic()

#Simulations

def simulateSmolBrain():
    brain = setupSmolBrain()
    brain.importInputData(generateBrainData(brain))
    record = brain.simulate(1000)
    processBrainData(record)
    print("Smol Brain Simulated")

#fullTestSuite()
#visualizeSmolBrain()
simulateSmolBrain()