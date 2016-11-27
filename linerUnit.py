import preceptron
def f(x):
    return x
class linerUnit(preceptron.Perceptron):
    def __init__(self,input_num):
        preceptron.Perceptron.__init__(self,f,input_num)

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
    print '6 years , salary = %.2f' % lut.predict([6.3])

