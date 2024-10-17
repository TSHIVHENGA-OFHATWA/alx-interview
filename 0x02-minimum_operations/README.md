Operations
Description
This project focuses on solving the "Minimum Operations" problem, where you need to determine the minimum number of operations required to get exactly n "H" characters in a text editor, starting with a single "H". The editor supports only two operations:

Copy All: Copies all characters present in the file.
Paste: Pastes the copied characters.
The goal is to calculate the fewest number of operations needed to result in exactly n "H" characters in the file.

If it is impossible to achieve exactly n characters, the function should return 0.

Prototype
python
Copy code
def minOperations(n)
Parameters:
n (int): The target number of "H" characters.
Returns:
An integer: The fewest number of operations needed to reach exactly n "H" characters. If n is impossible to achieve, return 0.
