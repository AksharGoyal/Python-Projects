# Minesweeper  

The program was originally made by [Kylie Ying](https://www.youtube.com/watch?v=8ext9G7xspg).  

Working on this program helped me strenghten my concept about objects and classes. It is based on popular games minesweeper. Below ouput is an example when the program is executed.  

```
   0  1  2  3  4  
-------------------
0 |  |  |  |  |  |
1 |  |  |  |  |  |
2 |  |  |  |  |  |
3 |  |  |  |  |  |
4 |  |  |  |  |  |
-------------------
Where would you like to dig? Input as row,col: 0,5
Invalid location. Try again.
   0  1  2  3  4
-------------------
0 |  |  |  |  |  |
1 |  |  |  |  |  |
2 |  |  |  |  |  |
3 |  |  |  |  |  |
4 |  |  |  |  |  |
-------------------
Where would you like to dig? Input as row,col: 0,4
   0  1  2  3  4  
-------------------
0 |  |  |  |  |1 |
1 |  |  |  |  |  |
2 |  |  |  |  |  |
3 |  |  |  |  |  |
4 |  |  |  |  |  |
-------------------
Where would you like to dig? Input as row,col: 0,3
   0  1  2  3  4  
-------------------
0 |  |  |  |2 |1 |
1 |  |  |  |  |  |
2 |  |  |  |  |  |
3 |  |  |  |  |  |
4 |  |  |  |  |  |
-------------------
Where would you like to dig? Input as row,col: 1,3
SORRY GAME OVER :(
   0  1  2  3  4
-------------------
0 |X |X |4 |2 |1 |
1 |3 |X |X |X |2 |
2 |1 |3 |X |5 |X |
3 |0 |1 |2 |X |2 |
4 |0 |0 |1 |1 |1 |
-------------------
```

We observe that numbers on the board help us determine number of bombs are there around us and can be used to decide where to dig for gold carefully. Hope you enjoy playing this 😄
