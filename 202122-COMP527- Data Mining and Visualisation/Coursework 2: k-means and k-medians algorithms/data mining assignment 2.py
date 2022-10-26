# import libraries
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt

# prepare dataset
header_list = ['word']  # define column name
for i in range(1, 301):
    header_list.append('f'+str(i))  # add feature columns

# read each file and add column label
animal = pd.read_csv('C:\\Users\\Saeth\\Downloads\\CA2data\\animals', sep=' ', names=header_list)
animal['label'] = 'animals'
countries = pd.read_csv('C:\\Users\\Saeth\\Downloads\\CA2data\\countries', sep=' ', names=header_list)
countries['label'] = 'countries'
fruits = pd.read_csv('C:\\Users\\Saeth\\Downloads\\CA2data\\fruits', sep=' ', names=header_list)
fruits['label'] = 'fruits'
veggies = pd.read_csv('C:\\Users\\Saeth\\Downloads\\CA2data\\veggies', sep=' ', names=header_list)
veggies['label'] = 'veggies'
data = pd.concat([animal, countries, fruits, veggies]).reset_index()  # merge all data
# display example and shape of dataset
print('example of dataset')
print(data.head())
print('shape of dataset: ', data.shape)
print('')

# define features of the dataset
features = data.drop(['word', 'label', 'index'], axis=1)

# all functions

# Question 1 and Question 2
def score(all_k, maxiter, X, l2, data, method):
    """
        Calculate the B-cubed scores of k-means and k-medians.
        Input:
            all_k: list of all desired k values
            maxiter: numbers of iterations (int)
            X: array of features in the dataset
            l2: boolean [True: apply l2 normalization, False: no l2 normalization]
            data: DataFrame of the whole dataset
            method: string ['mean': k-means, 'median': k-medians]
        Output:
            all_precision: list of all precisions
            all_recall: list of all recalls
            all_f_score: list of all f-scores
            title: string of the title of the graph to be plotted in the plot function
    """
    all_precision = []  # collect all precisions
    all_recall = []  # collect all recalls
    all_f_score = []  # collect all f-scores
    for k in all_k:
        if l2 == True:  # if l2 normalization
            X = np.array([X[i] / np.linalg.norm(X, axis=1)[i] for i in range(X.shape[0])])  # array of features
            # define title name in the graph
            if method == 'mean':
                title = 'K-means with L2 normalization'
            else:
                title = 'K-medians with L2 normalization'
        else:  # if not l2 normalization
            # define title name in the graph
            if method == 'mean':
                title = 'K-means without L2 normalization'
            else:
                title = 'K-medians without L2 normalization'

        # define initial centroids
        centroids = X[np.random.randint(X.shape[0], size=k)]

        # define initial classes, and distances
        classes = np.zeros(X.shape[0], dtype=np.float64)  # record class of each object
        distances = np.zeros([X.shape[0], k], dtype=np.float64)  # record distances between each object and selected centroid

        for i in range(maxiter):
            # assign step
            for i, c in enumerate(centroids):
                # calculate distances
                if method == 'mean':  # k-means method
                    # euclidean distance
                    distances[:, i] = np.linalg.norm(X - c, axis=1)
                else:  # k-medians method
                    # l1 distance
                    distances[:, i] = np.linalg.norm(X - c, ord=1, axis=1)

            # define classes of each object
            classes = np.argmin(distances, axis=1)

            # optimize step
            for c in range(k):
                if method == 'mean':  # k-means method
                    # update centroids using mean
                    centroids[c] = np.mean(X[classes == c], 0)
                else:  # k-medians method
                    # update centroids using median
                    centroids[c] = np.median(X[classes == c], 0)
        # B-cubed calculation
        precision = 0  # initial precision
        recall = 0  # initial recall
        f_score = 0  # initial f_score
        for label in list(data['label'].unique()):  # for each label
            group = list(classes[data[data['label'] == label].index])  # target cluster with desired label
            for member in group:  # for each object in selected cluster
                temp_precision = group.count(member) / len(group)  # precision of the current object
                temp_recall = group.count(member) / len(classes[classes == member])  # recall of the current object
                precision += temp_precision  # update precision
                recall += temp_recall  # update recall
                f_score += 2 * (temp_precision * temp_recall) / (temp_precision + temp_recall)  # update f_score
        # the final scores
        precision = precision / data.shape[0]
        recall = recall / data.shape[0]
        f_score = f_score / data.shape[0]
        # append the final scores to the output list
        all_precision.append(precision)
        all_recall.append(recall)
        all_f_score.append(f_score)

    # display scores
    print('precisions for k = 1 to 9: ')
    for i in range(len(all_precision)):
        print('k = '+str(i+1)+'/ precision: '+str(all_precision[i]))
    print('recalls for k = 1 to 9: ')
    for i in range(len(all_recall)):
        print('k = ' + str(i + 1) + '/ recall: ' + str(all_recall[i]))
    print('f-scores for k = 1 to 9: ')
    for i in range(len(all_f_score)):
        print('k = ' + str(i + 1) + '/ f-score: ' + str(all_f_score[i]))
    print('average precision: ', sum(all_precision) / len(all_precision))
    print('average recall: ', sum(all_recall) / len(all_recall))
    print('average f-score: ', sum(all_f_score) / len(all_f_score))
    return all_precision, all_recall, all_f_score, title

def plot(all_k, all_precision, all_recall, all_f_score, title, last_plot):
    """
        Plot scores and k of k-means and k-medians.
        Input:
            all_k: list of all desired k value
            all_precision: list of all precisions
            all_recall: list of all recalls
            all_f_score: list of all f-scores
            title: string of the title of the graph
            last_plot: boolean [True: last plot, False: not the last plot]
        Output:
            none
    """
    x = np.arange(len(all_k))  # label locations
    width = 0.25  # width of the bars graph
    fig, ax = plt.subplots()  # initial figure
    # define locations and labels of the graph
    rects1 = ax.bar(x - width, all_precision, width, label='precision')
    rects2 = ax.bar(x, all_recall, width, label='recall')
    rects3 = ax.bar(x + width, all_f_score, width, label='f_score')

    # graph configurations
    ax.set_ylabel('score')
    ax.set_xlabel('k')
    ax.set_title(title)
    ax.set_xticks(x, all_k)
    ax.legend()
    fig.tight_layout()
    if last_plot == True:  # if it is the last plot
        plt.show()

# main program

all_k = [1,2,3,4,5,6,7,8,9]  # k = 1 to 9

# Question 3: K-means without L2 normalization
print('K-means without L2 normalization')
k_mean_noL2 = score(all_k, 50, np.array(features), False, data, 'mean')
plot(all_k, k_mean_noL2[0], k_mean_noL2[1], k_mean_noL2[2], k_mean_noL2[3], False)

# Question 4: K-means with L2 normalization
print('K-means with L2 normalization')
k_mean_L2 = score(all_k, 50, np.array(features), True, data, 'mean')
plot(all_k, k_mean_L2[0], k_mean_L2[1], k_mean_L2[2], k_mean_L2[3], False)

# Question 5: K-medians without L2 normalization
print('K-medians without L2 normalization')
k_median_noL2 = score(all_k, 50, np.array(features), False, data, 'median')
plot(all_k, k_median_noL2[0], k_median_noL2[1], k_median_noL2[2], k_median_noL2[3], False)

# Question 6: K-medians with L2 normalization
print('K-medians with L2 normalization')
k_median_L2 = score(all_k, 50, np.array(features), True, data, 'median')
plot(all_k, k_median_L2[0], k_median_L2[1], k_median_L2[2], k_median_L2[3], True)
