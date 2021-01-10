class Lagrange:

    def __init__(self, prime):
        self.prime = prime

    def interpolation(self, evaluation, points):
        ''' Given a set of points, finds a polynomial that
        passes through all those points and evaluates x'''
        result = 0
        index = 0
        for x,y in points:
            result += y * self.basis(evaluation, points, index)
            index += 1
        return result % self.prime 

    def basis(self, evaluation, points, current_index):
        ''' Calculates the Lagrange basis'''
        top = 1
        bottom = 1
        constant,_ = points[current_index]
        # Starts at -1 to initiate the loop at 0'
        i = -1 
        for x,y in points:
            i += 1
            if i == current_index:
                continue
            top *= evaluation - x
            bottom *= constant - x
        return top * pow(bottom, -1, self.prime) 
