#pickle module 
import pickle

#specify list as mylist
mylist = [1, 2, 3, 4]

#serialized the object mylist
ser = pickle.dumps(mylist)
print(ser)