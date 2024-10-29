# GA2-CS325
Second group assignment

After the successful program you organized for a previous library book release event, you have gained a reputation for your high-quality event management skills. As a result, another library has approached you to organize their upcoming event.

This time, they plan to conduct the book release event over a long weekend, spanning three days. There are n registered clubs, with sizes c1, c2, . . . , cn. The library only allows clubs with a size of at most ` to register, meaning that for all 1 ≤ i ≤ n, ci ≤ `. Unlike before, the order in which clubs are registered does not need to be maintained, meaning clubs can be reordered. The objective is to ﬁnd the minimum number of people that need to be admitted per day to accommodate all clubs over the three days. Speciﬁcally, we need to answer the following problem:

• Design an algorithm to compute the minimum admittance per day to ﬁnish the book release event in three days. Any algorithm with polynomial time in n and ` will receive full credit for the report part. For the implementation, test cases will be designed such that any algorithm with O(`2n3) time complexity (with a reasonable hidden constant factor) can pass them.

Report (60%). In your report, include the description of your algorithms, running time analysis, and proof of correctness. Algorithms should be explained in plain english. You can use pseudocode if it helps your explanation, but the grader will not try to understand complicated pseudocode.

Code (40%). Submit a python program that computes the minimum attendance per day to ﬁnish the event in three days. Your program will be tested against several test cases, for correctness and eﬃciency. For each test case, the program will be automatically stopped after 30 seconds if it is not done in that time. In this case, the group will miss the points of that test case. Note: it is important that your output is formatted as described below, since your codes will be tested automatically. Speciﬁcally, you must implement the function “min attendance for long weekend” in the following code. The code you submit will be an implementation of this procedure in a ﬁle named “assignment2.py”.
