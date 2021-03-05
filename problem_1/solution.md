# Problem description

Provide some Python code that can be used to measure how long some code took to run in a
friendly format. The amount of time can range from less than a second to several hours and
should be easy for a human to read (for example “193048.231s” is not a good output).

**Answer:** the [humanized_time_measure.py](humanized_time_measure.py) file has the function that solves the problem.

It basically slices the given seconds number in bunches of each time boundary (seconds, minutes, hours, weeks, and months) and formats the output for a human-readable string.
