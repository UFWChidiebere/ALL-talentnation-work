# =====================================================================
# PART 1 & 2: RECURSION, DECORATORS, AND LRU CACHING (BONUS INCLUDED)
# =====================================================================

def memoize(max_size=None):
    """
    Decorator factory implementing a closure-based cache.
    Hard Bonus: Implements Least Recently Used (LRU) eviction logic 
    by leveraging Python's insertion-ordered dictionary behavior.
    """
    def decorator(func):
        cache = {}
        hits = 0
        misses = 0

        def wrapper(*args):
            nonlocal hits, misses
            # Explanation for conversion: Lists are unhashable in Python because they are mutable.
            # Dictionaries require keys to be immutable so their hash values remain stable.
            # We map any input lists into immutable tuples to make them valid hash keys.
            hashable_args = tuple(tuple(x) if isinstance(x, list) else x for x in args)

            if hashable_args in cache:
                hits += 1
                # LRU Shift: Move accessed item to the end (newest position)
                val = cache.pop(hashable_args)
                cache[hashable_args] = val
                return val

            misses += 1
            result = func(*args)

            if max_size is not None and len(cache) >= max_size:
                # Evict the oldest/least recently used entry (the first key in insertion order)
                oldest_key = next(iter(cache))
                del cache[oldest_key]

            cache[hashable_args] = result
            return result

        # Exposing tracking variables as callable attributes on the wrapper
        wrapper.hits = lambda: hits
        wrapper.misses = lambda: misses
        wrapper.calls = lambda: hits + misses
        return wrapper
    return decorator


# Time Complexity (Naive): O(2^(N + M)) where N is amount, M is number of coins.
# Exploration paths branch exponentially without pruning.
# Space Complexity (Naive): O(N) due to deep recursive stack frame allocation down to base amount 0.
# Time Complexity (Memoized): O(N * M) - every unique state configuration is computed exactly once.
# Space Complexity (Memoized): O(N * M) to preserve state records within our cache map.
def count_ways_raw(amount, coins, index=0):
    if amount == 0:
        return 1
    if amount < 0 or index >= len(coins):
        return 0
    # Binary Choice Tree: Include current coin or step forward to next option
    return count_ways_raw(amount - coins[index], coins, index) + count_ways_raw(amount, coins, index + 1)

# Apply our decorator to the raw recursive function
count_ways = memoize()(count_ways_raw)


# Time Complexity: O(2^N) - Naive recursive implementation with dual execution branching.
# Space Complexity: O(N) - Maximum call stack allocation frames running linearly up to input depth.
def fib_naive(n):
    fib_naive.calls += 1
    if n < 2: 
        return n
    return fib_naive(n-1) + fib_naive(n-2)
fib_naive.calls = 0


# Time Complexity: O(N) - Reduced to simple sequential linear evaluation loops due to structural memoization.
# Space Complexity: O(N) - Captures array structures for recursive lookup contexts and operational frames.
@memoize()
def fib_memo(n):
    if n < 2: 
        return n
    return fib_memo(n-1) + fib_memo(n-2)


# =====================================================================
# PART 3: OPTIMIZED HASH MAPS (O(N) DICTIONARY STRUCTURES)
# =====================================================================

# Time Complexity: O(N) - A clean two-pass architecture over the elements that completely avoids nested loops.
# Space Complexity: O(N) - Linear dictionary tracking allocation preserving elements as key pointers.
def longest_consecutive(nums):
    if not nums:
        return 0
    
    # Simulate a set's O(1) performance using a lookup map without using the set() builtin
    lookup = {x: True for x in nums}
    longest_run = 0
    
    for num in lookup:
        # Check if the number is the absolute start of a run (predecessor check)
        if (num - 1) not in lookup:
            current_num = num
            current_run = 1
            
            # Increment up through consecutive sequence elements
            while (current_num + 1) in lookup:
                current_num += 1
                current_run += 1
                
            if current_run > longest_run:
                longest_run = current_run
                
    return longest_run


# Time Complexity: O(N) - Single pass iteration checking compliments while incrementing a frequency dictionary.
# Space Complexity: O(N) - Memory scales to keep track of elements inside our target lookup table.
def count_pairs(nums, target):
    freq_map = {}
    pair_count = 0
    
    for num in nums:
        complement = target - num
        if complement in freq_map:
            pair_count += freq_map[complement]
            
        freq_map[num] = freq_map.get(num, 0) + 1
        
    return pair_count


# =====================================================================
# HARD BONUS: BOTTOM-UP ITERATIVE COIN COMBINATIONS
# =====================================================================

# Time Complexity: O(N * M) where N is amount and M is the size of the coins list.
# Space Complexity: O(N) - Highly optimized down to a single compact row array of size amount + 1.
def count_ways_iterative(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case: One way to make exactly zero value
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
            
    return dp[amount]


# =====================================================================
# PART 4: INSTRUMENTATION AND BIG O REPORT
# =====================================================================

def main():
    print("=== FIBONACCI PERFORMANCE TEST ===")
    for n in [10, 20, 25]:
        fib_naive.calls = 0
        fib_naive(n)
        
        # Reset and isolate a fresh memoized instance for metrics tracking
        @memoize()
        def temp_fib(x):
            if x < 2: return x
            return temp_fib(x-1) + temp_fib(x-2)
            
        temp_fib(n)
        print(f"n = {n} | Naive Calls: {fib_naive.calls:<8} | Memoized Calls: {temp_fib.calls()}")

    print(f"fib_memo(35) = {fib_memo(35)} (Misses: {fib_memo.misses()})")
    print(f"fib_memo(90) = {fib_memo(90)} (Misses: {fib_memo.misses()})")

    print("\n=== COIN COMBINATIONS PERFORMANCE TEST ===")
    ans = count_ways(100, [1, 5, 10, 25, 50])
    print(f"count_ways(100, [1, 5, 10, 25, 50]) = {ans}")
    print(f"Cache Performance -> Hits: {count_ways.hits()}, Misses: {count_ways.misses()}, Total Calls: {count_ways.calls()}")

    print("\n=== LRU CACHE INTERNALS DEMONSTRATION ===")
    @memoize(max_size=3)
    def identity(x):
        return x

    identity(1)  # Miss
    identity(2)  # Miss
    identity(3)  # Miss
    identity(1)  # Hit  -> Cache reordered to make 1 newest
    identity(4)  # Miss -> Cache full -> oldest key 2 is evicted because 1 was refreshed
    identity(5)  # Miss -> Cache full -> oldest key 3 is evicted

    old_misses = identity.misses()
    identity(1)  # 1 is still safely in cache
    if identity.misses() == old_misses:
        print("-> Success: Key '1' was protected from eviction due to LRU logic updates.")
    
    identity(2)  # 2 was previously evicted, should trigger a new miss
    if identity.misses() > old_misses:
        print("-> Success: Evicted key '2' correctly triggered a fresh miss calculation.")

    print("\n=== ALGORITHMIC ANALYSIS COMPLEXITY REPORT ===")
    header = f"{'Function Name':<28} | {'Time Complexity':<16} | {'Space Complexity':<16}"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    
    metrics = [
        ("count_ways (Naive)", "O(2^(N+M))", "O(N)"),
        ("count_ways (Memoized)", "O(N*M)", "O(N*M)"),
        ("count_ways (Iterative Bonus)", "O(N*M)", "O(N)"),
        ("fib_naive", "O(2^N)", "O(N)"),
        ("fib_memo", "O(N)", "O(N)"),
        ("longest_consecutive", "O(N)", "O(N)"),
        ("count_pairs", "O(N)", "O(N)"),
        ("memoize decorator", "O(1) overhead", "O(max_size)")
    ]
    for name, t_comp, s_comp in metrics:
        print(f"{name:<28} | {t_comp:<16} | {s_comp:<16}")
    print("-" * len(header))

if __name__ == "__main__":
    main()


# =====================================================================
# PART 5: WRITTEN ANALYSIS
# =====================================================================
#
# 1. Time Complexity of Naive vs Memoized Fibonacci:
#    - Naive fib(n) runs at O(2^N) because every function call branches out into two fresh sub-calls, 
#      forming an exponential execution tree.
#    - Memoized fib(n) runs at O(N) because it avoids repeating identical recalculations. 
#      Once fib(n-1) is evaluated, its complete sub-tree results are immediately retrieved from cache in O(1) time.
#
# 2. Why Memoizing longest_consecutive Gives Almost No Benefit:
#    - longest_consecutive already runs at optimal linear efficiency O(N) using an internal dictionary table lookup.
#    - Every element inside the array is examined at most twice. Because the function is non-recursive and 
#      internally handles all states sequentially, a memoization wrapper would only add extra lookup overhead 
#      without skipping any nested work loops.
#
# 3. Dictionary Lookup Performance (Average vs Worst Case):
#    - A dictionary lookup takes O(1) on average because it uses a hash function to transform keys into bucket matrix indexes, 
#      allowing immediate access to the exact memory address.
#    - It degrades to O(N) in worst-case scenarios where many different keys generate identical hash values (hash collisions).
#      This forces Python to loop linearly through a bucket list chain to find the matching key.
#
# 4. Situations Where Memoization Is Bad:
