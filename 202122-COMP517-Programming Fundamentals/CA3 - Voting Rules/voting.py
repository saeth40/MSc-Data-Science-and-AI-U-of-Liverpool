# import
import openpyxl

# function answer to minimize the duplication of the code
def answer(tieBreak, sort, preferences):

    """
        Find the winner from possible candidates.
        input:
            tieBreak ('max', 'min', integer of agent)
            sort (list of (maximum frequency of alternative, each alternative))
            preferences (dictionary of an preference profile)
        output:
            alternative (integer)
    """

    if len(sort) == 1:  # case 1: 1 candidate, no tieBreak
        return sort[0][1]
    else:  # case 2: more than 1 candidate, tieBreak
        if tieBreak == 'max':  # max method
            return sort[0][1]  # extract the first alternative in sort
        elif tieBreak == 'min':  # min method
            return sort[-1][1]  # extract the last alternative in sort
        else:
            # agent i method

            # handling errors
            try:
                test = preferences[tieBreak]  # check whether the tieBreak is eligible as a key in the dictionary
            except Exception:  # if error
                pass
            else:
                # if no errors
                for candidate in preferences[tieBreak]:  # for each alternative in the selected agent
                    if candidate in [g[1] for g in sort]:  # if that alternative in the sort list
                        return candidate

# generatePreferences
def generatePreferences(values):

    """
        generate preference profile
        input:
            an openpyxl worksheet
        output:
            a dictionary of preference profile
    """

    out = dict()  # dictionary of preference profile
    out_key = 1  # initial key of the dictionary

    for row in values.rows:  # for each row in the openpyxl worksheet
        temp = []  # store each valuation in the openpyxl file and its index
        for index_alternative in range(values.max_column):  # for index of each alternative
            temp.append([row[index_alternative].value, index_alternative + 1])  # store [valuation, index] in temp
        temp = sorted(temp, reverse=True)  # sorting based on the valuation and its index
        out[out_key] = [i[1] for i in temp]  # store the above sorting alternative to the dictionary in the current key
        out_key += 1  # change the key of the dictionary by 1
    return out

# dictatorship
def dictatorship(preferenceProfile, agent):

    """
        Dictatorship voting method
        input:
            preference profile (dictionary)
            agent (integer)
        output:
            the alternative (integer)
    """

    # handling errors
    try:
        test = preferenceProfile[agent][0]  # check a key in the dictionary as well as the index
    except Exception:  # if error
        pass
    else:
        # if no errors
        return preferenceProfile[agent][0]  # the first alternative in the preferred agent

# scoringRule
def scoringRule(preferences, scoreVector, tieBreak):

    """
        assign scoreVector to an preference profile. find the alternative(max score) with tie breaking rules.
        input:
            an preference profile (dictionary)
            scoreVector (list of float numbers)
            tieBreak ('max', 'min', integer of agent)
        output:
            winning alternative (integer)
    """

    # handling errors
    try:
        if len(preferences[list(preferences.keys())[0]]) != len(scoreVector):  # A test the length of scoreVector
            raise Warning
        test_sorting = sorted(scoreVector, reverse=True)  # B test whether scoreVector is sortable
        test_sum = sum(scoreVector)  # C test whether scoreVector can be summed
    except Warning:  # error A
        print('Incorrect input')
        return False
    except Exception:  # error B, C
        pass
    else:
        # if no errors, assign scoreVector to an preference profile.
        record = dict()  # dictionary to record score of each alternative
        scoreVector = sorted(scoreVector, reverse=True)  # sort scoreVector (max to min)
        for key in preferences.keys():  # for each key in the preference profile
            for index in range(len(scoreVector)):  # for index of each alternative
                if preferences[key][index] not in record.keys():  # if alternative is not in keys of record
                    record[preferences[key][index]] = scoreVector[index]  # set the initial score of that alternative
                else:  # if alternative in keys of record
                    record[preferences[key][index]] += scoreVector[index]  # accumulate the score of that alternative
        # sort the record based on the score followed by the integer of alternative (max to min)
        sort = sorted([(value, key) for (key, value) in record.items() if value == max(record.values())], reverse=True)

        # answer
        return answer(tieBreak, sort, preferences)

# plurality
def plurality(preferences, tieBreak):

    """
        The winner is the alternative that appears the most times in the first position of the agents' preference orderings.
        input:
            an preference profile (dictionary)
            tieBreak ('max', 'min', integer of agent)
        output:
            winning alternative (integer)
    """

    record = dict()  # dictionary to record frequency of each first alternative
    for key in preferences.keys():  # for each key in an preference profile
        if preferences[key][0] not in record.keys():  # if the key is not in keys of record
            record[preferences[key][0]] = 1  # set the initial frequency of that first alternative to 1
        else:  # the key is in keys of record
            record[preferences[key][0]] += 1  # increase the frequency of that alternative by 1
    # sort the record based on the score followed by the integer of alternative (max to min)
    sort = sorted([(value, key) for (key, value) in record.items() if value == max(record.values())], reverse=True)

    # answer
    return answer(tieBreak, sort, preferences)

# veto
def veto(preferences, tieBreak):

    """
        Assign 0 to the last order alternatives and 1 to the rest. Find the maximum score alternative with tie breaking rules.
        input:
            an preference profile (dictionary)
            tieBreak ('max', 'min', integer of agent)
        output:
            winning alternative (integer)
    """

    record = dict()  # dictionary to record score of each alternative
    for key in preferences.keys():  # for each key in an preference profile
        for index in range(len(preferences[key])):  # for index of each alternative
            if index != len(preferences[key]) - 1:  # if alternative is not the last one
                if preferences[key][index] not in record.keys():  # if that alternative is not the key of record
                    record[preferences[key][index]] = 1  # set the initial score of that alternative to 1
                else:  # if that alternative is in keys of record
                    record[preferences[key][index]] += 1  # increase the score of that alternative by 1
    # sort the record based on the score followed by the integer of alternative (max to min)
    sort = sorted([(value, key) for (key, value) in record.items() if value == max(record.values())], reverse=True)

    # answer
    return answer(tieBreak, sort, preferences)

# borda
def borda(preferences, tieBreak):

    """
        Assign m - j to each alternative. Find the maximum score alternative with tie breaking rules.
        input:
            an preference profile (dictionary)
            tieBreak ('max', 'min', integer of agent)
        output:
            winning alternative (integer)
    """

    record = dict()  # dictionary to record score of each alternative
    for key in preferences.keys():  # for each key in an preference profile
        num = len(preferences[key]) - 1  # initial score for the first alternative is the number of all alternatives - 1
        for candidate in preferences[key]:  # for each alternative
            if candidate not in record.keys():  # if that alternative not in keys of record
                record[candidate] = num  # set the initial score of that alternative to num
            else:  # if that alternative in keys of record
                record[candidate] += num  # increase the score of that alternative by num
            num -= 1  # reduce the num by 1 for the next alternative
    # sort the record based on the score followed by the integer of alternative (max to min)
    sort = sorted([(value, key) for (key, value) in record.items() if value == max(record.values())], reverse=True)

    # answer
    return answer(tieBreak, sort, preferences)

# harmonic
def harmonic(preferences, tieBreak):

    """
        Assign 1/j to each alternative. Find the maximum score alternative with tie breaking rules.
        input:
            an preference profile (dictionary)
            tieBreak ('max', 'min', integer of agent)
        output:
            winning alternative (integer)
    """

    record = dict()  # dictionary to record score of each alternative
    for key in preferences.keys():  # for each key in an preference profile
        num = 1  # initial score for the first alternative
        for candidate in preferences[key]:  # for each alternative
            if candidate not in record.keys():  # if that alternative not in keys of record
                record[candidate] = 1 / num  # set the initial score of that alternative to 1/num
            else:  # if that alternative in keys of record
                record[candidate] += 1 / num  # increase the score of that alternative by 1/num
            num += 1  # increase the num by 1 for the next alternative
    # sort the record based on the score followed by the integer of alternative (max to min)
    sort = sorted([(value, key) for (key, value) in record.items() if value == max(record.values())], reverse=True)

    # answer
    return answer(tieBreak, sort, preferences)

# STV
def STV(preferences, tieBreak):

    """
        The process is remove the least frequently alternatives in the first position in each round. Find the remaining alternative.
        input:
            an preference profile (dictionary)
            tieBreak ('max', 'min', integer of agent)
        output:
            winning alternative (integer)
    """

    repetition = len(preferences[list(preferences.keys())[0]])  # repetition is the number of all alternatives
    for iteration in range(repetition):  # for each round (the total of number of repetition)
        candidates = preferences[list(preferences.keys())[0]]  # all alternatives in each round
        temp = [value[0] for (key, value) in preferences.items()]  # all alternatives in the first position
        count_rec = dict()  # dictionary to record frequency of each alternative
        for i in candidates:  # for each alternative in candidates
            if i not in temp:  # if that alternative not in the first order
                count_rec[i] = 0  # set the frequency of that alternative to 0
            else:  # if that alternative is in the first order
                count_rec[i] = temp.count(i)  # set the frequency of that alternative to the counting of it
        # sort the record based on the score followed by the integer of alternative (max to min)
        sort = sorted([(v, k) for (k, v) in count_rec.items() if v == min(count_rec.values())], reverse=True)
        eliminate = [i[1] for i in sort]  # list of eliminating candidates
        remain = set(candidates) - set(eliminate)  # remaining alternatives
        if len(remain) == 0:  # if there is no remaining alternative
            return answer(tieBreak, sort, preferences)
        else:  # if there is some remaining alternatives
            # delete each alternative in an preference profile from eliminate list
            for key in preferences.keys():  # for each key in an preference profile
                for target in eliminate:  # for each alternative in eliminate list
                    preferences[key].pop(preferences[key].index(target))  # delete that alternative in an preference profile

# rangeVoting
def rangeVoting(values, tieBreak):

    """
        Find the alternative that has the maximum sum of valuations.
        input:
            an openpyxl worksheet
            tieBreak ('max', 'min', integer of agent)
        output:
            winning alternative (integer)
    """

    record = dict()  # dictionary to record score of each alternative
    for row in values.rows:  # for each row in an openpyxl worksheet
        for index in range(values.max_column):  # for each index in range number of alternatives
            if index + 1 not in record.keys():  # if that alternative not in keys of record
                record[index + 1] = row[index].value  # set the initial score of that alternative to the valuation with the same index
            else:  # if that alternative in keys of record
                record[index + 1] += row[index].value  # increase the score of that alternative by the valuation with the same index
    # sort the record based on the score followed by the integer of alternative (max to min)
    sort = sorted([(value, key) for (key, value) in record.items() if value == max(record.values())], reverse=True)

    # answer
    return answer(tieBreak, sort, generatePreferences(values))
