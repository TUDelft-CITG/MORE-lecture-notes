# Definition of vine-copula

As stated in Section [Minimal concepts of graph theory](graph_theory), a tree is a connected graph with no cycles. A *vine* is a sequence of trees $T_1,…,T_{n-1}$ such that the edges of $T_i$ become nodes of $T_{i+1}$ for $i=1,…,n-1$. If all edges in $T_i$ connected as nodes in $T_{i+1}$ are adjacent to a common node in $T_i$ then this is a regular vine. Figure \ref{D-vine-5} presents a regular vine with five nodes. 



In $T_1$ 3 is adjacent to 4; 4 is adjacent to 3 and 2; 2 is adjacent to 4 and 1; 1 is adjacent to 2 and 5; 5 is adjacent to 1. Thus, 3 has degree 1, 4 has degree 2, 2 has degree 2, 1 has degree 2 and 5 has degree 1. These types of trees are commonly referred to as "*lines*". That is, trees that have two nodes with degree one (*leafs*) and the rest with degree 2. 