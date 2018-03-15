__author__ = 'Ke Wang'
__copyright__ = 'Copyright 2018, Ke Wang'
__version__ = '0.1'
__email__ = 'kewang1@andrew.cmu.edu'

import numpy as np
from util import *

def Beef_Patty_gen(Beef_Patty, sys_time):
    current_object_count = len(Beef_Patty)
    if current_object_count == 0:  # there is currently no Beef_Patty object, the next transaction must be a produce
        Beef_Patty.append('produced')
        return produce_gen('Beef', 'Beef', 0, sys_time, '500', [])
    else:
        while 1:
            picked_index = int((current_object_count + 1) * np.random.rand())
            if picked_index == current_object_count:  # we should produce a new product
                Beef_Patty.append('produced')
                return produce_gen('Beef', 'Beef', current_object_count, sys_time, '500', [])
            else:  # we should generate a transaction related to an existing product
                state = Beef_Patty[picked_index]
                if state == 'produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Beef_Patty[picked_index] = 'shipped'
                        return shipped_gen('Beef', 'Beef', picked_index, sys_time, '20', 'ups', 'Beef_Patty',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Beef_Patty[picked_index] = 'stored'
                        return stored_gen('Beef', 'Beef', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Beef_Patty[picked_index] = 'terminated'
                        return terminated_gen('Beef', 'Beef', picked_index, sys_time, 'lost')
                elif state == 'shipped':
                    Beef_Patty[picked_index] = 'arrived'
                    return arrived_gen('Beef_Patty', 'Beef', picked_index, sys_time, 'Martin')
                elif state == 'stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Beef_Patty[picked_index] = 'shipped'
                        return shipped_gen('Beef', 'Beef', picked_index, sys_time, '20', 'ups', 'Beef_Patty',
                                           'non-prime')
                    else:  # go to 'terminated' state
                        Beef_Patty[picked_index] = 'terminated'
                        return terminated_gen('Beef', 'Beef', picked_index, sys_time, 'lost')
                elif state == 'arrived':
                    Beef_Patty[picked_index] = 's produced'
                    return produce_gen('Beef_Patty', 'Beef_Patty', picked_index, sys_time, '500', [('Beef', picked_index)])

                elif state == 's produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Beef_Patty[picked_index] = 's shipped'
                        return shipped_gen('Beef_Patty', 'Beef_Patty', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Beef_Patty[picked_index] = 's stored'
                        return stored_gen('Beef_Patty', 'Beef_Patty', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Beef_Patty[picked_index] = 'terminated'
                        return terminated_gen('Beef_Patty', 'Beef_Patty', picked_index, sys_time, 'sold')
                elif state == 's shipped':
                    Beef_Patty[picked_index] = 's arrived'
                    return arrived_gen('Mcdonalds', 'Beef_Patty', picked_index, sys_time, 'Joe')
                elif state == 's stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Beef_Patty[picked_index] = 's shipped'
                        return shipped_gen('Beef_Patty', 'Beef_Patty', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    else:  # go to 'terminated' state
                        Beef_Patty[picked_index] = 'terminated'
                        return terminated_gen('Beef_Patty', 'Beef_Patty', picked_index, sys_time, 'lost')


def Ketchup_gen(Ketchup, sys_time):
    current_object_count = len(Ketchup)
    if current_object_count == 0:  # there is currently no Ketchup object, the next transaction must be a produce
        Ketchup.append('produced')
        return produce_gen('Tomato', 'Tomato', 0, sys_time, '500', [])
    else:
        while 1:
            picked_index = int((current_object_count + 1) * np.random.rand())
            if picked_index == current_object_count:  # we should produce a new product
                Ketchup.append('produced')
                return produce_gen('Tomato', 'Tomato', current_object_count, sys_time, '500', [])
            else:  # we should generate a transaction related to an existing product
                state = Ketchup[picked_index]
                if state == 'produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Ketchup[picked_index] = 'shipped'
                        return shipped_gen('Tomato', 'Tomato', picked_index, sys_time, '20', 'ups', 'Ketchup',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Ketchup[picked_index] = 'stored'
                        return stored_gen('Tomato', 'Tomato', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Ketchup[picked_index] = 'terminated'
                        return terminated_gen('Tomato', 'Tomato', picked_index, sys_time, 'lost')
                elif state == 'shipped':
                    Ketchup[picked_index] = 'arrived'
                    return arrived_gen('Ketchup', 'Tomato', picked_index, sys_time, 'Tom')
                elif state == 'stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Ketchup[picked_index] = 'shipped'
                        return shipped_gen('Tomato', 'Tomato', picked_index, sys_time, '20', 'ups', 'Ketchup',
                                           'non-prime')
                    else:  # go to 'terminated' state
                        Ketchup[picked_index] = 'terminated'
                        return terminated_gen('Tomato', 'Tomato', picked_index, sys_time, 'lost')
                elif state == 'arrived':
                    Ketchup[picked_index] = 's produced'
                    return produce_gen('Ketchup', 'Ketchup', picked_index, sys_time, '500', [('Tomato', picked_index)])

                elif state == 's produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Ketchup[picked_index] = 's shipped'
                        return shipped_gen('Ketchup', 'Ketchup', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Ketchup[picked_index] = 's stored'
                        return stored_gen('Ketchup', 'Ketchup', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Ketchup[picked_index] = 'terminated'
                        return terminated_gen('Ketchup', 'Ketchup', picked_index, sys_time, 'sold')
                elif state == 's shipped':
                    Ketchup[picked_index] = 's arrived'
                    return arrived_gen('Mcdonalds', 'Ketchup', picked_index, sys_time, 'Joe')
                elif state == 's stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Ketchup[picked_index] = 's shipped'
                        return shipped_gen('Ketchup', 'Ketchup', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    else:  # go to 'terminated' state
                        Ketchup[picked_index] = 'terminated'
                        return terminated_gen('Ketchup', 'Ketchup', picked_index, sys_time, 'lost')

def Chicken_Patty_gen(Chicken_Patty, sys_time):
    current_object_count = len(Chicken_Patty)
    if current_object_count == 0:  # there is currently no Chicken_Patty object, the next transaction must be a produce
        Chicken_Patty.append('produced')
        return produce_gen('Chicken', 'Chicken', 0, sys_time, '500', [])
    else:
        while 1:
            picked_index = int((current_object_count + 1) * np.random.rand())
            if picked_index == current_object_count:  # we should produce a new product
                Chicken_Patty.append('produced')
                return produce_gen('Chicken', 'Chicken', current_object_count, sys_time, '500', [])
            else:  # we should generate a transaction related to an existing product
                state = Chicken_Patty[picked_index]
                if state == 'produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Chicken_Patty[picked_index] = 'shipped'
                        return shipped_gen('Chicken', 'Chicken', picked_index, sys_time, '20', 'ups', 'Chicken_Patty',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Chicken_Patty[picked_index] = 'stored'
                        return stored_gen('Chicken', 'Chicken', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Chicken_Patty[picked_index] = 'terminated'
                        return terminated_gen('Chicken', 'Chicken', picked_index, sys_time, 'lost')
                elif state == 'shipped':
                    Chicken_Patty[picked_index] = 'arrived'
                    return arrived_gen('Chicken_Patty', 'Chicken', picked_index, sys_time, 'Lisa')
                elif state == 'stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Chicken_Patty[picked_index] = 'shipped'
                        return shipped_gen('Chicken', 'Chicken', picked_index, sys_time, '20', 'ups', 'Chicken_Patty',
                                           'non-prime')
                    else:  # go to 'terminated' state
                        Chicken_Patty[picked_index] = 'terminated'
                        return terminated_gen('Chicken', 'Chicken', picked_index, sys_time, 'lost')
                elif state == 'arrived':
                    Chicken_Patty[picked_index] = 's produced'
                    return produce_gen('Chicken_Patty', 'Chicken_Patty', picked_index, sys_time, '500', [('Chicken', picked_index)])

                elif state == 's produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Chicken_Patty[picked_index] = 's shipped'
                        return shipped_gen('Chicken_Patty', 'Chicken_Patty', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Chicken_Patty[picked_index] = 's stored'
                        return stored_gen('Chicken_Patty', 'Chicken_Patty', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Chicken_Patty[picked_index] = 'terminated'
                        return terminated_gen('Chicken_Patty', 'Chicken_Patty', picked_index, sys_time, 'sold')
                elif state == 's shipped':
                    Chicken_Patty[picked_index] = 's arrived'
                    return arrived_gen('Mcdonalds', 'Chicken_Patty', picked_index, sys_time, 'Joe')
                elif state == 's stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Chicken_Patty[picked_index] = 's shipped'
                        return shipped_gen('Chicken_Patty', 'Chicken_Patty', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    else:  # go to 'terminated' state
                        Chicken_Patty[picked_index] = 'terminated'
                        return terminated_gen('Chicken_Patty', 'Chicken_Patty', picked_index, sys_time, 'lost')

def Bacon_gen(Bacon, sys_time):
    current_object_count = len(Bacon)
    if current_object_count == 0:  # there is currently no Bacon object, the next transaction must be a produce
        Bacon.append('produced')
        return produce_gen('Pork', 'Pork', 0, sys_time, '500', [])
    else:
        while 1:
            picked_index = int((current_object_count + 1) * np.random.rand())
            if picked_index == current_object_count:  # we should produce a new product
                Bacon.append('produced')
                return produce_gen('Pork', 'Pork', current_object_count, sys_time, '500', [])
            else:  # we should generate a transaction related to an existing product
                state = Bacon[picked_index]
                if state == 'produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Bacon[picked_index] = 'shipped'
                        return shipped_gen('Pork', 'Pork', picked_index, sys_time, '20', 'ups', 'Bacon',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Bacon[picked_index] = 'stored'
                        return stored_gen('Pork', 'Pork', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Bacon[picked_index] = 'terminated'
                        return terminated_gen('Pork', 'Pork', picked_index, sys_time, 'lost')
                elif state == 'shipped':
                    Bacon[picked_index] = 'arrived'
                    return arrived_gen('Bacon', 'Pork', picked_index, sys_time, 'Jerry')
                elif state == 'stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Bacon[picked_index] = 'shipped'
                        return shipped_gen('Pork', 'Pork', picked_index, sys_time, '20', 'ups', 'Bacon',
                                           'non-prime')
                    else:  # go to 'terminated' state
                        Bacon[picked_index] = 'terminated'
                        return terminated_gen('Pork', 'Pork', picked_index, sys_time, 'lost')
                elif state == 'arrived':
                    Bacon[picked_index] = 's produced'
                    return produce_gen('Bacon', 'Bacon', picked_index, sys_time, '500', [('Pork', picked_index)])

                elif state == 's produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Bacon[picked_index] = 's shipped'
                        return shipped_gen('Bacon', 'Bacon', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Bacon[picked_index] = 's stored'
                        return stored_gen('Bacon', 'Bacon', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Bacon[picked_index] = 'terminated'
                        return terminated_gen('Bacon', 'Bacon', picked_index, sys_time, 'sold')
                elif state == 's shipped':
                    Bacon[picked_index] = 's arrived'
                    return arrived_gen('Mcdonalds', 'Bacon', picked_index, sys_time, 'Joe')
                elif state == 's stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Bacon[picked_index] = 's shipped'
                        return shipped_gen('Bacon', 'Bacon', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    else:  # go to 'terminated' state
                        Bacon[picked_index] = 'terminated'
                        return terminated_gen('Bacon', 'Bacon', picked_index, sys_time, 'lost')

def Cheese_gen(Cheese, sys_time):
    current_object_count = len(Cheese)
    if current_object_count == 0:  # there is currently no Cheese object, the next transaction must be a produce
        Cheese.append('produced')
        return produce_gen('Milk', 'Milk', 0, sys_time, '500', [])
    else:
        while 1:
            picked_index = int((current_object_count + 1) * np.random.rand())
            if picked_index == current_object_count:  # we should produce a new product
                Cheese.append('produced')
                return produce_gen('Milk', 'Milk', current_object_count, sys_time, '500', [])
            else:  # we should generate a transaction related to an existing product
                state = Cheese[picked_index]
                if state == 'produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Cheese[picked_index] = 'shipped'
                        return shipped_gen('Milk', 'Milk', picked_index, sys_time, '20', 'ups', 'Cheese',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Cheese[picked_index] = 'stored'
                        return stored_gen('Milk', 'Milk', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Cheese[picked_index] = 'terminated'
                        return terminated_gen('Milk', 'Milk', picked_index, sys_time, 'lost')
                elif state == 'shipped':
                    Cheese[picked_index] = 'arrived'
                    return arrived_gen('Cheese', 'Milk', picked_index, sys_time, 'Nina')
                elif state == 'stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Cheese[picked_index] = 'shipped'
                        return shipped_gen('Milk', 'Milk', picked_index, sys_time, '20', 'ups', 'Cheese',
                                           'non-prime')
                    else:  # go to 'terminated' state
                        Cheese[picked_index] = 'terminated'
                        return terminated_gen('Milk', 'Milk', picked_index, sys_time, 'lost')
                elif state == 'arrived':
                    Cheese[picked_index] = 's produced'
                    return produce_gen('Cheese', 'Cheese', picked_index, sys_time, '500', [('Milk', picked_index)])

                elif state == 's produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Cheese[picked_index] = 's shipped'
                        return shipped_gen('Cheese', 'Cheese', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Cheese[picked_index] = 's stored'
                        return stored_gen('Cheese', 'Cheese', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Cheese[picked_index] = 'terminated'
                        return terminated_gen('Cheese', 'Cheese', picked_index, sys_time, 'sold')
                elif state == 's shipped':
                    Cheese[picked_index] = 's arrived'
                    return arrived_gen('Mcdonalds', 'Cheese', picked_index, sys_time, 'Joe')
                elif state == 's stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Cheese[picked_index] = 's shipped'
                        return shipped_gen('Cheese', 'Cheese', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    else:  # go to 'terminated' state
                        Cheese[picked_index] = 'terminated'
                        return terminated_gen('Cheese', 'Cheese', picked_index, sys_time, 'lost')

def Mayonnaise_gen(Mayonnaise, sys_time):
    current_object_count = len(Mayonnaise)
    if current_object_count == 0:  # there is currently no Mayonnaise object, the next transaction must be a produce
        Mayonnaise.append('produced')
        return produce_gen('Egg', 'Egg', 0, sys_time, '500', [])
    else:
        while 1:
            picked_index = int((current_object_count + 1) * np.random.rand())
            if picked_index == current_object_count:  # we should produce a new product
                Mayonnaise.append('produced')
                return produce_gen('Egg', 'Egg', current_object_count, sys_time, '500', [])
            else:  # we should generate a transaction related to an existing product
                state = Mayonnaise[picked_index]
                if state == 'produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Mayonnaise[picked_index] = 'shipped'
                        return shipped_gen('Egg', 'Egg', picked_index, sys_time, '20', 'ups', 'Mayonnaise',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Mayonnaise[picked_index] = 'stored'
                        return stored_gen('Egg', 'Egg', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Mayonnaise[picked_index] = 'terminated'
                        return terminated_gen('Egg', 'Egg', picked_index, sys_time, 'lost')
                elif state == 'shipped':
                    Mayonnaise[picked_index] = 'arrived'
                    return arrived_gen('Mayonnaise', 'Egg', picked_index, sys_time, 'Teddy')
                elif state == 'stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Mayonnaise[picked_index] = 'shipped'
                        return shipped_gen('Egg', 'Egg', picked_index, sys_time, '20', 'ups', 'Mayonnaise',
                                           'non-prime')
                    else:  # go to 'terminated' state
                        Mayonnaise[picked_index] = 'terminated'
                        return terminated_gen('Egg', 'Egg', picked_index, sys_time, 'lost')
                elif state == 'arrived':
                    Mayonnaise[picked_index] = 's produced'
                    return produce_gen('Mayonnaise', 'Mayonnaise', picked_index, sys_time, '500', [('Egg', picked_index)])

                elif state == 's produced':
                    next_state = 100 * np.random.rand()
                    if next_state < 30:  # go to 'shipped' state
                        Mayonnaise[picked_index] = 's shipped'
                        return shipped_gen('Mayonnaise', 'Mayonnaise', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    elif next_state < 60:  # go to 'stored' state
                        Mayonnaise[picked_index] = 's stored'
                        return stored_gen('Mayonnaise', 'Mayonnaise', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Mayonnaise[picked_index] = 'terminated'
                        return terminated_gen('Mayonnaise', 'Mayonnaise', picked_index, sys_time, 'sold')
                elif state == 's shipped':
                    Mayonnaise[picked_index] = 's arrived'
                    return arrived_gen('Mcdonalds', 'Mayonnaise', picked_index, sys_time, 'Joe')
                elif state == 's stored':
                    next_state = 100 * np.random.rand()
                    if next_state < 80:  # go to 'shipped' state
                        Mayonnaise[picked_index] = 's shipped'
                        return shipped_gen('Mayonnaise', 'Mayonnaise', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'prime')
                    else:  # go to 'terminated' state
                        Mayonnaise[picked_index] = 'terminated'
                        return terminated_gen('Mayonnaise', 'Mayonnaise', picked_index, sys_time, 'lost')

def Bun_gen(Bun, sesames, flour, sys_time):
    sesame_or_flour = np.random.rand()
    if sesame_or_flour < 0.5: # look at sesame
        current_object_count = len(sesames)
        if current_object_count == 0:  # there is currently no Ketchup object, the next transaction must be a produce
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

def Pickles_gen(Pickles, Cucumber, Vinegar, sys_time):
    sesame_or_Vinegar = np.random.rand()
    if sesame_or_Vinegar < 0.5: # look at sesame
        current_object_count = len(Cucumber)
        if current_object_count == 0:  # there is currently no Ketchup object, the next transaction must be a produce
            Cucumber.append('produced')
            return produce_gen('Cucumber', 'Cucumber', 0, sys_time, '500', [])
        else:
            while 1:
                picked_index = int((current_object_count + 1) * np.random.rand())
                if picked_index == current_object_count:  # we should produce a new product
                    Cucumber.append('produced')
                    return produce_gen('Cucumber', 'Cucumber', current_object_count, sys_time, '500', [])
                else:  # we should generate a transaction related to an existing product
                    state = Cucumber[picked_index]
                    if state == 'produced':
                        next_state = 100 * np.random.rand()
                        if next_state < 30:  # go to 'shipped' state
                            Cucumber[picked_index] = 'shipped'
                            return shipped_gen('Cucumber', 'Cucumber', picked_index, sys_time, '20', 'ups', 'Pickles',
                                               'prime')
                        elif next_state < 60:  # go to 'stored' state
                            Cucumber[picked_index] = 'stored'
                            return stored_gen('Cucumber', 'Cucumber', picked_index, sys_time, '15')
                        else:  # go to 'terminated' state
                            Cucumber[picked_index] = 'terminated'
                            return terminated_gen('Cucumber', 'Cucumber', picked_index, sys_time, 'lost')
                    elif state == 'shipped':
                        Cucumber[picked_index] = 'arrived'
                        return arrived_gen('Pickles', 'Cucumber', picked_index, sys_time, 'Mike')
                    elif state == 'stored':
                        next_state = 100 * np.random.rand()
                        if next_state < 80:  # go to 'shipped' state
                            Cucumber[picked_index] = 'shipped'
                            return shipped_gen('Cucumber', 'Cucumber', picked_index, sys_time, '20', 'ups', 'Pickles',
                                               'prime')
                        else:  # go to 'terminated' state
                            Cucumber[picked_index] = 'terminated'
                            return terminated_gen('Cucumber', 'Cucumber', picked_index, sys_time, 'expired')
                    elif state == 'arrived':
                        for index in range(len(Vinegar)):
                            if Vinegar[index] == 'arrived':
                                Cucumber[picked_index] = 'b produced'
                                Vinegar[index] = 'used'
                                return produce_gen('Pickles', 'Pickles', picked_index, sys_time, '500', [('Cucumber', picked_index), ('Vinegar', index)])

                    elif state == 'b produced':
                        next_state = 100 * np.random.rand()
                        if next_state < 30:  # go to 'shipped' state
                            Cucumber[picked_index] = 'b shipped'
                            return shipped_gen('Pickles', 'Pickles', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                               'prime')
                        elif next_state < 60:  # go to 'stored' state
                            Cucumber[picked_index] = 'b stored'
                            return stored_gen('Pickles', 'Pickles', picked_index, sys_time, '15')
                        else:  # go to 'terminated' state
                            Cucumber[picked_index] = 'terminated'
                            return terminated_gen('Pickles', 'Pickles', picked_index, sys_time, 'expired')
                    elif state == 'b shipped':
                        Cucumber[picked_index] = 'b arrived'
                        return arrived_gen('Mcdonalds', 'Pickles', picked_index, sys_time, 'Joe')
                    elif state == 'b stored':
                        next_state = 100 * np.random.rand()
                        if next_state < 80:  # go to 'shipped' state
                            Cucumber[picked_index] = 'b shipped'
                            return shipped_gen('Pickles', 'Pickles', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                               'prime')
                        else:  # go to 'terminated' state
                            Cucumber[picked_index] = 'terminated'
                            return terminated_gen('Pickles', 'Pickles', picked_index, sys_time, 'expired')

    else:
        current_object_count = len(Vinegar)
        if current_object_count == 0:  # there is currently no lettuce object, the next transaction must be a produce
            Vinegar.append('produced')
            return produce_gen('Vinegar', 'Vinegar', 0, sys_time, '500', [])
        else:
            while 1:
                picked_index = int((current_object_count + 1) * np.random.rand())
                if picked_index == current_object_count:  # we should produce a new product
                    Vinegar.append('produced')
                    return produce_gen('Vinegar', 'Vinegar', current_object_count, sys_time, '500', [])
                else:  # we should generate a transaction related to an existing product
                    state = Vinegar[picked_index]
                    if state == 'produced':
                        next_state = 100 * np.random.rand()
                        if next_state < 30:  # go to 'shipped' state
                            Vinegar[picked_index] = 'shipped'
                            return shipped_gen('Vinegar', 'Vinegar', picked_index, sys_time, '20', 'ups', 'Pickles',
                                               'non-prime')
                        elif next_state < 60:  # go to 'stored' state
                            Vinegar[picked_index] = 'stored'
                            return stored_gen('Vinegar', 'Vinegar', picked_index, sys_time, '15')
                        else:  # go to 'terminated' state
                            Vinegar[picked_index] = 'terminated'
                            return terminated_gen('Vinegar', 'Vinegar', picked_index, sys_time, 'lost')
                    elif state == 'shipped':
                        Vinegar[picked_index] = 'arrived'
                        return arrived_gen('Pickles', 'Vinegar', picked_index, sys_time, 'Mike')
                    elif state == 'stored':
                        next_state = 100 * np.random.rand()
                        if next_state < 80:  # go to 'shipped' state
                            Vinegar[picked_index] = 'shipped'
                            return shipped_gen('Vinegar', 'Vinegar', picked_index, sys_time, '20', 'ups', 'Pickles',
                                               'non-prime')
                        else:  # go to 'terminated' state
                            Vinegar[picked_index] = 'terminated'
                            return terminated_gen('Vinegar', 'Vinegar', picked_index, sys_time, 'expired')

def Lettuce_gen(Lettuce, sys_time):
    current_object_count = len(Lettuce)
    if current_object_count == 0:  # there is currently no Lettuce object, the next transaction must be a produce
        Lettuce.append('produced')
        return produce_gen('Lettuce', 'Lettuce', 0, sys_time, '500', [])
    else:
        while 1:
            picked_index = int((current_object_count+1)*np.random.rand())
            if picked_index==current_object_count:  # we should produce a new product
                Lettuce.append('produced')
                return produce_gen('Lettuce', 'Lettuce', current_object_count, sys_time, '500', [])
            else:  # we should generate a transaction related to an existing product
                state = Lettuce[picked_index]
                if state=='produced':
                    next_state = 100*np.random.rand()
                    if next_state<30:  # go to 'shipped' state
                        Lettuce[picked_index] = 'shipped'
                        return shipped_gen('Lettuce', 'Lettuce', picked_index, sys_time, '20', 'ups', 'Mcdonalds', 'non-prime')
                    elif next_state<60: # go to 'stored' state
                        Lettuce[picked_index] = 'stored'
                        return stored_gen('Lettuce', 'Lettuce', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Lettuce[picked_index] = 'terminated'
                        return terminated_gen('Lettuce', 'Lettuce', picked_index, sys_time, 'lost')
                elif state=='shipped':
                    Lettuce[picked_index] = 'arrived'
                    return arrived_gen('Mcdonalds', 'Lettuce', picked_index, sys_time, 'Joe')
                elif state=='stored':
                    next_state = 100*np.random.rand()
                    if next_state<80:  # go to 'shipped' state
                        Lettuce[picked_index] = 'shipped'
                        return shipped_gen('Lettuce', 'Lettuce', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'non-prime')
                    else:  # go to 'terminated' state
                        Lettuce[picked_index] = 'terminated'
                        return terminated_gen('Lettuce', 'Lettuce', picked_index, sys_time, 'lost')

def Potato_gen(Potato, sys_time):
    current_object_count = len(Potato)
    if current_object_count == 0:  # there is currently no Potato object, the next transaction must be a produce
        Potato.append('produced')
        return produce_gen('Potato', 'Potato', 0, sys_time, '500', [])
    else:
        while 1:
            picked_index = int((current_object_count+1)*np.random.rand())
            if picked_index==current_object_count:  # we should produce a new product
                Potato.append('produced')
                return produce_gen('Potato', 'Potato', current_object_count, sys_time, '500', [])
            else:  # we should generate a transaction related to an existing product
                state = Potato[picked_index]
                if state=='produced':
                    next_state = 100*np.random.rand()
                    if next_state<30:  # go to 'shipped' state
                        Potato[picked_index] = 'shipped'
                        return shipped_gen('Potato', 'Potato', picked_index, sys_time, '20', 'ups', 'Mcdonalds', 'non-prime')
                    elif next_state<60: # go to 'stored' state
                        Potato[picked_index] = 'stored'
                        return stored_gen('Potato', 'Potato', picked_index, sys_time, '15')
                    else:  # go to 'terminated' state
                        Potato[picked_index] = 'terminated'
                        return terminated_gen('Potato', 'Potato', picked_index, sys_time, 'lost')
                elif state=='shipped':
                    Potato[picked_index] = 'arrived'
                    return arrived_gen('Mcdonalds', 'Potato', picked_index, sys_time, 'Joe')
                elif state=='stored':
                    next_state = 100*np.random.rand()
                    if next_state<80:  # go to 'shipped' state
                        Potato[picked_index] = 'shipped'
                        return shipped_gen('Potato', 'Potato', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'non-prime')
                    else:  # go to 'terminated' state
                        Potato[picked_index] = 'terminated'
                        return terminated_gen('Potato', 'Potato', picked_index, sys_time, 'lost')

def data_gen(seed=1, n_trans=20, ave_trans_interval=10):
    np.random.seed(seed)
    sys_time = 0
    beefPatty=[]
    chickenPatty=[]
    bacon=[]
    buns = []
    pickles=[]
    lettuce = []
    cheese=[]
    ketchup = []
    mayonnaise=[]
    potato=[]
    sesames = []
    flour = []
    cucumber=[]
    vinegar=[]


    with open('data.txt', 'w') as data_file:
        for k in range(n_trans):
            if k%10000 == 0:
                print(k)
            sys_time += np.random.exponential(ave_trans_interval)
            data_file.write(next_transaction(beefPatty=beefPatty,chickenPatty=chickenPatty,bacon=bacon,buns=buns,pickles=pickles,lettuce=lettuce,cheese=cheese,ketchup = ketchup,mayonnaise=mayonnaise,potato=potato,sesames = sesames,flour = flour,cucumber=cucumber,vinegar=vinegar,sys_time=sys_time))
            data_file.write('\n')
    data_file.close()


def next_transaction(beefPatty,chickenPatty,bacon,buns,pickles,lettuce,cheese,ketchup,mayonnaise,potato,sesames,flour,cucumber,vinegar,sys_time):
    prob_among_sources = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    next_type = np.random.rand()
    if next_type < prob_among_sources[0]:
        return Beef_Patty_gen(beefPatty, sys_time)
    elif next_type < prob_among_sources[1]:
        return Chicken_Patty_gen(chickenPatty, sys_time)
    elif next_type < prob_among_sources[2]:
        return Bacon_gen(bacon,sys_time)
    elif next_type < prob_among_sources[3]:
        return Cheese_gen(cheese, sys_time)
    elif next_type < prob_among_sources[4]:
        return Mayonnaise_gen(mayonnaise, sys_time)
    elif next_type < prob_among_sources[5]:
        return Ketchup_gen(ketchup, sys_time)
    elif next_type < prob_among_sources[6]:
        return Bun_gen(buns, sesames, flour, sys_time)
    elif next_type < prob_among_sources[7]:
        return Pickles_gen(pickles, cucumber, vinegar, sys_time)
    elif next_type < prob_among_sources[8]:
        return Potato_gen(potato, sys_time)
    else:
        return Lettuce_gen(lettuce, sys_time)


if __name__ == '__main__':
    data_gen(seed=11, n_trans=100000, ave_trans_interval=10)
