#Axon, V.0.0.2
#Featuring:
#   -Length (time in ms)
#   -Neuron (or axon) it attaches to
#
#   -Ability to 'shock' affeced neurons after (length) ms

class Axon:
    def __init__(self, length = 100, outputs = []):
        # length is measured in milliseconds of time it takes for signal to traverse
        self.length = length
        # all of the objects this axon can apply a shock to
        self.outputs = outputs

    def applySHOCK(self, shock = 1):
        # Shock everything this axon is attached to
        for i in self.outputs:
            # The output objects will handle the shock events on their own
            i.timeShock(self, shock, self.length)

    def addOutput(self, output):
        # add a new object this axon can apply a shock to
        self.outputs.append(output)