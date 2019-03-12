# Multiplying-Sparse-Matrices-with-MapReduce
There are two big sparse matrices M and N (each is 100k * 10k), compute the multiplication of them by using MapReduce. Matrices are stored with the following format: <br/> 
<*i*><**TAB**><*j*><**TAB**><*m*<sub>*i*</sub><sub>*j*</sub>><br/>
<*j*><**TAB**><*k*><**TAB**><*n*<sub>*j*</sub><sub>*k*</sub>><br/>
If you want to install Hadoop cluster by yoursrlf, you can refer to my tutorial (https://zhuanlan.zhihu.com/p/58968191)<br/>
I use Hadoop streaming with Python to solve this problem. There are three MapReduce jobs in total.
## Stage 1 <br/>
mappper: add tag to matrices M and N so as to differentiate them. Swap *i* and *j* in M. Output is <br/>
<*j*><**TAB**><**m**><**TAB**><*i*><**TAB**><*m*<sub>*i*</sub><sub>*j*</sub>><br/>
<*j*><**TAB**><**n**><**TAB**><*k*><**TAB**><*n*<sub>*j*</sub><sub>*k*</sub>><br/>
reducer: no reducer in this stage <br/>
## Stage 2 <br/>
mapper: identity mapper
reducer: Cartesian product of record with the same *j* from M and N matrices, output is <br>
< *i*,*k* ><**TAB**>< *m*<sub>*ij*</sub> * *n*<sub>*jk*</sub>> </br>
## Stage 3 </br>
mapper: identity mapper
reducer: sum record with same key (i,k)
