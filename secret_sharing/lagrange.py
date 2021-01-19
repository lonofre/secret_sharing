class Lagrange:

    def __init__(self, prime):
        self.prime = prime

    def interpolation(self, evaluation, points):
        '''Given a set of points, finds a polynomial that
        passes through all those points and evaluates x

        Parameters
        ----------
        evaluation: int
            The x-coordinate that will be evaluated
        points:
            A set of points to build the polynomial

        Returns
        -------
        int
            the result of the evaluation
        '''
        result = 0
        index = 0
        for x,y in points:

            result += y * self.basis(evaluation, points, index)
            index += 1
        return result % self.prime 

    def basis(self, evaluation, points, current_index):
        '''Calculates the Lagrange basis given an index
        
        Parameters
        ----------
        evaluation: int
            The x-coordinate to evaluate 
        points:
            Set of points to calculate the basis
        current_index: int
            The index to find the current term to calculate
            the basis

        Returns
        -------
        int
            the result of the basis at the given index
        '''
        top = 1
        bottom = 1
        constant,_ = points[current_index]
        # Starts at -1 to initiate the loop at 0'
        i = -1 
        for x,_ in points:
            if not isinstance(x, int):
                raise AritmeticError('Not an integer')
            i += 1
            if i == current_index:
                continue
            top *= evaluation - x
            bottom *= constant - x
        if bottom == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return top * pow(bottom, -1, self.prime) 

