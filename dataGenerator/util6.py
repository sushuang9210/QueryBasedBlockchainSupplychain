__author__ = 'Ke Wang'
__copyright__ = 'Copyright 2018, Ke Wang'
__version__ = '0.1'
__email__ = 'kewang1@andrew.cmu.edu'

products={}
products['Sauce']=1
products['Lettuce']=2
products['Bun']=3
products['Tomato']=4
products['Flour']=5
products['Sesames']=6
products['Mcdonalds']=7

company={}
company['ups']=1

package={}
package['prime']=1
package['non-prime']=2

signature={}
signature['Tom']=1
signature['Joe']=2
signature['Milda']=3
signature['John']=4

reasons={}
reasons['lost']=1
reasons['sold']=2
reasons['expired']=3

#produced: 1;shipped: 2;arrived: 3;storeed: 4;terminated: 5

def produce_gen(supplier, type, ID, time, weight, sources):
    #result = str(products[supplier])+' '+str(products[type])+' '+str(ID+1)+' 1 '+str(int(100*time))+' '+str(weight)+' '+str(len(sources))
    result = str(products[type])+' '+str(ID+1)+' 1 '+str(int(100*time))+' '+str(weight)
    #for source in sources:
        #result += (' '+str(products[source[0]])+' '+str(source[1]))
    for i in range(2):
        if i<len(sources):
            result += (' '+str(products[sources[i][0]])+' '+str(sources[i][1]))
        else:
            result += (' '+str(6)+' '+str(0))
    result+=(' '+str(products[supplier]))
    return result


def shipped_gen(supplier, type, ID, time, trans_temp, trans_comp, dest_supplier, package_info):
    result = str(products[type])+' '+str(ID+1)+' 2 '+str(int(100*time))+' '+str(products[dest_supplier])+' '+str(100*int(trans_temp)+10*company[trans_comp]+package[package_info])+' '+str(products[supplier])
    return result


def arrived_gen(supplier, type, ID, time, signed_name):
    result = str(products[type])+' '+str(ID+1)+' 3 '+str(int(100*time))+' '+str(products[supplier])+' '+str(signature[signed_name])+' '+str(products[supplier])
    return result


def stored_gen(supplier, type, ID, time, stored_temp):
    result = str(products[type])+' '+str(ID+1)+' 4 '+str(int(100*time))+' 0 '+stored_temp+' '+str(products[supplier])
    return result


def terminated_gen(supplier, type, ID, time, reason):
    result = str(products[type])+' '+str(ID+1)+' 5 '+str(int(100*time))+' 0 '+str(reasons[reason])+' '+str(products[supplier])
    return result
