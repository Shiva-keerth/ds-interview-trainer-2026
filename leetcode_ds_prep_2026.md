# 2026 Data Science LeetCode Preparation Guide

For Data Science roles, coding interviews primarily test your ability to **manipulate data, handle strings, use Hash Maps (dictionaries), and write flawless SQL/Pandas.**

---

## Phase 1: The Non-Negotiable Core (SQL & Pandas)
Before touching complex algorithms, your SQL and Pandas skills must be bulletproof. Most companies will start a DS interview loop here.

### LeetCode SQL (Aim for Medium difficulty)
*   **[175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)** (Easy)
*   **[184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/)** (Medium) - *Tests Window Functions/Joins*
*   **[185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/)** (Hard) - *Tests Dense Rank, very common*
*   **[196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/)** (Easy)
*   **[262. Trips and Users](https://leetcode.com/problems/trips-and-users/)** (Hard) - *Excellent for aggregation and conditional logic*
*   **[1179. Reformat Department Data](https://leetcode.com/problems/reformat-department-data/)** (Easy) - *Tests pivoting data*

### LeetCode Pandas (Highly Relevant for Python Interviews)
LeetCode recently added a Pandas section. Do **all** of them (there are around 15-20 core ones). They perfectly mimic what you will do on the job.
*   **[2877. Create a DataFrame from List](https://leetcode.com/problems/create-a-dataframe-from-list/)** (Easy)
*   **[2882. Drop Duplicate Rows](https://leetcode.com/problems/drop-duplicate-rows/)** (Easy)
*   **[2888. Reshape Data: Concatenate](https://leetcode.com/problems/reshape-data-concatenate/)** (Easy)
*   **[2890. Reshape Data: Melt](https://leetcode.com/problems/reshape-data-melt/)** (Easy)

---

## Phase 2: Python Data Structures (The "Coding Round")
When they ask you to open a Python editor, they usually test Arrays, Strings, and Hash Maps. They want to see if you can write efficient Python code (O(n) time complexity).

### 1. Hash Maps / Dictionaries (The most important DS data structure)
*   **[1. Two Sum](https://leetcode.com/problems/two-sum/)** (Easy) - *Understand why a Hash Map makes this O(n)*
*   **[49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)** (Medium)
*   **[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)** (Medium) - *Extremely common DS question*
*   **[560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)** (Medium)

### 2. Arrays & Matrices (Simulating image data or time series)
*   **[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)** (Easy)
*   **[238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)** (Medium)
*   **[56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)** (Medium) - *Great for time-series overlap problems*
*   **[73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)** (Medium)

### 3. String Manipulation (Essential for NLP basics)
*   **[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)** (Medium)
*   **[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)** (Easy) - *Tests Stack usage*
*   **[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)** (Easy) - *Data cleaning simulation*

---

## Phase 3: Math, Stats, and Logic
Data Scientists are often given problems that test basic probability or mathematical logic rather than pure algorithmic trickery.

*   **[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)** (Easy) - *Basic intro to dynamic programming/Fibonacci*
*   **[136. Single Number](https://leetcode.com/problems/single-number/)** (Easy) - *Bit manipulation/Logic*
*   **[204. Count Primes](https://leetcode.com/problems/count-primes/)** (Medium)
*   **[384. Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/)** (Medium) - *Can you code randomness properly?*
*   **[470. Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/)** (Medium) - *A classic probability interview question.*

---

## Strategy for 2026:
1. **Don't memorize, internalize:** If you solve a problem, make sure you can explain the Time and Space Complexity (Big O notation) out loud.
2. **Ignore the extremely obscure:** Unless you are applying for a specialized MLE role, skip Hard-level DP and Graph algorithms. Focus on Mediums.
3. **Use Python's built-ins:** Learn to use `collections.Counter`, `itertools`, and list comprehensions to write clean, Pythonic code.
