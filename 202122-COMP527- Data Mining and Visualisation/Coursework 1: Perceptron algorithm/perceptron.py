import pandas as pd
import numpy as np

# training data
header_list = ['f1', 'f2', 'f3', 'f4', 'class']  # define column name
train = pd.read_csv('C:\\Users\\Saeth\\Downloads\\CA1data\\train.data', names=header_list)  # read training data
train = train.sample(frac=1).reset_index(drop=True)  # shuffle dataset
train['class'] = train['class'].map({'class-1': 1, 'class-2': 2, 'class-3': 3})  # rename class to 1, 2, and 3
print('train data examples: ' + '\n')
print(train.head())  # show some records
print('\n')
print('train data information: ' + '\n')
print(train.describe())  # show data information
print('\n')

# test data
test = pd.read_csv('C:\\Users\\Saeth\\Downloads\\CA1data\\test.data', names=header_list)  # read test data
test['class'] = test['class'].map({'class-1': 1, 'class-2': 2, 'class-3': 3})  # rename class to 1, 2, and 3
print('test data examples: ' + '\n')
print(test.head())  # show some records
print('\n')
print('test data information: ' + '\n')
print(test.describe())  # show data information

# all function

# Question 2
def PerceptronTrain(dataFrame, max_iter, L2, lamda):
    """
        Calculate bias and weights of 2 classes (positive and negative)
        input:
            dataFrame of positive(1) and negative(-1) classes
            max_iter: numbers of iterations (int)
            L2: boolean (True: perform L2 Regularisation, False: without L2 Regularisation)
            lamda: parameter for L2 Regularisation
        output:
            weights: vector of weights
            bias
    """
    # initial values of weights and bias
    weights = np.array([0, 0, 0, 0])
    bias = 0
    eta = 1  # mu value
    for iteration in range(max_iter):
        # calculate a value of a
        for row in range(dataFrame.shape[0]):
            x = np.array(dataFrame.iloc[row][['f1', 'f2', 'f3', 'f4']])  # input features
            y = dataFrame.iloc[row]['class']  # class value (1 or -1)
            a = np.dot(weights, x) + bias  # activation score
            # misclassification: update weights and bias
            if y*a <= 0:
                bias = bias + y
                if L2 == False:  # without L2 method
                    weights = weights + eta*y*x
                else:  # L2 method
                    weights = (1 - 2*lamda)*weights + y*x
    return [weights, bias]

def PerceptronTest(weights, bias, x):
    """"
        Calculate output prediction (1 or -1)
        input:
            weights: vector weight of the model
            bias: bias of the model
            x: input features
        output:
            1 or -1
    """
    a = np.dot(weights, x) + bias
    if a > 0:
        return 1
    else:
        return -1

def accuracy(select_data, weightBias, oneVersusTheRest):
    """"
        Print accuracy of the model
        input:
            selected data: selected dataFrame (train, test)
            weightBias: weight and bias of model(s)
            oneVersusTheRest: boolean (True: multiclass method, False: not multiclass method)
        output:
            accuracy of model(s)
    """
    y_train = np.array(select_data['class'])  # class value (1, -1 or 1,2,3)
    y_pred = []  # to record predicted values
    if oneVersusTheRest == False:  # not multiclass method
        # define weight and bias
        weights = weightBias[0]
        bias = weightBias[1]
        for row in range(len(y_train)):
            x = select_data.iloc[row][['f1', 'f2', 'f3', 'f4']]  # input features
            y_pred.append(PerceptronTest(weights, bias, x))  # class prediction
    else:  # multiclass method
        for row in range(len(y_train)):
            x = select_data.iloc[row][['f1', 'f2', 'f3', 'f4']]  # input features
            temp_a = [np.dot(weightAndBias[0], x) + weightAndBias[1] for weightAndBias in weightBias]  # a values
            y_pred.append(temp_a.index(max(temp_a)) + 1)  # predicted class (1,2,3)
    y_pred = np.array(y_pred)
    # calculate the accuracy
    score = 0
    for member in range(len(y_train)):
        if y_train[member] == y_pred[member]:  # the same value
            score += 1
    print('target data')
    print(y_train)
    print('\n')
    print('predicted data')
    print(y_pred)
    return score / len(y_train)

def oneVersusTheRest(train, iteration, L2, lamda):
    """"
        Calculate weights and bias of multiclass method
        input:
            train: train data
            iteration: numbers of iterations (int)
            L2 = boolean (True: perform L2 Regularisation, False: without L2 Regularisation)
            lamda: parameter for L2 Regularisation
        output:
            list of weights and bias of all models
    """
    # model1: 1 vs the rest
    select_data = train.copy()
    select_data['class'] = select_data['class'].map({1: 1, 2: -1, 3: -1})  # rename class to 1 or -1
    weightBias1 = PerceptronTrain(select_data, iteration, L2, lamda)  # find weight and bias

    # model2: 2 vs the rest
    select_data = train.copy()
    select_data['class'] = select_data['class'].map({1: -1, 2: 1, 3: -1})  # rename class to 1 or -1
    weightBias2 = PerceptronTrain(select_data, iteration, L2, lamda)  # find weight and bias

    # model3: 3 vs the rest
    select_data = train.copy()
    select_data['class'] = select_data['class'].map({1: -1, 2: -1, 3: 1})  # rename class to 1 or -1
    weightBias3 = PerceptronTrain(select_data, iteration, L2, lamda)  # find weight and bias

    return [weightBias1, weightBias2, weightBias3]

def train_a_vs_b(train, test, class1, class2, MaxIter, L2, lamda, oneVersusTheRest):
    """"
        Select data with both class1 and class2, and calculate accuracy of class1 vs class2 model
        input:
            train: train data
            test: test data
            class1: the positive class (1)
            class2: the negative class (-1)
            MaxIter: numbers of iterations in training process (int)
            L2 = boolean (True: perform L2 Regularisation, False: without L2 Regularisation)
            lamda: parameter for L2 Regularisation
            oneVersusTheRest: boolean (True: multiclass method, False: not multiclass method)
        output:
            accuracy of the class1 vs class2 model
    """
    select_data = train[train['class'].isin([class1, class2])].reset_index(drop=True)  # select class 1 and 2
    select_data['class'] = select_data['class'].map({class1: 1, class2: -1})  # rename class to 1 and -1
    weightBias = PerceptronTrain(select_data, MaxIter, L2, lamda)  # find weight and bias

    # train accuracy
    print('train accuracy: ', accuracy(select_data, weightBias, oneVersusTheRest))

    # test acc
    select_test = test[test['class'].isin([class1, class2])].reset_index(drop=True)  # select class 1 and 2
    select_test['class'] = select_test['class'].map({class1: 1, class2: -1})  # rename class to 1 and -1
    print('test accuracy: ', accuracy(select_test, weightBias, oneVersusTheRest))

# Question 3
print('\n')
print('Question 3: ' + '\n')

# train perceptron class 1 vs 2
print('1 vs 2')
train_a_vs_b(train, test, 1, 2, 20, False, 0, False)
print('\n')

# train perceptron class 2 vs 3
print('2 vs 3')
train_a_vs_b(train, test, 2, 3, 20, False, 0, False)
print('\n')

# train perceptron class 1 vs 3
print('1 vs 3')
train_a_vs_b(train, test, 1, 3, 20, False, 0, False)

# Question4: 1 vs the rest approach
print('\n')
print('Q4: 1 vs the rest method')
weightBias = oneVersusTheRest(train, 20, False, 0)  # weights and bias of 3 models

# train accuracy
print('train accuracy: ', accuracy(train, weightBias, True))

# test accuracy
print('test accuracy: ', accuracy(test, weightBias, True))

# Question 5: L2 regularization
print('\n')
print('Question 5: L2 regularization' + '\n')
allLamda = [0.01, 0.1, 1, 10, 100]  # all lambda
for lamda in allLamda:
    print('lambda = ', lamda)
    weightBias = oneVersusTheRest(train, 20, True, lamda)  # weight and bias of the model

    # train and test accuracy
    print('train accuracy: ', accuracy(train, weightBias, True))
    print('test accuracy: ', accuracy(test, weightBias, True))
    print('\n')
