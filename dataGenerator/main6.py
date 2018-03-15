__author__ = 'Ke Wang'
__copyright__ = 'Copyright 2018, Ke Wang'
__version__ = '0.1'
__email__ = 'kewang1@andrew.cmu.edu'

import numpy as np
from util import *

def sauces_gen(sauces, sys_time):
    current_object_count = len(sauces)
    if current_object_count == 0:  # there is currently no sauce object, the next transaction must be a produce
        sauces.append('produced')
        return produce_gen('Tomato', 'Tomato', 0, sys_time, '500', [])
    else:
        while 1:
            picked_index = int((current_object_count + 1) * np.random.rand())
            if picked_index == current_object_count:  # we should produce a new product
                sauces.append('produced')
                return produce_gen('Tomato', 'Tomato', current_object_count, sys_time, '500', [])
            else:  # we should generate a transaction related to an existing product
                state = sauces[picked_index]
                if state == 'produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        sauces[picked_index] = 'shipped'
                        return shipped_gen('Tomato', 'Tomato', picked_index, sys_time, '20', 'ups', 'Sauce',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        sauces[picked_index] = 'stored'
                        return stored_gen('Tomato', 'Tomato', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        sauces[picked_index] = 'terminated'
                        return terminated_gen('Tomato', 'Tomato', picked_index, sys_time, 'lost')
                elif state == 'shipped':
                    sauces[picked_index] = 'arrived'
                    return arrived_gen('Sauce', 'Tomato', picked_index, sys_time, 'Tom')
                elif state == 'stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        sauces[picked_index] = 'shipped'
                        return shipped_gen('Tomato', 'Tomato', picked_index, sys_time, '20', 'ups', 'Sauce',
                                           'non-prime')
                    else:  # go to 'terminated' state
                        sauces[picked_index] = 'terminated'
                        return terminated_gen('Tomato', 'Tomato', picked_index, sys_time, 'lost')
                elif state == 'arrived':
                    sauces[picked_index] = 's produced'
                    return produce_gen('Sauce', 'Sauce', picked_index, sys_time, '500', [('Tomato', picked_index)])

                elif state == 's produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        sauces[picked_index] = 's shipped'
                        return shipped_gen('Sauce', 'Sauce', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        sauces[picked_index] = 's stored'
                        return stored_gen('Sauce', 'Sauce', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        sauces[picked_index] = 'terminated'
                        return terminated_gen('Sauce', 'Sauce', picked_index, sys_time, 'sold')
                elif state == 's shipped':
                    sauces[picked_index] = 's arrived'
                    return arrived_gen('Mcdonalds', 'Sauce', picked_index, sys_time, 'Joe')
                elif state == 's stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        sauces[picked_index] = 's shipped'
                        return shipped_gen('Sauce', 'Sauce', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    else:  # go to 'terminated' state
                        sauces[picked_index] = 'terminated'
                        return terminated_gen('Sauce', 'Sauce', picked_index, sys_time, 'lost')


def buns_gen(buns, sesames, flour, sys_time):
    sesame_or_flour = np.random.rand()
    if sesame_or_flour < 0.5: # look at sesame
        current_object_count = len(sesames)
        if current_object_count == 0:  # there is currently no sauce object, the next transaction must be a produce
            sesames.append('produced')
            return produce_gen('Sesames', 'Sesames', 0, sys_time, '500', [])
        else:
            while 1:
                picked_index = int((current_object_count + 1) * np.random.rand())
                if picked_index == current_object_count:  # we should produce a new product
                    sesames.append('produced')
                    return produce_gen('Sesames', 'Sesames', current_object_count, sys_time, '500', [])
                else:  # we should generate a transaction related to an existing product
                    state = sesames[picked_index]
                    if state == 'produced':
                        next_state = 100 * np.random.rand()
                        if next_state < 30:  # go to 'shipped' state
                            sesames[picked_index] = 'shipped'
                            return shipped_gen('Sesames', 'Sesames', picked_index, sys_time, '20', 'ups', 'Bun',
                                               'prime')
                        elif next_state < 60:  # go to 'stored' state
                            sesames[picked_index] = 'stored'
                            return stored_gen('Sesames', 'Sesames', picked_index, sys_time, '15')
                        else:  # go to 'terminated' state
                            sesames[picked_index] = 'terminated'
                            return terminated_gen('Sesames', 'Sesames', picked_index, sys_time, 'lost')
                    elif state == 'shipped':
                        sesames[picked_index] = 'arrived'
                        return arrived_gen('Bun', 'Sesames', picked_index, sys_time, 'Milda')
                    elif state == 'stored':
                        next_state = 100 * np.random.rand()
                        if next_state < 80:  # go to 'shipped' state
                            sesames[picked_index] = 'shipped'
                            return shipped_gen('Sesames', 'Sesames', picked_index, sys_time, '20', 'ups', 'Bun',
                                               'prime')
                        else:  # go to 'terminated' state
                            sesames[picked_index] = 'terminated'
                            return terminated_gen('Sesames', 'Sesames', picked_index, sys_time, 'expired')
                    elif state == 'arrived':
                        for index in range(len(flour)):
                            if flour[index] == 'arrived':
                                sesames[picked_index] = 'b produced'
                                flour[index] = 'used'
                                return produce_gen('Bun', 'Bun', picked_index, sys_time, '500', [('Sesames', picked_index), ('Flour', index)])

                    elif state == 'b produced':
                        next_state = 100 * np.random.rand()
                        if next_state < 30:  # go to 'shipped' state
                            sesames[picked_index] = 'b shipped'
                            return shipped_gen('Bun', 'Bun', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                               'prime')
                        elif next_state < 60:  # go to 'stored' state
                            sesames[picked_index] = 'b stored'
                            return stored_gen('Bun', 'Bun', picked_index, sys_time, '15')
                        else:  # go to 'terminated' state
                            sesames[picked_index] = 'terminated'
                            return terminated_gen('Bun', 'Bun', picked_index, sys_time, 'expired')
                    elif state == 'b shipped':
                        sesames[picked_index] = 'b arrived'
                        return arrived_gen('Mcdonalds', 'Bun', picked_index, sys_time, 'Joe')
                    elif state == 'b stored':
                        next_state = 100 * np.random.rand()
                        if next_state < 80:  # go to 'shipped' state
                            sesames[picked_index] = 'b shipped'
                            return shipped_gen('Bun', 'Bun', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                               'prime')
                        else:  # go to 'terminated' state
                            sesames[picked_index] = 'terminated'
                            return terminated_gen('Bun', 'Bun', picked_index, sys_time, 'expired')

    else:
        current_object_count = len(flour)
        if current_object_count == 0:  # there is currently no lettuce object, the next transaction must be a produce
            flour.append('produced')
            return produce_gen('Flour', 'Flour', 0, sys_time, '500', [])
        else:
            while 1:
                picked_index = int((current_object_count + 1) * np.random.rand())
                if picked_index == current_object_count:  # we should produce a new product
                    flour.append('produced')
                    return produce_gen('Flour', 'Flour', current_object_count, sys_time, '500', [])
                else:  # we should generate a transaction related to an existing product
                    state = flour[picked_index]
                    if state == 'produced':
                        next_state = 100 * np.random.rand()
                        if next_state < 30:  # go to 'shipped' state
                            flour[picked_index] = 'shipped'
                            return shipped_gen('Flour', 'Flour', picked_index, sys_time, '20', 'ups', 'Bun',
                                               'non-prime')
                        elif next_state < 60:  # go to 'stored' state
                            flour[picked_index] = 'stored'
                            return stored_gen('Flour', 'Flour', picked_index, sys_time, '15')
                        else:  # go to 'terminated' state
                            flour[picked_index] = 'terminated'
                            return terminated_gen('Flour', 'Flour', picked_index, sys_time, 'lost')
                    elif state == 'shipped':
                        flour[picked_index] = 'arrived'
                        return arrived_gen('Bun', 'Flour', picked_index, sys_time, 'Milda')
                    elif state == 'stored':
                        next_state = 100 * np.random.rand()
                        if next_state < 80:  # go to 'shipped' state
                            flour[picked_index] = 'shipped'
                            return shipped_gen('Flour', 'Flour', picked_index, sys_time, '20', 'ups', 'Bun',
                                               'non-prime')
                        else:  # go to 'terminated' state
                            flour[picked_index] = 'terminated'
                            return terminated_gen('Flour', 'Flour', picked_index, sys_time, 'expired')


def lettuce_gen(lettuce, sys_time):
    current_object_count = len(lettuce)
    if current_object_count == 0:  # there is currently no lettuce object, the next transaction must be a produce
        lettuce.append('produced')
        return produce_gen('Lettuce', 'Lettuce', 0, sys_time, '500', [])
    else:
        while 1:
            picked_index = int((current_object_count+1)*np.random.rand())
            if picked_index==current_object_count:  # we should produce a new product
                lettuce.append('produced')
                return produce_gen('Lettuce', 'Lettuce', current_object_count, sys_time, '500', [])
            else:  # we should generate a transaction related to an existing product
                state = lettuce[picked_index]
                if state=='produced':
                    next_state = 100*np.random.rand()
                    if next_state<30:  # go to 'shipped' state
                        lettuce[picked_index] = 'shipped'
                        return shipped_gen('Lettuce', 'Lettuce', picked_index, sys_time, '20', 'ups', 'Mcdonalds', 'non-prime')
                    elif next_state<60: # go to 'stored' state
                        lettuce[picked_index] = 'stored'
                        return stored_gen('Lettuce', 'Lettuce', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        lettuce[picked_index] = 'terminated'
                        return terminated_gen('Lettuce', 'Lettuce', picked_index, sys_time, 'lost')
                elif state=='shipped':
                    lettuce[picked_index] = 'arrived'
                    return arrived_gen('Mcdonalds', 'Lettuce', picked_index, sys_time, 'John')
                elif state=='stored':
                    next_state = 100*np.random.rand()
                    if next_state<80:  # go to 'shipped' state
                        lettuce[picked_index] = 'shipped'
                        return shipped_gen('Lettuce', 'Lettuce', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'non-prime')
                    else:  # go to 'terminated' state
                        lettuce[picked_index] = 'terminated'
                        return terminated_gen('Lettuce', 'Lettuce', picked_index, sys_time, 'lost')


def data_gen(seed=1, n_trans=20, ave_trans_interval=10):
    np.random.seed(seed)
    sys_time = 0
    sauces = []
    buns = []
    sesames = []
    flour = []
    lettuce = []
    with open('data.txt', 'w') as data_file:
        for k in range(n_trans):
            if k%10000 == 0:
                print(k)
            sys_time += np.random.exponential(ave_trans_interval)
            data_file.write(next_transaction(sauces=sauces, buns=buns, sesames=sesames, flour=flour, lettuce=lettuce, sys_time=sys_time))
            data_file.write('\n')
    data_file.close()


def next_transaction(sauces, buns, sesames, flour, lettuce, sys_time):
    prob_among_sources = [0.33, 0.83, 1]
    next_type = np.random.rand()
    if next_type < prob_among_sources[0]:
        return sauces_gen(sauces, sys_time)
    elif next_type < prob_among_sources[1]:
        return buns_gen(buns, sesames, flour, sys_time)
    else:
        return lettuce_gen(lettuce, sys_time)


if __name__ == '__main__':
    data_gen(seed=11, n_trans=100000, ave_trans_interval=10)
