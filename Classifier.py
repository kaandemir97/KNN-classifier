class classif:
    def __init__(self, prediction, true):
        self.prediction = prediction
        self.true = true
        self.correct = prediction==true
        return
        #Store final classified label and true/false label
