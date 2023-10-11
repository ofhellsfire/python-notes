# Profiling

There are several types of profiling, the most common ones are:

1. Deterministic profiling
2. Sampling profiling

Deterministic profilers execute trace functions at various points of interest 
(e.g. function call, function return) and record precise timings of these events. 
Typically this requires source code instrumentation but it can be automated.

Instead of tracking every event (e.g. call to every function), statistical profilers interrupt application periodically and collect samples of the execution state (call stack snapshots). The call stacks are then analysed to determine execution time of different parts of the application. TODO