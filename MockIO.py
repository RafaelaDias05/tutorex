from io import StringIO

class MockIO:
    def __init__(self, inputs):
        self.inputs = StringIO(inputs)
        self.outputs = StringIO()

    def input(self, prompt=''):
        self.outputs.write(prompt)
        return self.inputs.readline().strip()

    def print(self, *args):
        self.outputs.write(' '.join(map(str, args)) + '\n')

    def get_output(self):
        return self.outputs.getvalue()
    
    


