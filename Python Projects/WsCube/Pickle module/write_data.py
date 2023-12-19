import pickle

listing = [10, 20, 30, 40, 50, 60, 70]

file = open('write_all_data.txt', 'wb')

pickle.dump(listing, file)

file.close()