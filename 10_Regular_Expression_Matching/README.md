# 10. Regular Expression Matching

>Hard

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

	* `'.'` Matches any single character.​​​​

	* `'*'` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).

**Example 1:**

>Input: s = &quot;aa&quot;, p = &quot;a&quot; \
>Output: false \
>Explanation: &quot;a&quot; does not match the entire string &quot;aa&quot;.

**Example 2:**

>Input: s = &quot;aa&quot;, p = &quot;a*&quot; \
>Output: true \
>Explanation: &#39;*&#39; means zero or more of the preceding element, &#39;a&#39;. Therefore, by repeating &#39;a&#39; once, it becomes &quot;aa&quot;.

**Example 3:**

>Input: s = &quot;ab&quot;, p = &quot;.*&quot; \
>Output: true \
>Explanation: &quot;.*&quot; means &quot;zero or more (*) of any character (.)&quot;.

**Constraints:**

* `1 <= s.length <= 20`
* `1 <= p.length <= 20`
* `s` contains only lowercase English letters.
* `p` contains only lowercase English letters, `'.'`, and `'*'`.
* It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.

[See the original page](https://leetcode.com/problems/regular-expression-matching/)

# My Answers:

## Answer 1

[See the Answer](ans.py)

## Answer 2

[See the Answer](ans2.py)
