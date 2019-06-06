Lightning Talks
===============

...lost my notes...


Keynote - Sha
=============

Open-source access, inclusion is *love*.


Keynote - Jessia McKellar
=========================

Speaker:  Python person, plus Founder/CTO pilot.

The criminal justice is horrible, hella racist, wildly ineffective.  What can we do to help as programmers?

Opportunities:
* as individuals:
** give people money and equipment that can help them get a job.
** establish and support programs at prisons to help people better themselves, e.g. to build a career.
** get political about prisons.  [Know your DA](meetyourda.org).
* as technologists:
** tech-focused job training, inside and outside prisons.  e.g. "last mile" program/website.
** bootcamps
** tech support for local reform orgs
* as employers:
** hire people with records - background checks, entry-level roles, active outreach


Floats are Friends
==================

Speaker: David Wolever

Whole numbers.  Easy.  `INT_MIN, _MAX, LONG_MIN, _MAX`.

We could fix whole and fractional part memory (e.g. 32 bits for whole portion, 32 bits for fractional part), but that will limit how many different numbers we can store.

Instead, we can store a slcaing factor, e.g. 7.5. + scale=12 would store 7.5 billion.  That scale is the 'floating' point.

Storage internally:  bit for sign; bits for exponent; bits for fraction (also 'mantissa').
Essentially, this is base-2 scientific notation.
e.g. 0.5 is 0 100 0001.  0 means +; 100 is 4 and exponent is then `2**(3-4)` (3 is the 'scaling factor').

Tradeoff: precision vs magnitude.

```python
>>> 1e20 + 1 == 1e20
True
```
Wha???
```python
>>> 12345 + 1e15
>>> 12345 + 1e16
>>> 12345 + 1e17
```

sum vs math.fsum vs np.sum.

Every real number can't be represented (e.g. irrationals).
e.g. 0.1.  The best we can do is 0.100000005.

.: So, every flaot operation introduces some error.  Nothing you can do about this.  Always round your results to the appropriate number of decimal places.  Also, see numpy.isclose().

The weird parts:
```python
inf = float('inf')
inf + inf
inf > 10e33
inf / inf
nan = float('nan')
nan == nan # False!?!
1 > nan
1 + nan
nan in [nan]
```

There are `2**52` nans.!?

The `decimal` module provides support for floats.
* nearest number rounding will be more sensible.
* default precision is greater
* exact representation:
```python
from decimal import Decimal
d = Decimal('0.2')
d + d + d + d + d
1.0
```


PEP 572: The Walrus Operator
============================

Subtitle: what's new in Python 3.7

Speaker: Dustin Ingram

First, a note on governance.  Guido was BDFL.  Now, PEP - Python Enhancement Proposal.  Like a constitutional amendment.  Well known ones:
* PEP 8 = style guide for Python code.
* PEP 20 = the Zen of Python
There are now BDFL delegates, so that others can make decisions on behalf of Guido.

PEP 572 = assignment expressions.  DRAMA!

`:=`.  Let's call this the walrus operator.
Examples:
```python
# option 1
foo = [f(x), f(x)**2, f(x)**3]

# option 2
y = f(x)
foo = [y, y**2, y**3]

# .:Simple (one line), but only calling expensive f() once
foo = [y := f(x), y**2, y**3]
```

Another example:
```python
chunk = file.read(8192)
while chunk:
    process(chunk)
    chunk = file.read(8192)

# instead
while chunk := file.read(8192):
    process(chunk)
```

You cannot use `:=` in the same way as `=`.

Reception of PEP 572:  it won't be backwards compatible!  What do we call it, so that we can teach it? (it's officially called the named expression operator, I think)  I hate it!

Guido (GEE-do) said "he had to stop reading the threads so that he wouldn't go insane".  He approved PEP 572 and then Guido removed himself as BDFL.  Sad.  Dictators are people too.

Result:  PEP 8000 - governance overview process., 8001 - voting, 8002 - open source governance survey
Approved:  PEP 8016.  Steering Council.  See keynote tomorrow.

Walrus is in 3.8.  If you don't like it, don't use it.

Is Guido coming back?  He's still here, but not as BDFL.


Statisical Profiling (and other fun with the sys module)
========================================================

Speaker: Emin Martinian

Why statistical profiling? - stats on how often and how long various parts of the program executed.

cProfile is a *deterministic* profiler.
```python
import cProfile
cProfile.run(cmd)
```
Awesome, but slow.  Usually can't profile in production.  Also note that deterministic is not thread-aware.

Alternative:  statistical profiler.  Records a "sample" of what is running at various times, i.e. waking up occasionally to see what's running.
Implement your own with e.g. `stat_prof`, `plop`, `pyflame` (all POSIX); `ox_profile`, `pprofile` (Windows)


Exceptional Exceptions - How to properly raise, handle and create them
======================================================================

Speaker: Mario Corchero

```python
# exc_info = True includes stack trace in log
logging.error("an error occurred", exc_info=True)
```

`logging.exception()`?

Use `repr()` instead of `str()` when printing exceptions, so give you more info.

KeyboardInterrupt, SystemExit, Exception are subclasses of the base class BaseException.  Lots other exceptions are subclasses of Exception.
Don't inherit from BaseException.  Only from Exception.

.:Be mindful about catching and raising exceptions.


Getting Started with Deep Learning
==================================

Using numpy and keras on voice data.

Data is larnyx vibrations.  Trying to predict if the person has vocal trauma.

More on deep learning...
numpy - mostly for hold/manipulate array data
keras - python wrapper around theano, pytorch, tensorflow

A *perceptron* is like a neuron, in that there are multiple inputs with various weights, and those go into some function, and then some output comes out.

Neural network:  observable known input(s) and output; maybe hidden intermediate steps (in this case, the network is "deep").

Types:
* Convolutional NN: lots and lots of inputs, pulled down to maybe an average of them, and then generates one of a few outputs. Usually for classification.
* Recurrent NN: intermediate steps "remember" also what happened in the prior step
* Long-term short-term memory (LSTM) (?)

Issues:
* running out of memory.  Solution - batch data and analyze batch by batch
* struggling to write to disk (with pickle).  Solution - h5py to grab/store portions at a time.
* managing long running process.  Solution - tmux!
* not analyzing your errors.  Solution - understand the algorithm and its results.

"kaggle" to get data (?), "neural network zoo" to understand the suite of learning algorithms.


Lightning Talks
===============

Qt for simple gui development

Wear your badge up high so people can see your name.

FairOSS is trying to establish 'certifications' for businesses so that you know that they're using OS software fairly (funding it, giving back to it, etc.)




