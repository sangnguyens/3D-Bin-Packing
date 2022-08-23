# container_size: A vector of length 3 describing the size of the container in the x, y, z dimension.
# item_size_set:  A list records the size of each item. The size of each item is also described by a vector of length 3.
import random 

# random.seed(13) 

container_size = [10,10,10]

lower = 1
higher = 5 
short_low = 1
short_high = 3
long_low = 6
long_high = 10
resolution = 1
item_size_set = []

# # Default Boxes
# for i in range(lower, higher + 1):
#     for j in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
#         for k in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
#                 item_size_set.append((i * resolution, j * resolution , k *  resolution))

# # Uniform Boxes
# for i in range(lower, higher + 1):
#     for j in range(lower, higher + 1): 
#         for k in range(lower, higher + 1): 
#                 item_size_set.append((2 * resolution, 2 * resolution , 2 *  resolution)) # All 2 for uniform boxes

# # Long Boxes on side
# for i in range(long_low, long_high + 1):
#     for j in range(short_low, short_high + 1): 
#         for k in range(short_low, short_high + 1): 
#                 item_size_set.append(( i * resolution, j * resolution , k *  resolution)) 

# # Flat Boxes on end
# for i in range(short_low, short_high + 1):
#     for j in range(long_low, long_high + 1): 
#         for k in range(long_low, long_high + 1): 
#                 item_size_set.append(( i * resolution, j * resolution , k *  resolution)) 

# Flat Boxes flat on ground
for i in range(long_low, long_high + 1):
    for j in range(long_low, long_high + 1): 
        for k in range(short_low, short_high + 1): 
                item_size_set.append(( i * resolution, j * resolution , k *  resolution)) 



# If you want to sample item sizes from a uniform distribution in continuous domain,
# type --sample-from-distribution in your command line.