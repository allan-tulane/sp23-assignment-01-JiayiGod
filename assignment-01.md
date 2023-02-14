

# CMPS 2200 Assignment 1

**Name:**________Jiayi Xu_________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  No, because $\lim _{n\to \infty \:}\left(\frac{2^{n+1}}{2^n}\right)=2>0$. By limit method, we know that if the limit is equal to zero, it is true. But it is not equal to zero, thus the statement is false.
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No, because $\lim _{n\to \infty \:}\left(\frac{2^{2^n}}{2^n}\right)=\infty$. Thus it is false by limit method.
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  No, because $\lim _{n\to \infty \:}\left(\frac{n^{1.01}}{\mathrm{log}^2 n}\right)=\infty$. Thus it is false by limit method.
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes, because $\lim _{n\to \infty \:}\left(\frac{n^{1.01}}{\mathrm{log}^2 n}\right)=\infty$. Thus it is true by limit method.
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No, because $\lim _{n\to \infty \:}\left(\frac{\sqrt{n}}{(\mathrm{log} n)^3}\right)=\infty$. So it is false by limit method. 
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes, because $\lim _{n\to \infty \:}\left(\frac{\sqrt{n}}{(\mathrm{log} n)^3}\right)=\infty$. So it is true by limit method.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  This function define a sequence with domain(inputs) of all positive integers. `S(0)=0`, `S(1)=1` are initialized(base case), and the later outputs are equal to the sum of previous two numbers such that `S(n)=S(n-1)+S(n-2)`(recursive case). 
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  The work and span are both `O(n)`.
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
. Span is `O(n)`, work is `O(n)`
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  Work is still `O(n)` as the total work would not change. Span is now improved to `O(logn)`, as the depth of tree is `logn`
.  
.  
.  
.  
.  
.  
.  

