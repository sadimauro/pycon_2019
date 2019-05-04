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
** give people money and equipmne tthat can help them get a job.
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


