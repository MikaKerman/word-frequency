# Backend Software Engineer Home Assignment
Howdy, dear interviewee!
This task examines your back-end skills. It doesn’t require any prior or domain-specific knowledge. Just be yourself and deliver the best solution
in the allocated time.

Please create a service in the language you’re most comfortable with that provide 2 endpoints (doesn’t have to be HTTP):
1. First endpoint receives a string of comma-separated words, stores them in service’s internal state. It can return ack in any suitable form
(for example, if it’s **HTTP** endpoint - it should return 200 OK response with no payload). If ack is not needed - leave it as is (for example,
you can continuously send strings over **websocket**).
* Sample input

```text
ball,eggs,pool,wild,daily
```

2. Second endpoint only returns the 5 most recurring words with their frequency distribution rank (from 5 to 1). It does require any
payload to be sent.
* Distribution rank is calculated for any word by this formula:


```
round(4 * (currentWordCount - leastOccurringWordCount) / (mostOccurringWordCount - leastOccurringWordCount)) + 1
``` 

* Example:
When the dateset is `ball ball ball ball eggs eggs pool pool wild daily`
The result would be:

```text
ball 5
eggs 2
pool 2
wild 1
daily 1
```

Lets check some not obvious word as an example:
* eggs count = 2
* Best word - ball = 4
* Worst word wild | daily = 1
* For eggs : rank = round(4*(2-1)/(5-1))+1 = round(4*0.25)+1 = round(1)+1 = 2

### Task notes:
* Do not use any external resources. Store data in memory.
* Allow concurrency and expect a lot of traffic. Note that sending words to the server seems to happen much more then getting the
histogram
* Write code as you write for production and you think people will enjoy maintain it
* Try to think about edge cases a bit!
* It doesn’t have to be extensible, but it is expected that you provide an optimal solution logically
 
Good luck,
We believe in you :)
