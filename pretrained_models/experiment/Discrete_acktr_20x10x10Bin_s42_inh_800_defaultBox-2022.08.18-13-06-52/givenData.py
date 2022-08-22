# container_size: A vector of length 3 describing the size of the container in the x, y, z dimension.
# item_size_set:  A list records the size of each item. The size of each item is also described by a vector of length 3.

container_size = [20,10,10]

lower = 1
higher = 5 ## Change to have uniform boxes was 1-5, now 2-2
resolution = 1
item_size_set = []
for i in range(lower, higher + 1):
    for j in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
        for k in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
                item_size_set.append((i * resolution, j * resolution , k *  resolution))

# If you want to sample item sizes from a uniform distribution in continuous domain,
# type --sample-from-distribution in your command line.