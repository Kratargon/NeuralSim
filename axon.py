#Axon, V.0.0.3
#Featuring:
#   -Length (time in ms)
#   -Neuron (or axon) it attaches to
#
#   -Ability to 'shock' affeced neurons after (length) ms
#   -Static visualization function

class Axon:
    def __init__(self, length = 100, outputs = []):
        # length is measured in milliseconds of time it takes for signal to traverse
        self.length = length
        # all of the objects this axon can apply a shock to
        self.outputs = outputs
        self.drawn = False

    def applySHOCK(self, shock = 1):
        # Shock everything this axon is attached to
        for i in self.outputs:
            # The output objects will handle the shock events on their own
            i.timeShock(shock, self.length)

    def addOutput(self, output):
        # add a new object this axon can apply a shock to
        self.outputs.append(output)

    def visualizeStatic(self):
        # TODO fix this
        # If this axon hasn't been drawn
        if self.drawn == False:
            # Draw it
            print("< " + "Axon" + " >")
            # Draw its outputs
            for i in self.outputs:
                i.visualizeStatic()
            self.drawn == True

    def getOutputs(self):
        # Retreive the list of outputs
        out = []
        for i in self.outputs:
            if type(i) == Axon:
                out = out + i.getOutputs()
            else:
                out.append(i)
        return out