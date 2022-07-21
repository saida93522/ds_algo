#A function that returns the index of a value removing the need to perform a search is called a hash function. 
# In order for hash functions to work, it needs to consistently return the same output for the same input. Mapping strings to numbers

def get_one(x):
    """ returns '1' for all inputs """ 
    return 1

# print(get_one(2))
# print(get_one(9))

def find_length(x):
    """ returns the length of a string and uses it as the index. """
    #maps the string(x) to number(len(x))
    return len(x) 

# print(find_length('string'))
# print(find_length('integer'))


def phone_book(name):
    if name == 'Jenny':
        return 78536774
    if name == 'ER':
        return 911
    else:
        return None


my_list = [phone_book('Jenny'),phone_book('ER')]
# print(my_list[0])



# A hash function combined with an array creates a hash table.
# Hash tables uses hash functions to figure out where to store elements.
#  In python, dictionaries are implemented as  Hash tables. dictionary is an abstract data type that consist of a one to one relashionship, the key and the value.

# Hash tables are fast. retrieving,inserting, and removing elements take up a Time Complexcity of O(1).

phone_book = dict()
#  adding phone numbers
phone_book['jenny'] = 346778
phone_book['er'] = 911

# retrieving jenny phone number
# print(phone_book['jenny'])  # 346778

# Hash Tables use cases 
# Using Hash tables to prevent duplication

voted = {}

def check_voter(name):
    if voted.get(name):
        return "You already voted!"
    else:
        voted[name] = True
        return "You can vote!"

# print(check_voter('jenny')) # You can vote!
# print(check_voter('saida')) # You can vote!
# print(check_voter('mike')) #  You can vote!
# print(check_voter('saida')) # You already voted!

# if we were to store the voters in a list, we would have to do a simple search of all the people who have voted, thus the function would be really slow because we wold have to search though the entire list worst case. Using hash tables (dictionary) all we have to do is provide the name(key) and returns if the name exist in the table. this helps prevent duplication.

#Using hash tables as a cache

cache = {}

def get_page(url):
    #check if web page is already stored in our memory, then return it
    if cache.get(url):
        return cache[url]
    else:
        #if page is not cached, call server do extra fetching, save data in the cache then return it.
        data = get_data_from_server(url)
        cache[url] = data # save page in cache
        return data