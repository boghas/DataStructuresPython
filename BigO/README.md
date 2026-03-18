# Big O

**Big O** notation is a mathematical tool used in computer science to analyze an algorithm's efficiency, describing how runtime or space requirements grow as the input size (n) increases.

There are **three greek letters** you'll meet when dealing with time & space complexity.

* Omega: This is the best scenario for running a piece of code.
* Theta: Average case for running a piece of code.
* Omicron (Big O): The worst case for running a piece of code.

## Example

L = [1, 2, 3, 4, 5, 6, 7]

1. Iterating the list and retrieving the first item in the list, will be **the best case scenario** and will be represented by **Omega**.

2. Iterating the list and retrieving the last item from the list, will be the **worst case scenario** and will be represented by **Omicron - O**.

3. Iterating and finding any other element, like, for example 4, will represent the **average case scenario** and will be represented by **Theta**.

## O(n)

Also called **Poportional**.

It basically means that an algorithm will have to perform an ***n* number of operations** to reach the solution.

![](/resources/big_O_graph.jpg)

! O(n) **is always** going to be **a straight line** - it is what is called **proportional**.

! If you here the term **proportional** in Big O, that will be a reference to **O(n)**.

## O(n^2)

Also called a **Loop within a Loop**.

It represents an algorithm that will take **n * n (n squared) or n^2** numbers of operations.

### Example

```
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)
```

![](/resources/O(n_squared)_compared_to_O(n).png)

## O(1)

Also called **constant time** because as **n** grows in size, the number of operations will remain constant.

This is the ideal time complexity.

### Example

```
def add_items(n):
    return n + n
```

![](/resources/O(1)_comparison.png)

## O(log n)

Also called **Divide and Conquer**.

It basically means that an algorithm will reach the solution by repeatedly **reducing the problem size by a constant factor** (commonly by half) at each step. Instead of checking every element, the algorithm eliminates large portions of the input each time, so the number of operations grows **logarithmically with *n***. This makes `O(log n)` algorithms very efficient for large inputs, since the number of steps increseas *very slowly even as n becomes much bigger*.

![](/resources/O(logn)_comparison.png)

## O(nlog n)

It means that an algorithm performs `n` **operations, each taking logarithmic time** (`log n`). In other words, the algorithm processes all *n* elements, and during that process it repeatedly performs steps that reduce the problem size logaritmically. As a result, the total number of operations grows proportionally to `n * log n`, which is more than linear time but still significantly more efficient than quadratic time for large inputs.

It is very common with sorting algorithms and it's **the most efficient way you can make a sorting algorithm**.

![](/resources/O(nlog%20n)_comparison.png)

## Simplifying Big O notation

### Drop constants

This is a trick to simplify the Big O notation. For example, for cases where we might have O(x * n) complexity, we will just drop the constants and use O(n).

#### Example

```
def print_items(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

print_items(10)
```

This block of code will print the numbers from 1 to 9 two times, so the complexity is O(2n), but to simplify the notation, we will use **O(n)**.

### Drop Non-Dominants

To simplify even further the Big O notation, we will only keep the dominants.

#### Example

```
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    
    for i in range(n):
        print(i)

print_items(10)
```

The complexity of this function will be O(n^2 + n). But, as we **n keeps growing in size, the O(n) will represent only a small percentage of O(n^2)**, therefore, we will **only keep the dominant part: O(n^2)**.

## Different Terms for Inputs

### Example

What is the time complexity of the code below:

```
def print_items(a, b):
    for i in range(a):
        print(i)
    
    for j in range(b):
        print(j)
```

The complexity will be `O(a + b)`.

```
def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)
```

The complexity will be `O(a * b)`.
