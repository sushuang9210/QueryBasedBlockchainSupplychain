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
                    return arrived_gen('Mcdonalds', 'Potato', picked_index, sys_time, 'John')
                elif state=='stored':
                    next_state = 100*np.random.rand()
                    if next_state<80:  # go to 'shipped' state
                        Potato[picked_index] = 'shipped'
                        return shipped_gen('Potato', 'Potato', picked_index, sys_time, '20', 'ups', 'Mcdonalds',
                                           'non-prime')
                    else:  # go to 'terminated' state
                        Potato[picked_index] = 'terminated'
                        return terminated_gen('Potato', 'Potato', picked_index, sys_time, 'lost')
