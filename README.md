# Description of LCuS
This is our working repository as we research ways to speed up the LCuS
algorithm, using strategies from Kosowski's 2004 paper. Our naive implementation
can be found at https://github.com/robynburger/LCuS_Naive

LCuS.py is an optimized O(n^4) approach to solving the longest cubic subsequence 
(LCuS) problem. 

For a string of characters, LCuS.py identifies the longest subsequence repeated 
three distinct times. It finds the optimal breakpoints to seperate the string 
into three consecutive substrings, each containing an interation of the 
subsequence. It then returns these indices and three matrices, F, D, and E. 

* Description of F
* Description of D
* Description of E

For more information, see paper (* citation)

## Requirements

1. Install python 3.12 or higher
<!-- 2. Use Conda or other similar environment to run NumPy package:
(https://www.numpy.org) -->

## Running LCuS

LCuS is still experimental and is not yet functional. As such, you cannot run 
it yet. 
<!-- Clone the repository: 
```
$ git clone https://github.com/robynburger/LCS_naieve
```

Run LCuS.py:
```
$ python LCuS.py
```

Enter command line arguments:
```
Enter string:

Use ideal parameters? (Yes/No):
```
If user types 'Yes:
``` 
Your file was saved: results/s/ideal.txt
```
If user types 'No':
```
Enter positive integers j, l, m:

Note: 1 <= i < j <= k < l <= m <= {len(s)}.

j:

l:

m:

Your file was saved: results/s/j_l_m.txt
``` -->

## Authors and Acknowledgements 

Written by Robyn Burger and Allison Shi under the mentorship of 
Dr. Brendan Mumey and Dr. Adiesha Liyanage. 

Funded by the National Science Foundation (NSF) as part of research conducted 
at Montana State University for the summer 2024 Algorithms REU. 

Adapated from longest tandem subsequence problem:   

Kosowski, Adrian., An Efficient Algorithm for the Longest Tandem
Scattered Subsequence Problem,  Lecture Notes in Computer Science, volume 3246 
(2004) 93-100.
