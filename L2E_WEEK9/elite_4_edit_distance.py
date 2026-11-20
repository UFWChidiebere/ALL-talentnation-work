# Memoization decorator (no external libraries)
# Time: O(1) average per cache lookup; Space: O(states) to store computed results.
# Reasoning: Uses a dictionary in a closure to cache unique (i, j) arguments and count total wrapper calls.
def memoize(func):
    cache = {}

    def wrapper(*args):
        wrapper.calls += 1
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    wrapper.calls = 0
    return wrapper


# 1. Naive Recursion (No Caching)
# Time: O(3^(m + n)) where m = len(a) and n = len(b); Space: O(m + n) for recursion stack depth.
# Reasoning: Each mismatch branches into three recursive calls without caching overlapping subproblems.
def edit_naive(a: str, b: str) -> int:
    def helper(i, j):
        helper.calls += 1
        if i == 0:
            return j
        if j == 0:
            return i

        if a[i - 1] == b[j - 1]:
            return helper(i - 1, j - 1)

        insert_cost = helper(i, j - 1)
        delete_cost = helper(i - 1, j)
        replace_cost = helper(i - 1, j - 1)
        return 1 + min(insert_cost, delete_cost, replace_cost)

    helper.calls = 0
    ans = helper(len(a), len(b))
    edit_naive.last_calls = helper.calls
    return ans


edit_naive.last_calls = 0


# 2. Memoized Recursion (Using @memoize)
# Time: O(m * n) where m = len(a) and n = len(b); Space: O(m * n) for the cache dictionary and stack.
# Reasoning: There are at most (m + 1) * (n + 1) unique (i, j) pairs, and each is computed once.
def edit_memo(a: str, b: str) -> int:
    @memoize
    def helper(i, j):
        if i == 0:
            return j
        if j == 0:
            return i

        if a[i - 1] == b[j - 1]:
            return helper(i - 1, j - 1)

        insert_cost = helper(i, j - 1)
        delete_cost = helper(i - 1, j)
        replace_cost = helper(i - 1, j - 1)
        return 1 + min(insert_cost, delete_cost, replace_cost)

    ans = helper(len(a), len(b))
    edit_memo.last_calls = helper.calls
    return ans


edit_memo.last_calls = 0


# 3. Bottom-Up 2D Table
# Time: O(m * n) where m = len(a) and n = len(b); Space: O(m * n) for the (m + 1) x (n + 1) grid.
# Reasoning: Nested loops fill every cell in an (m + 1) by (n + 1) table with O(1) work per cell.
def edit_table(a: str, b: str) -> int:
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i  # Fixed: set column 0
    for j in range(n + 1):
        dp[0][j] = j  # Fixed: set row 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j],      # Delete
                    dp[i - 1][j - 1]   # Replace
                )

    edit_table.last_cells = (m + 1) * (n + 1)
    return dp[m][n]


edit_table.last_cells = 0


# Hard Bonus: Space-Optimized Bottom-Up (Two Rows Only)
# Time: O(m * n) where m = len(a) and n = len(b); Space: O(n) using only two 1D lists of size n + 1.
# Reasoning: Computing row i only reads row i - 1 and row i, allowing us to discard older rows after each step.
def edit_table_two_rows(a: str, b: str) -> int:
    m, n = len(a), len(b)
    prev = list(range(n + 1))

    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        curr[0] = i
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(
                    curr[j - 1],   # Insert
                    prev[j],       # Delete
                    prev[j - 1]    # Replace
                )
        prev = curr

    return prev[n]


# Helper to format ASCII table using pure string logic
# Time: O(rows * cols), Space: O(rows * cols)
# Reasoning: Measures max column widths across all rows and pads each cell with spaces using string concatenation.
def format_table(headers: list, rows: list) -> str:
    widths = [len(h) for h in headers]
    for row in rows:
        for idx, cell in enumerate(row):
            if len(str(cell)) > widths[idx]:
                widths[idx] = len(str(cell))

    def build_row(items):
        parts = []
        for idx, item in enumerate(items):
            text = str(item)
            parts.append(" " + text + " " * (widths[idx] - len(text) + 1))
        return "|".join(parts)

    sep = "+".join("-" * (w + 2) for w in widths)
    lines = [build_row(headers), sep]
    for row in rows:
        lines.append(build_row(row))
    return "\n".join(lines)


# --- Written Analysis (Required Comments) ---
#
# 1. Time complexity of the naive version and why it blows up:
#    O(3^(m + n)). Every mismatch branches into 3 recursive calls (insert, delete, replace),
#    recomputing the exact same (i, j) subproblems exponentially many times across different branches.
#
# 2. Time and space complexity of memoized vs. bottom-up versions:
#    - Memoized: O(m * n) time and O(m * n) space (stores up to (m + 1)(n + 1) cached states plus call stack).
#    - Bottom-up table: O(m * n) time and O(m * n) space (fills an (m + 1) x (n + 1) grid iteratively).
#
# 3. For two strings of length 5000, which version would you use and why?
#    Use the bottom-up version (specifically the two-row O(n) space variant).
#    Memoized recursion reaches a call depth of m + n = 10,000, crashing Python's ~1,000-frame recursion limit,
#    while a full 5001 x 5001 table uses ~25 million cells (~200 MB) compared to just two 5,001-item lists (~80 KB).
#
# 4. Which single previous row does each step actually need, and how does that change space complexity?
#    Row i only ever reads from row i - 1 (the immediately preceding row) and row i itself.
#    Dropping all rows before i - 1 reduces space complexity from O(m * n) down to O(n).


# --- Main Section (Testing & Measurement) ---
if __name__ == "__main__":
    # 1. Verify all versions agree on prompt examples
    examples = [
        ("kitten", "sitting"),  # 3
        ("", "abc"),            # 3
        ("same", "same"),       # 0
        ("flaw", "lawn"),       # 2
    ]
    print("--- Prompt Examples ---")
    for s1, s2 in examples:
        r1 = edit_naive(s1, s2)
        r2 = edit_memo(s1, s2)
        r3 = edit_table(s1, s2)
        r4 = edit_table_two_rows(s1, s2)
        assert r1 == r2 == r3 == r4
        print(f"'{s1}' -> '{s2}': {r1}")

    # 2. Side-by-side call count comparison ("kitten" vs "sitting" + two longer pairs up to 8 letters)
    print("\n--- Call Count Comparison ---")
    pairs = [
        ("kitten", "sitting"),
        ("distance", "editing"),
        ("sunday", "saturday"),
    ]
    for s1, s2 in pairs:
        dist = edit_naive(s1, s2)
        c_naive = edit_naive.last_calls
        edit_memo(s1, s2)
        c_memo = edit_memo.last_calls
        print(f"'{s1}' vs '{s2}' (dist={dist}) -> Naive calls: {c_naive:,} | Memo calls: {c_memo:,}")

    # 3. Formatted Comparison Table for two custom pairs
    print("\n--- Complexity & Work Table ---")
    headers = ["function", "result", "calls / cells", "time complexity", "space complexity"]
    custom_pairs = [("park", "spake"), ("dynamic", "program")]
    for s1, s2 in custom_pairs:
        print(f"\nPair: '{s1}' -> '{s2}'")
        r_n = edit_naive(s1, s2)
        c_n = f"{edit_naive.last_calls} calls"
        r_m = edit_memo(s1, s2)
        c_m = f"{edit_memo.last_calls} calls"
        r_t = edit_table(s1, s2)
        c_t = f"{edit_table.last_cells} cells"

        rows = [
            ["edit_naive", r_n, c_n, "O(3^(m+n))", "O(m+n)"],
            ["edit_memo", r_m, c_m, "O(m*n)", "O(m*n)"],
            ["edit_table", r_t, c_t, "O(m*n)", "O(m*n)"],
        ]
        print(format_table(headers, rows))

    # 4. Hard Bonus Proof: Two-row version vs Full Table on 5+ pairs
    print("\n--- Hard Bonus Proof (5 Pairs) ---")
    bonus_pairs = [
        ("kitten", "sitting"),
        ("algorithm", "altruistic"),
        ("", ""),
        ("abcdef", "azced"),
        ("intention", "execution"),
    ]
    for s1, s2 in bonus_pairs:
        full_res = edit_table(s1, s2)
        two_row_res = edit_table_two_rows(s1, s2)
        assert full_res == two_row_res
        print(f"'{s1}' -> '{s2}': full={full_res}, two_rows={two_row_res} (OK)")
