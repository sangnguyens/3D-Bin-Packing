## Experiment Runs used in evaluation tests

****************************************************************************************************
__Next Test:__
acktr with internal_node_holder=800 stopping at 35000 updates

__Run name:__
Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox

__Run command:__
`python main.py --seed 42 --internal-node-holder 800 --model-update-interval 1000 –model-save-interval 1000 --use-acktr USE_ACKTR`

__Other Notes:__
Changed `train_tools.py` to have training stop at 35000 updates (lines 63-64))

__givenData.py__ settings:
```
container_size = [10,10,10]

lower = 1
higher = 5 ## Change to have uniform boxes was 1-5, now 2-2
resolution = 1
item_size_set = []
for i in range(lower, higher + 1):
    for j in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
        for k in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
                item_size_set.append((i * resolution, j * resolution , k *  resolution))
```

__Output File:__
logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51

__Completed__
****************************************************************************************************
****************************************************************************************************

__Next Test:__
acktr Rectangular Bin with internal_node_holder=800 stopping at 35000 updates

__Run name:__
Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox

__Run command:__
`python main.py --seed 42 --internal-node-holder 800 --model-update-interval 1000 –model-save-interval 1000 --use-acktr USE_ACKTR`

__Other Notes:__
Changed `train_tools.py` to have training stop at 35000 updates (lines 63-64))

__givenData.py__ settings:
```
container_size = [20,10,10]

lower = 1
higher = 5 ## Change to have uniform boxes was 1-5, now 2-2
resolution = 1
item_size_set = []
for i in range(lower, higher + 1):
    for j in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
        for k in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
                item_size_set.append((i * resolution, j * resolution , k *  resolution))
```

__Output File:__
`logs/experiment/Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52`

__Completed__


****************************************************************************************************
****************************************************************************************************
__Next Test:__
A2C with internal_node_holder=800 stopping at 35000 updates

__Run name:__
Discrete_A2C_10x10x10Bin_s42_inh_800_defaultBox

__Run command:__
`python main.py --seed 42 --internal-node-holder 800 --model-update-interval 1000 –model-save-interval 1000 --use-acktr USE_A2C` 

__Other Notes:__
Changed `train_tools.py` to have training stop at 35000 updates (lines 63-64))

__givenData.py__ settings:
```
container_size = [10,10,10]

lower = 1
higher = 5 ## Change to have uniform boxes was 1-5, now 2-2
resolution = 1
item_size_set = []
for i in range(lower, higher + 1):
    for j in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
        for k in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
                item_size_set.append((i * resolution, j * resolution , k *  resolution))
```

__Output File:__

__Incomplete__

****************************************************************************************************
****************************************************************************************************
__Next Test:__
A2C Rectangular Bin with internal_node_holder=800 stopping at 35000 updates

__Run name:__
Discrete_A2C_20x10x10Bin_s42_inh_800_defaultBox

__Run command:__
`python main.py --seed 42 --internal-node-holder 800 --model-update-interval 1000 –model-save-interval 1000 --use-acktr USE_A2C`

__Other Notes:__
Changed `train_tools.py` to have training stop at 35000 updates (lines 63-64))

__givenData.py__ settings:
``` 
container_size = [20,10,10]

lower = 1
higher = 5 ## Change to have uniform boxes was 1-5, now 2-2
resolution = 1
item_size_set = []
for i in range(lower, higher + 1):
    for j in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
        for k in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
                item_size_set.append((i * resolution, j * resolution , k *  resolution))
```

__Output File:__


__Incomplete__


****************************************************************************************************
********************************************************************************************************************************************************************************************************
********************************************************************************************************************************************************************************************************
****************************************************************************************************






## Evaluation Tests for Rendering

****************************************************************************************************
### __Files used in evaluation of the two trained models__

__10 x 10 x 10 Bin__

Evaluation of model after 1000 training episodes:

`./logs/experiment/Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52/PCT-Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52_2022.08.18-13-18-45.pt`

Evaluation of model after 2000 training episodes:

`./logs/experiment/Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52/PCT-Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52_2022.08.18-13-30-37.pt`

Evaluation of model after 34000 training episodes:

`./logs/experiment/Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52/PCT-Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52_2022.08.18-19-30-13.pt`

__20 x 10 x 10 Bin__

Evaluation of model after 1000 training episodes:

`./logs/experiment/Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52/PCT-Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52_2022.08.18-13-18-45.pt`

Evaluation of model after 2000 training episodes:

`./logs/experiment/Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52/PCT-Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52_2022.08.18-13-30-37.pt`

Evaluation of model after 34000 training episodes:

`./logs/experiment/Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52/PCT-Discrete_acktr_20x10x10Bin_s42_inh_800_defaultBox-2022.08.18-13-06-52_2022.08.18-19-30-13.pt`
****************************************************************************************************

 
### __Evaluation Commands for the two trained models__
 


### __10 x 10 x 10 Bin__

****************************************************************************************************

 

### __Bin packed with random boxes with the same size distribution as the training boxes__
givenData.py
```
container_size = [10,10,10]

lower = 1
higher = 5 
short_low = 1
short_high = 3
long_low = 6
long_high = 10
resolution = 1
item_size_set = []

# Default Boxes
for i in range(lower, higher + 1):
    for j in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
        for k in range(lower, higher + 1): ## Changing from + 1 to + 4 for large flat boxes.
                item_size_set.append((i * resolution, j * resolution , k *  resolution))

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

# # Flat Boxes flat on ground
# for i in range(long_low, long_high + 1):
#     for j in range(long_low, long_high + 1): 
#         for k in range(short_low, short_high + 1): 
#                 item_size_set.append(( i * resolution, j * resolution , k *  resolution)) 

```



### **acktr at 1k Updates**

__Next Test:__ 
Evaluation at 1k of Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox
 
__Run name:__
SqBinRandomBoxEval_acktr_01k
 
Run command:
echo 'SqBinRandomBoxEval_acktr_01k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.19-23-59-01.pt' > SqBinRandomBoxEval_acktr_01k
python evaluation.py --evaluate --internal-node-holder 800 --seed 0  --use-acktr USE_ACKTR  --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.19-23-59-01.pt' < 'SqBinRandomBoxEval_acktr_01k' > 'SqBinRandomBoxEval_acktr_01k.log'
 
 
### **acktr at 2k Updates**

__Next Test:__ 
Evaluation at 2k of Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox
 
__Run name:__
SqBinRandomBoxEval_acktr_02k
 
__Run command:__
```
echo 'SqBinRandomBoxEval_acktr_02k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-00-10-07.pt' > SqBinRandomBoxEval_acktr_02k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0   --use-acktr USE_ACKTR --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-00-10-07.pt' < 'SqBinRandomBoxEval_acktr_02k'> 'SqBinRandomBoxEval_acktr_02k.log'
 ```
### **acktr at 34k Updates**

__Next Test:__ 
Evaluation at 34k of Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox
 
__Run name:__
SqBinRandomBoxEval_acktr_34k
 
__Run command:__
```
echo 'SqBinRandomBoxEval_acktr_34k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-06-02-10.pt' > SqBinRandomBoxEval_acktr_34k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0  --use-acktr USE_ACKTR  --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-06-02-10.pt' < 'SqBinRandomBoxEval_acktr_34k' > 'SqBinRandomBoxEval_acktr_34k.log'
```

### __Bin packed with 2 x 2 x 2 cubes__
givenData.py
```
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

# Uniform Boxes
for i in range(lower, higher + 1):
    for j in range(lower, higher + 1): 
        for k in range(lower, higher + 1): 
                item_size_set.append((2 * resolution, 2 * resolution , 2 *  resolution)) # All 2 for uniform boxes

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

# # Flat Boxes flat on ground
# for i in range(long_low, long_high + 1):
#     for j in range(long_low, long_high + 1): 
#         for k in range(short_low, short_high + 1): 
#                 item_size_set.append(( i * resolution, j * resolution , k *  resolution)) 

```




### **acktr at 1k Updates**

__Next Test:__   Evaluation at 1k of Discrete_acktr_10x10x10Bin_s42_inh_800_CubeBox
 
__Run name:__
SqBinCubeBoxEval_acktr_01k
 
__Run command:__
```
echo 'SqBinCubeBoxEval_acktr_01k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.19-23-59-01.pt' > SqBinCubeBoxEval_acktr_01k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.19-23-59-01.pt' < 'SqBinCubeBoxEval_acktr_01k' > 'SqBinCubeBoxEval_acktr_01k.log'
```
 


### **acktr at 2k Updates**
__Next Test:__
Evaluation at 2k of Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox
 
__Run name:__
SqBinCubeBoxEval_acktr_02k
 
__Run command:__
```
echo 'SqBinCubeBoxEval_acktr_02k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-00-10-07.pt' > SqBinCubeBoxEval_acktr_02k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR  --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-00-10-07.pt' < 'SqBinCubeBoxEval_acktr_02k'> 'SqBinCubeBoxEval_acktr_02k.log'
 ```


### **acktr at 34k Updates**
 
__Next Test:__
Evaluation at 34k of Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox
 
__Run name:__
SqBinCubeBoxEval_acktr_34k
 
__Run command:__
```
echo 'SqBinCubeBoxEval_acktr_34k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-06-02-10.pt' > SqBinCubeBoxEval_acktr_34k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-06-02-10.pt' < 'SqBinCubeBoxEval_acktr_34k' > 'SqBinCubeBoxEval_acktr_34k.log'
```
 


### __Bin packed with long boxes__
givenData.py
```
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

# Long Boxes on side
for i in range(long_low, long_high + 1):
    for j in range(short_low, short_high + 1): 
        for k in range(short_low, short_high + 1): 
                item_size_set.append(( i * resolution, j * resolution , k *  resolution)) 

# # Flat Boxes on end
# for i in range(short_low, short_high + 1):
#     for j in range(long_low, long_high + 1): 
#         for k in range(long_low, long_high + 1): 
#                 item_size_set.append(( i * resolution, j * resolution , k *  resolution)) 

# # Flat Boxes flat on ground
# for i in range(long_low, long_high + 1):
#     for j in range(long_low, long_high + 1): 
#         for k in range(short_low, short_high + 1): 
#                 item_size_set.append(( i * resolution, j * resolution , k *  resolution)) 

```


 ### **acktr at 1k Updates**

 
__Next Test:__
Evaluation at 1k of Discrete_acktr_10x10x10Bin_s42_inh_800_LongBox
 
__Run name:__
SqBinLongBoxEval_acktr_01k
 
__Run command:__
```
echo 'SqBinLongBoxEval_acktr_01k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.19-23-59-01.pt' > SqBinLongBoxEval_acktr_01k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.19-23-59-01.pt' < 'SqBinLongBoxEval_acktr_01k' > 'SqBinLongBoxEval_acktr_01k.log'
```
 
 
### **acktr at 2k Updates**
__Next Test:__ 
Evaluation at 2k of Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox
 
__Run name:__
SqBinLongBoxEval_acktr_02k
 
__Run command:__
```
echo 'SqBinLongBoxEval_acktr_02k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-00-10-07.pt' > SqBinLongBoxEval_acktr_02k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-00-10-07.pt' < 'SqBinLongBoxEval_acktr_02k'> 'SqBinLongBoxEval_acktr_02k.log'
 ```

 
### **acktr at 34k Updates**

__Next Test:__ 
Evaluation at 34k of Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox
 
__Run name:__
SqBinLongBoxEval_acktr_34k
 
__Run command:__
``` 
'SqBinLongBoxEval_acktr_34k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-06-02-10.pt' > SqBinLongBoxEval_acktr_34k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-06-02-10.pt' < 'SqBinLongBoxEval_acktr_34k' > 'SqBinLongBoxEval_acktr_34k.log'
 ```


### __Bin packed with flat boxes__
givenData.py
```
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
```




### **acktr at 1k Updates**

__Next Test:__ 
Evaluation at 1k of Discrete_acktr_10x10x10Bin_s42_inh_800_FlatBox
 
__Run name:__
SqBinFlatBoxEval_acktr_01k
 
__Run command:__
``` 
 'SqBinFlatBoxEval_acktr_01k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.19-23-59-01.pt' > SqBinFlatBoxEval_acktr_01k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.19-23-59-01.pt' < 'SqBinFlatBoxEval_acktr_01k' > 'SqBinFlatBoxEval_acktr_01k.log'
 ```
 
### **acktr at 2k Updates**

__Next Test:__ 
Evaluation at 2k of Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox
 
__Run name:__
SqBinFlatBoxEval_acktr_02k
 
__Run command:__
``` 
 'SqBinFlatBoxEval_acktr_02k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-00-10-07.pt' > SqBinFlatBoxEval_acktr_02k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR  --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-00-10-07.pt'  <  'SqBinFlatBoxEval_acktr_02k' > 'SqBinFlatBoxEval_acktr_02k.log'
```
 
### **acktr at 34k Updates**

__Next Test:__ 
Evaluation at 34k of Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox
 
__Run name:__
SqBinFlatBoxEval_acktr_34k
 
__Run command:__
``` 
 'SqBinFlatBoxEval_acktr_34k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-06-02-10.pt' > SqBinFlatBoxEval_acktr_34k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-06-02-10.pt' < 'SqBinFlatBoxEval_acktr_34k' > 'SqBinFlatBoxEval_acktr_34k.log'
```
 
 

### __Bin packed with flat boxes__
givenData.py
```
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

# Flat Boxes on end
for i in range(short_low, short_high + 1):
    for j in range(long_low, long_high + 1): 
        for k in range(long_low, long_high + 1): 
                item_size_set.append(( i * resolution, j * resolution , k *  resolution)) 

# # Flat Boxes flat on ground
# for i in range(long_low, long_high + 1):
#     for j in range(long_low, long_high + 1): 
#         for k in range(short_low, short_high + 1): 
#                 item_size_set.append(( i * resolution, j * resolution , k *  resolution)) 
```

### **acktr at 1k Updates**

__Next Test:__ 
Evaluation at 1k of Discrete_acktr_10x10x10Bin_s42_inh_800_FlatBoxVert
 
__Run name:__
SqBinFlatBoxVertEval_acktr_01k
 
__Run command:__
``` 
 'SqBinFlatBoxVertEval_acktr_01k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.19-23-59-01.pt' > SqBinFlatBoxVertEval_acktr_01k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.19-23-59-01.pt' < 'SqBinFlatBoxVertEval_acktr_01k' > 'SqBinFlatBoxVertEval_acktr_01k.log'
 ```
 
### **acktr at 2k Updates**

__Next Test:__ 
Evaluation at 2k of Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox
 
__Run name:__
SqBinFlatBoxVertEval_acktr_02k
 
__Run command:__
``` 
 'SqBinFlatBoxVertEval_acktr_02k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-00-10-07.pt' > SqBinFlatBoxVertEval_acktr_02k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR  --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-00-10-07.pt' < 'SqBinFlatBoxVertEval_acktr_02k'> 'SqBinFlatBoxVertEval_acktr_02k.log'
```

 
### **acktr at 34k Updates**

__Next Test:__  
Evaluation at 34k of Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox
 
__Run name:__
SqBinFlatBoxVertEval_acktr_34k
 
__Run command:__
``` 
 'SqBinFlatBoxVertEval_acktr_34k.log___PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-06-02-10.pt' > SqBinFlatBoxVertEval_acktr_34k

python evaluation.py --evaluate --internal-node-holder 800 --seed 0 --use-acktr USE_ACKTR --load-model --model-path './logs/experiment/Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51/PCT-Discrete_acktr_10x10x10Bin_s42_inh_800_defaultBox-2022.08.19-23-47-51_2022.08.20-06-02-10.pt' < 'SqBinFlatBoxVertEval_acktr_34k' > 'SqBinFlatBoxVertEval_acktr_34k.log'
 ```
 
