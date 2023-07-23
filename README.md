# resample

Resampling a list is to slice the list with a step `s` such as `li[::,s]`.

However, if the step is not integer number, then the above approach does not work. One of the approach to resample the list is shown in this repo.

If the ratio to sample is bigger than 1, then the list is subsampled. If the ratio is smaller than 1, then the list is supsampled, some elements are repeated.
