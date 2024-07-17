## Minimum Operations

This projects employs algorithmic and mathematical concepts to devise a solution that efficiently calculates the minimum number of operations to achieve a given number of characters using only “Copy All” and “Paste” operations.

Assumption
--
In a text file, there is a single character H. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` H characters in the file.

- Prototype:
```py
def minOperations(n)
```
* Returns an integer
* If n is impossible to achieve, return 0

Example:
--

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

---

Run the `0-main.py` script:

```cmd
$ ./0-main.py 
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
```
