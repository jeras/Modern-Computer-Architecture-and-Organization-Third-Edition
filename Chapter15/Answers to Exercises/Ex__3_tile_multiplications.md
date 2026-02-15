__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 15, Exercise 3

Consider the multiplication of a 1,024 x 768 matrix by a 768 x 768 matrix, as occurs in the linear projection operation at the beginning of the attention block of _Figure 15.3_. Assume the GPU performing this multiplication uses a 16 x 16 tile size (See the _Tensor Processing_ section of _Chapter 10 – Graphics Processing Units_ for more information about tile-based tensor operations). How many tile multiplications and how many additions of the multiplication results are required to multiply the two large matrices? Assume the destination matrix has been initialized to all zeros, and the results of all tile multiplications are added into the destination tiles.

# Answer

1.	Dividing the dimensions of each matrix by the corresponding tile size, the resulting dimensions are 64 x 48 tiles multiplied by 48 x 48 tiles.
2.	Each tile of the output matrix results from the multiplication of 48 tiles by 48 tiles.
3.	There are 64 x 48 tiles in the output matrix, so the total number of tile multiplications is 64 x 48 x 48 = **147,456 tile multiplications**.
4.	Given the assumptions, the total number of additions is the same: **147,456 tile additions**.
