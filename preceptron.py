class Perceptron(object):
    """docstring for Perceptron"""
    def __init__(self, activator,input_num):
        self.activator = activator
        self.bias = 0.0
        self.weights = [ 0.0 for _ in range(input_num)]
    def __str__(self):
        return "weight  : %s\n bias : %f\n" % (self.weights,self.bias)

    def  predict(self,input_vector):
        return self.activator(
            reduce(lambda x,y : x+y ,
            map(lambda (x,y) : x*y,zip(input_vector,self.weights)),0.0)
            +self.bias)

    def trains(self,iteration,rate,input_vectors,labels):
        for _ in range(iteration):
            self.one_train(input_vectors,labels,rate)

    def one_train(self,input_vectors,labels,rate):
        simples = zip(input_vectors,labels)
        for(input_vec,label) in simples:
            output = self.predict(input_vec)
            self.update_weights(input_vec,output,label,rate)

    def update_weights(self,input_vec,output,label,rate):
        delta = label - output
        self.weights = map(lambda (x,w) : w+rate*delta*x,zip(input_vec,self.weights))
        self.bias +=rate * delta

def f(x):
    return x
class linerUnit(Perceptron):
    def __init__(self,input_num):
        Perceptron.__init__(self,f,input_num)

def get_train_data():
    input_vectors = [[5],[3],[8],[1.4],[10.1]]
    labels = [5000,2300,7600,1800,11400]
    return input_vectors, labels

def train_liner_uint():
    lut = linerUnit(1)
    input_vectors, labels = get_train_data()
    lut.trains(10, 0.01, input_vectors, labels)
    return lut


if __name__ == '__main__':
    lut = train_liner_uint()
    print lut
    print '6 years , salary = %.2f' % lut.predict([8.1])


