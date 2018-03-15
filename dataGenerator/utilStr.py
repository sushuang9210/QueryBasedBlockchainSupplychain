__author__ = 'Ke Wang'
__copyright__ = 'Copyright 2018, Ke Wang'
__version__ = '0.1'
__email__ = 'kewang1@andrew.cmu.edu'


def produce_gen(supplier, type, ID, time, weight, sources):
    result = str(supplier)+' '+str(type)+' '+str(ID)+' produced '+str(time)+' '+str(weight)+' '+str(len(sources))
    for source in sources:
        result += (' '+str(source[0])+' '+str(source[1]))
    return result


def shipped_gen(supplier, type, ID, time, trans_temp, trans_comp, dest_supplier, package_info):
    result = str(supplier)+' '+str(type)+' '+str(ID)+' shipped '+str(time)+' '+str(trans_temp)+' '\
             +str(trans_comp)+' '+str(dest_supplier)+' '+str(package_info)
    return result


def arrived_gen(supplier, type, ID, time, signed_name):
    result = str(supplier)+' '+str(type)+' '+str(ID)+' arrived '+str(time)+' '+str(signed_name)
    return result


def stored_gen(supplier, type, ID, time, stored_temp):
    result = str(supplier)+' '+str(type)+' '+str(ID)+' stored '+str(time)+' '+str(stored_temp)
    return result


def terminated_gen(supplier, type, ID, time, reason):
    result = str(supplier)+' '+str(type)+' '+str(ID)+' terminated '+str(time)+' '+str(reason)
    return result