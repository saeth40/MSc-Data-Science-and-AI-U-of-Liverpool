# Saeth Wannasuphoprasit
# 201585689

# the above comment is my full name and my student ID


# define function ***********************************

def fifo():
    # iteration for each page in request
    for page in requests:
        # case 1, page is already in cache
        if page in cache:
            print('hit')

        # case 2, page is not in cache
        else:
            print('miss')
            if len(cache) < 8:  # if cache is not full
                cache.append(page)
            else:  # if cache is already full
                cache.pop(0)  # delete the left page in the cache
                cache.append(page)  # add the new page to the right of cache
    print(cache)

def lfu():
    # list to record each page and its frequency
    record_page = []  # [[page1, frequency1], [page2, frequency2], ..., [pageN, frequencyN]]

    # iteration for each page in request
    for page in requests:
        # section 1, record each page and its frequency in the record_page list

        if len(record_page) == 0:  # if recording list is empty
            record_page.append([page, 1])
        else:  # if recording list is not empty
            # example record_page = [[1,1], [2,1], [3,5], [4,2], [5,1]]
            # [p[0] for p in record_page] = [1, 2, 3, 4, 5]
            if page not in [p[0] for p in record_page]:  # if page has not been recorded yet
                record_page.append([page, 1])  # add the list of [page, frequency]
            else:  # if that page has already been recorded
                for index in range(len(record_page)):  # iteration to find that page in the record list
                    if record_page[index][0] == page:
                        record_page[index][1] += 1  # add the frequency of that page by 1
                        break

        # section 2, hit or miss

        if page in cache:  # case 1, page is already in cache
            print('hit')
        else:  # case 2, page is not in cache
            print('miss')
            if len(cache) < 8:  # if cache is not full, add that page in the cache
                cache.append(page)
            else:  # if page is full, find the page to be eliminated (out)
                # example record_page = [[1,1], [2,1], [3,5], [4,2], [5,1]]
                # example cache = [1,2,3,4]
                # [f[1] for f in record_page] = [1, 1, 5, 2, 1]
                # [f[1] for f in record_page if f[0] in cache] = [1, 1, 5, 2]
                # the minimum of the above list is 1

                # minimum frequency of the current pages in the cache
                minimum_frequency = min([f[1] for f in record_page if f[0] in cache])

                # possible pages in the cache to be eliminated that has the minimum frequency
                # [g for g in record_page if g[1] == 1] = [[1,1], [2,1], [5,1]]
                # [g for g in record_page if g[1] == 1 and g[0] in cache] = [[1,1], [2,1]]
                possible_out = [g for g in record_page if g[1] == minimum_frequency and g[0] in cache]

                out = min(possible_out)  # the page to be eliminated, in this case = [1,1]

                # eliminate the target page
                for index in range(len(cache)):
                    if cache[index] == out[0]:
                        cache.pop(index)
                        break
                # add the current page
                cache.append(page)
    print(cache)

# main program ***********************************

while True:
    # set up a new cach and requests
    cache = []
    requests = []

    # set up requests: add each page in requests
    # assume: user type only int number
    while True:
        number = int(input('Please enter the next page to be added to the list of requests: ').strip())
        # to finalize the requests list
        if number == 0:
            break
        requests.append(number)

    # set up options
    # assume: user type only 1, 2, or Q
    print('Select one of the options below for the cache management:')
    print(' 1 for FIFO')
    print(' 2 for LFU')
    print(' Q for existing the program')
    option = input('').strip()

    # process the option that the user selected
    if option == 'Q':
        break
    elif option == '1':
        fifo()
    else:
        lfu()