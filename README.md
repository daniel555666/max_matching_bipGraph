# Max Matching in Biparatite Graph
## By Yakov Khodorkovski , Daniel Zaken and Aviad Gilboa 
The Hungarian maximum matching algorithm, is an algorithm that can be used to find maximum matchings in bipartite graphs. 
![gif_hung](https://user-images.githubusercontent.com/66936716/171358041-bee96a16-efaa-489b-872b-3b9c4392e219.gif)

## Installation

First clone the project to your directory 

install the necessary libraries 

```bash
pip install networkx
```
```bash
pip install matplotlib
```
```bash
pip install tk
```

then run the program using the command line : 
```bash
python3 hungarian_method.py 
```

## How to add vertices and the edges

add the vertices and the edges, divide them with spaces , for example : 

![image](https://user-images.githubusercontent.com/66936716/171355326-020182f4-bda3-4544-a6c4-ccbf401b28ce.png)


then press ok to launch the algorithm

## Ready input graphs : 
Clique of (5,5) : 

A vertices :

```1 2 3 4 5```

B vertices : 

```a b c d e```

Edges : 

```(a,1) (a,2) (a,3) (a,4) (a,5) (b,1) (b,2) (b,3) (b,4) (b,5) (c,1) (c,2) (c,3) (c,4) (c,5) (d,1) (d,2) (d,3) (d,4) (d,5) (e,1) (e,2) (e,3) (e,4) (e,5)```

Clique of (10,10) : 

A vertices : 

1 2 3 4 5 6 7 8 9 10

B vertices : 

a b c d e f g h i j

Edges :

(a,1) (a,2) (a,5) (a,6) (a,7) (a,8) (a,9) (a,10) (b,3) (b,4) (b,5) (b,6) (b,7) (b,8) (b,9) (b,10) (c,1) (d,1) (d,3) (d,4) (d,6) (d,7) (d,8) (d,9) (f,10) (g,1) (g,2) (g,3) (g,4) (g,5) (g,6) (g,7) (g,8) (g,9) (g,10) (h,2) (h,3) (h,4) (h,5) (h,10) (i,1) (i,9) (i,10) (j,8) (j,9) (j,10)


## License
[MIT](https://choosealicense.com/licenses/mit/)
