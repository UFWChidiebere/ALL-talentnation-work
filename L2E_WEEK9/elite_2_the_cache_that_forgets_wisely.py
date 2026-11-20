# Time: O(1) per cache lookup, hit refresh, or eviction; Space: O(max_size) to store cached entries.
# Reasoning: Standard Python dictionaries preserve insertion order, allowing O(1) pop/re-insert to refresh recency and O(1) next(iter(cache)) to evict the oldest key.
def lru_cache(max_size=128):
    def decorator(func):
        cache = {}

        def wrapper(*args):
            wrapper.calls += 1
            key = args

            if key in cache:
                wrapper.hits += 1
                # Refresh recency by removing and re-inserting at the end
                val = cache.pop(key)
                cache[key] = val
                return val

            wrapper.misses += 1
            result = func(*args)

            if max_size == 0:
                return result

            if max_size is not None and len(cache) >= max_size:
                oldest_key = next(iter(cache))
                del cache[oldest_key]

            cache[key] = result
            return result

        def keys():
            return list(cache.keys())

        def clear():
            cache.clear()
            wrapper.hits = 0
            wrapper.misses = 0
            wrapper.calls = 0

        wrapper.hits = 0
        wrapper.misses = 0
        wrapper.calls = 0
        wrapper.keys = keys
        wrapper.clear = clear
        return wrapper

    return decorator


# Time: O(1) per cache lookup or eviction; Space: O(max_size) to store cached entries.
# Reasoning: Dictionary hash lookups take O(1) average time, and evicting the earliest inserted key via next(iter(cache)) avoids scanning the dictionary.
def fifo_cache(max_size=128):
    def decorator(func):
        cache = {}

        def wrapper(*args):
            wrapper.calls += 1
            key = args

            if key in cache:
                wrapper.hits += 1
                # Do NOT update insertion order on a hit in FIFO
                return cache[key]

            wrapper.misses += 1
            result = func(*args)

            if max_size == 0:
                return result

            if max_size is not None and len(cache) >= max_size:
                oldest_key = next(iter(cache))
                del cache[oldest_key]

            cache[key] = result
            return result

        def keys():
            return list(cache.keys())

        def clear():
            cache.clear()
            wrapper.hits = 0
            wrapper.misses = 0
            wrapper.calls = 0

        wrapper.hits = 0
        wrapper.misses = 0
        wrapper.calls = 0
        wrapper.keys = keys
        wrapper.clear = clear
        return wrapper

    return decorator


# Bonus: LRU cache that also expires entries older than max_age_calls function calls
# Time: O(1) amortized per call (worst-case O(n) only when sweeping multiple expired keys); Space: O(max_size).
# Reasoning: Storing (value, call_timestamp) in insertion order allows sweeping expired entries from the front of the dictionary until a fresh entry is reached.
def lru_ttl_calls_cache(max_size=128, max_age_calls=None):
    def decorator(func):
        cache = {}  # Maps key -> (value, last_used_call_number)

        def wrapper(*args):
            wrapper.calls += 1
            current_call = wrapper.calls

            # Evict any entries whose age exceeds max_age_calls (oldest are at the front)
            if max_age_calls is not None:
                expired = []
                for k, (_, last_call) in cache.items():
                    if current_call - last_call > max_age_calls:
                        expired.append(k)
                    else:
                        break
                for k in expired:
                    del cache[k]

            key = args
            if key in cache:
                wrapper.hits += 1
                val, _ = cache.pop(key)
                cache[key] = (val, current_call)
                return val

            wrapper.misses += 1
            result = func(*args)

            if max_size == 0:
                return result

            if max_size is not None and len(cache) >= max_size:
                oldest_key = next(iter(cache))
                del cache[oldest_key]

            cache[key] = (result, current_call)
            return result

        def keys():
            return list(cache.keys())

        def clear():
            cache.clear()
            wrapper.hits = 0
            wrapper.misses = 0
            wrapper.calls = 0

        wrapper.hits = 0
        wrapper.misses = 0
        wrapper.calls = 0
        wrapper.keys = keys
        wrapper.clear = clear
        return wrapper

    return decorator


# --- Written Analysis (Required Comments) ---
#
# 1. Does FIFO beating LRU on [1, 2, 1, 3, 2, 1] mean FIFO is better?
#    No. That sequence is a cyclic loop of 3 distinct items (1, 2, 3) on a cache of size 2;
#    refreshing '1' caused LRU to evict '2' right before '2' was requested next, creating worst-case thrashing.
#    LRU strongly favours workloads with temporal locality (where recently accessed items are likely to be requested again soon),
#    whereas FIFO works well when data naturally ages out in strict chronological order (such as streaming logs or time-bucketed events).
#
# 2. Time complexity of an LRU hit, where it could become O(n), and how we avoided it:
#    A cache hit is O(1) average time because dict lookup, dict.pop(key), and dict[key] = val are all hash-table operations.
#    It would become O(n) if we tracked order in a Python list and used list.remove(key) or rebuilt the dictionary on every hit;
#    we avoided this by relying on Python's built-in insertion-ordered dict via pop() + re-insert.
#
# 3. Real-world system where LRU is the right call:
#    A web browser's page/image cache or an operating system's virtual memory page table: users actively navigate back and forth
#    between recently opened tabs or active working-set memory pages, while pages untouched for hours are safe to evict.


# --- Main Section (Testing) ---
if __name__ == "__main__":
    # 1. Prompt Example: sequence [1, 2, 1, 3, 2, 1] with max_size = 2
    @lru_cache(max_size=2)
    def f_lru(x):
        return x * x

    @fifo_cache(max_size=2)
    def f_fifo(x):
        return x * x

    seq = [1, 2, 1, 3, 2, 1]
    for item in seq:
        f_lru(item)
        f_fifo(item)

    print(f"LRU  -> hits: {f_lru.hits}, misses: {f_lru.misses}, calls: {f_lru.calls}, keys: {f_lru.keys()}")
    print(f"FIFO -> hits: {f_fifo.hits}, misses: {f_fifo.misses}, calls: {f_fifo.calls}, keys: {f_fifo.keys()}")

    # 2. Custom Test 1: Multiple arguments
    @lru_cache(max_size=2)
    def add(a, b):
        return a + b

    print("add(1, 2):", add(1, 2))
    print("add(3, 4):", add(3, 4))
    print("add(1, 2) hit:", add(1, 2))
    print("Multi-arg keys (oldest to newest):", add.keys(), "| hits:", add.hits)

    # 3. Custom Test 2 (Edge Case): max_size = 0 (nothing ever cached)
    @lru_cache(max_size=0)
    def zero_cache(x):
        return x + 10

    zero_cache(5)
    zero_cache(5)
    print("max_size=0 -> hits:", zero_cache.hits, "misses:", zero_cache.misses, "keys:", zero_cache.keys())

    # 4. Custom Test 3 (Edge Case): max_size = None (unlimited) + Bonus clear()
    @lru_cache(max_size=None)
    def unlimited(x):
        return x * 2

    for i in range(5):
        unlimited(i)
    unlimited(2)
    print("Unlimited before clear -> keys:", unlimited.keys(), "hits:", unlimited.hits)
    unlimited.clear()
    print("Unlimited after clear  -> keys:", unlimited.keys(), "hits:", unlimited.hits, "calls:", unlimited.calls)
