__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 6, Exercise 1

**Rate monotonic scheduling (RMS)** is an algorithm for assigning thread priorities in preemptive, hard, real-time applications where threads execute periodically. RMS assigns the highest priority to the thread with the shortest execution period, the next-highest priority to the thread with the next-shortest execution period, and so on. An RMS system is schedulable, meaning all tasks are guaranteed to meet their deadlines (assuming that no inter-thread interactions or other activities such as interrupts cause processing delays) if the following condition is met:

$$\sum_{k=1}^n \frac{C_i}{T_i} \leq n(n^{1/n}-1) $$

This formula represents the maximum fraction of available processing time that $n$ threads can consume. In this formula, $C_i$ is the maximum execution time required for thread $i$, and $T_i$ is the execution period of thread $i$.

Is the following system composed of three threads schedulable?

Thread | Execution time ($C_i$), ms | Execution period ($T_i$), ms
------ | ------------------------ | --------------------------
Thread 1 | 50 | 100
Thread 2 | 100 | 500
Thread 3 | 120 | 1000

# Answer
First, evaluate the left side of the RMS formula using the data from the table:

$$\frac{50}{100} + \frac{100}{500} + \frac{120}{1000} = 0.82$$

Then evaluate the right side of the RMS formula:

$$3(2^{1/3}-1) = 0.7798$$

Because $0.82$ is not less than or equal to $0.7798$, **this set of tasks is not schedulable under RMS**.