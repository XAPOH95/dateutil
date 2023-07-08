# pyperiodutils
Small experimental python package for handling month representation

Solves next problems:
1. Month representation:
<pre>
  november = Month(11)
  november.Eng() # nov
  november.Eng().capitalize() # Nov
  november.EngFull() # november
  november.M() # M11
</pre>
3. Months comparison:
<pre>
jan = Month(1)
march = Month("march")
march > jan # True
</pre>
3. Months shifting:
<pre>
January = Month("Jan")
april = January + 3  
</pre>
