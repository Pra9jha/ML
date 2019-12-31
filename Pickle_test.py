import pickle

example_dictionary={"name":"Prashant","language":"Python","dep":"development"}
pickle_out=open("dict.picle","wb")
pickle.dump(example_dictionary,pickle_out)
pickle_out.close()


pickle_in=open("dict.picle","rb")
example_dict=pickle.load(pickle_in)
print(example_dictionary)


