# Python-Mini-Projects
# New Concepts I Learnt Form This Projects:
#  PROJECT2 : NUMBER_GUSSER
## random — Generate pseudo-random numbers
- This module implements pseudo-random number generators for various distributions.For integers, there is uniform selection from a range. 
- For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.
- The functions supplied by this module are actually bound methods of a hidden instance of the random.Random class. You can instantiate your own instances of Random to get generators that don’t share state.
- The random module also provides the SystemRandom class which uses the system function os.urandom() to generate random numbers from sources provided by the operating system.

```
random.randrange(start, stop[, step])
```
- Return a randomly selected element from range(start, stop, step).
```
random.randint(a, b)
```
- Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
