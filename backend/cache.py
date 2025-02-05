from django.core.cache import cache

def get_or_set_cache(key, fetch_func, timeout=300):
    """
    Fetch data from cache or call `fetch_func` to retrieve and cache the data.
    :param key: Cache key
    :param fetch_func: Function to fetch data if not in cache
    :param timeout: Cache expiration time (in seconds)
    :return: Cached or fetched data
    """
    data = cache.get(key)
    if not data:
        print("Fetching data from the database")
        data = fetch_func()
        cache.set(key, data, timeout)
    print("Returning cached data")
    return data
