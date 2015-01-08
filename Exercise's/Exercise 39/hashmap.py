# hashmap algorithm:
# 1. Convert a key to an integer using a hashing function: hash_key.
# 2. Convert this hash to a bucket number using a % (modulus) operator.
# 3. Get this buket from the aMap list of buckets,
#    and then traverse it to find the slot that contains the key we want.

def new(num_buckets=256):
    """Initializes new hashMap by create aMap variable with the given number of num_buckets."""
    aMap = []
    
    # Why using range(0, num_buckets) instead of range(num_buckets)?
    # What's the rationale for using one instead of the other? (range/xrange)
    for i in xrange(num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    """This will create a number and then convert it to
    an index for the aMap's buckets."""
    # hash() convert string to a num'.
    return hash(key) % len(aMap)

def get_bucket(aMap, key):
    """This function use hash_key() to find the bucket that a key could be in. 
    Since we have % len(aMap) in the hash_key() function, We know whatever 
    bucket_index will fit into the aMap list.
    After intializing bucket_id we can get the bucket where the key could be."""
    bucket_index = hash_key(aMap, key)
    return aMap[bucket_index]

def get_slot(aMap, key, default=None):
    """Simply rolls through every element of that bucket until it finds a matching key. 
    Once it does it returns the tuple("pair") of (i, k, v) which is the index the key was found in, 
    the key itself, and the value set for that key. 
    Returns -1, key, and default (None if not set) when not found."""
    bucket = get_bucket(aMap, key)

    # enumarete() - object iterator that return a tuple(pair) containing count(start by default at 0) 
    # and the values obtained from iterating over sequence.
    for i, kv in enumerate(bucket):
        k, v = kv
        
        if key == k:
                return i, k, v

    return -1, key, default

def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not existst, append to create it
        bucket.append((key, value))

def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)

    # for i in xrange(len(bucket)):
    for i in bucket:
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v

