#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle

# Sample data.
example_dict = {9:"6",2:"2",3:"f"}

######################
# Create pickle file.#
######################

# Create a pickle file named "demo".
pickle_out = open("demo","wb")
# Write example_dict to "demo".
pickle.dump(example_dict, pickle_out)
# Close the file.
pickle_out.close()

############################################
# Open and assign values using pickle file.#
############################################

# Open pickle file named "demo"
pickle_in = open("demo","rb")
# Load information in the pickle file.
example_dict = pickle.load(pickle_in)
# Close the file.
pickle_in.close()

# Will print example_dict defined above.
print(example_dict)

