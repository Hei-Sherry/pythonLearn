import preceptron
def f(x):
    return 1 if x > 0 else 0

def get_training_dataset():
    input_vectors = [[1,1],[1,0],[0,1],[0,0]]
    labels = [1,0,0,0]
    return input_vectors , labels
def train_and_perceptron():
    p = preceptron.Perceptron(f,2)
    input_vectors, labels = get_training_dataset()
    p.trains(5,0.1, input_vectors,labels)
    return p
if __name__ == '__main__':
    #print get_training_dataset()
    and_perceptron = train_and_perceptron()

    print and_perceptron
    print '1 and 1 = %d' % and_perceptron.predict([1,1])
