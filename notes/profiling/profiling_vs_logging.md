# Profiling vs Logging

Profiling is typically used offline during development, we can also use 
it in production to find performance bottlenecks, with a new generation of 
continuous profiling tools.

Trace-based logging and profiling give us different information. Once our 
software is complex enough, it is good to use both.




Statistical profiling takes a sample of your program’s running code at intervals, and tells you what the program is doing at that particular time. Basically, it runs a loop like this:

    Sleep for a bit.
    Record what the program is doing at this moment in time.
    Go to step 1.

Whatever code is running slowly is more likely to be sampled, and therefore more likely to show up in the final trace.

With a profiler, we can find our example’s performance bottlenecks without changing the code at all

In real software, the input may be buried deep in an input file, an HTTP response, or the result of some other calculation, any of which won’t show up in the profiling report; profiling is typically focused on functions, not on inputs or variables. To understand the impact of inputs on performance, we need to turn to logging, and ideally tracing.

Logging gives us a different set of information than profiling: in particular, we can log function arguments, results, variables, and other runtime information. And the timestamps of log messages can be used to determine how long some code ran.

Like regular logging, trace-based logging or tracing can also be used to identify which parts of your code are slow. But tracing is much better at getting you this information than normal logging.

-Instead of isolated statements of fact—”something happened!”, “something else happened!”—tracing records spans or actions that have a beginning and an end.
-Spans build up a tree: they can contain other spans, and can be tracked across threads or processes, even across multiple computers. You can imagine tracing a request from the browser, to the web server, to the backend service, and finally to the database, and then all the way back.

The fact that traces have a beginning and an end is one reason why tracing is better than normal logging: the elapsed time of spans automatically gives you the run time for the relevant code.

## Comparison

    Profiling: Just run your program under a profiler, that’s it.
    Tracing: You need to instrument every function and code block that you want to end up in the logs.


    Profiling: Yes, they’re no different than functions in your code; everything relevant gets recorded.
    Tracing: The need for manual instrumentation means getting information about third-party can be tricky, especially for internal details and in less dynamic languages.


    Profiling: Any function that runs long enough will get recorded, but because of the use of sampling, functions that run quickly and infrequently will not show up in the profiling report.
    Tracing: All functions calls can be recorded… so long as you’ve instrumented them. In practice, once you scale up (e.g. large web applications) sampling is also used, because otherwise the data is overwhelming.

    Profiling: No.
    Tracing: Yes, if you chose to record them.

In short, you want both tracing and profiling in your production environment: they give you different information, sometimes complementary, sometimes useful all on its own.


https://pythonspeed.com/articles/logging-vs-profiling/