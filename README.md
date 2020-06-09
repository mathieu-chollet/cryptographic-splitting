# cryptographic-splitting-poc

A cryptographic splitting (academic) proof of concept

Here you will find a simple implemementation of [Cryptographic splitting](https://en.wikipedia.org/wiki/Cryptographic_splitting).

This is not optimised for performance, but for transparency of the approach: the 1<sup>st</sup>, 3<sup>rd</sup>, 5<sup>th</sup>, ... **bits** are put in file 1, while the 2<sup>nd</sup>, 4<sup>th</sup>, 6<sup>th</sup>, ... **bits** are put in file 2, keeping the original bit positions (hence half of the output files are 0).

# Functions

`split_file(path_in, path_out_1, path_out_2)` splits the file given at `path_in` to `path_out_1` and `path_out_2`
`merge_files(path_in_1, path_in_2, path_out)` merges the file given at `path_in_1` and `path_in_2` to `path_out`

# Author

[Mathieu Chollet](https://mchollet.eu/)
