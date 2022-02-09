#Neuron, V.0.0.3
#Featuring:
#   -Neural IDs
#   -List of inputs (Axons?)
#   -List of outputs (Axons?)
#   -Threshold value
#
#   -Ability to select which neurons are connected
#   -Ability to 'shock' to increase threshold value
#   -Ability to 'fire' and apply 'shock' of 1 to all children
#   -Ability to record a list of times at which it will be shocked
#
#   -External access to outputs
#   -External access to shock times

class Neuron:
    def __init__(self, brain, number):
        # Note: Implementation does not use 'brain' currently

        # This allows for neurons to be differentiated and found easily
        self.id = number
        # A list of the neurons that fire into this neuron
        self.inputs = []
        # A list of neurons that this neuron fires into
        self.outputs = []
        # The current voltage of the neuron
        self.threshold = 0
        # A list of times at which this neuron will be shocked and the value of the shock
        self.shockTimes = []
        # A market for visualizations
        self.drawn = False

    def surgery(self, nin, nout):
        # Append all elements of nin to elements that fire into this neuron
        if (nin != None):
            if type(nin) == list:
                for i in nin:
                    self.inputs.append(i)
                    i.outputs.append(self)
            self.inputs.append(nin)
            nin.outputs.append(self)
        # Append all elements of nout to elements that this neuron fires into
        if (nout != None):
            if type(nout) == list:
                for i in nout:
                    self.inputs.append(i)
                    i.outputs.append(self)
            self.outputs.append(nout)
            nout.inputs.append(self)

    def timeShock(self, shock, time):
        # Add a new time at which this neuron will be shocked
        self.shockTimes.append((time, shock))

    def applySHOCK(self, shock):
        # Shock this neuron; if it crosses the threshold, fire
        self.threshold += shock
        if self.threshold > 3:
            self.fire()
            return True
        return False

    def fire(self):
        self.threshold = 0
        for i in self.outputs:
            i.applySHOCK(1)

    def visualizeStatic(self):
        # If this neuron hasn't been drawn
        if self.drawn == False:
            # Draw its inputs
            for i in self.inputs:
                i.visualizeStatic()
            # Draw it
            print("< " + str(self.id) + " >")
            # Draw its outputs
            for i in self.outputs:
                i.visualizeStatic()
            self.drawn == True

    def getOutputs(self):
        # The list of objects this neuron can impact
        return self.outputs

    def getShockTimes(self):
        # The list of shocks and times they will occur at
        return self.shockTimes