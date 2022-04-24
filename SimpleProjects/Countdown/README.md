# Countdown  

The program Countdown will take hours, minutes and seconds as input and create a timer.  
The inputs need to be non-negative integers.  
The thing that makes this countdown unique is that inputs for minutes and seconds should normally in the range of 0 to 60 but when you use this program, you can provide any non-negative integer and it will work fine.  
The >60 numbers will treated in a way that when divided by 60, the remainders will be used to add the number of minutes or hours as appropriate.  

## An ordinary example  

```{python}
> python countdown.py  
Hello! Enter a label for your timer: Timer
Enter the hour for the timer: 0
Enter the minute for the timer: 0
Enter the second for the timer: 10
00:00:10
```

```{python}
> python countdown.py  
Hello! Enter a label for your timer: Timer
Enter the hour for the timer: 0
Enter the minute for the timer: 0
Enter the second for the timer: 10
Timer completed: Timer!
```

The above chunk is from the output when we execute the file. This can be considered an ordinary example as it will work as per everyone's expectations.  

## A special example  

```{python}
> python countdown.py  
Hello! Enter a label for your timer: Timer
Enter the hour for the timer: 1
Enter the minute for the timer: 78
Enter the second for the timer: 61
02:19:01
```

Above we see that we have provided some values for minutes and seconds which would normally be considered invalid.  
However, our program still manages to convert these values as per the range a timer would need and starts the countdown.  
We see that we have 61 seconds which is same as 1 minute and 1 second passing, as per the timer.  
We see that we got 78 minutes which implies 1 hour and 18+1 minutes have passed.  
Finally, we see we have 1 hour but as per the values, 2 hours will be considered.  

And in case this timer is too long, you can always click `Ctrl + C` to end the timer.  

```{python}
> python countdown.py  
Hello! Enter a label for your timer: Timer
Enter the hour for the timer: 1
Enter the minute for the timer: 78
Enter the second for the timer: 61
Timer Interrupted! Exiting!
```  

Hope you enjoy playing with the program.
