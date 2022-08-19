# 3D-Bin-Packing Project
This project is a 3D Packing Optimization project under mentorship of InstaDeep. The source code of this repository can be found at [Hang Zhao](https://github.com/alexfrom0815) The ultimate goal is to pack a Unit Load Device [Unit Load Device Description](https://en.wikipedia.org/wiki/Unit_load_device)


<p style="text-align: center;"><img src="https://upload.wikimedia.org/wikipedia/commons/8/81/Unit_load_device_sizes.png" height="99" width="136.5" > 

[image credit Marc Lacoste](https://commons.wikimedia.org/wiki/User:Marc_Lacoste)</p>


Specific dimensions for several [Unit Load Devices](https://freight.qantas.com/freight-planning/equipment-uld.html).

## Why?
Is it possible to pack shipping containers more efficiently? Save space, save time, save money - pack efficiently.
Packing efficiently has the potential to reduce shipping costs that have increased due to the increase in fuel costs, shipping containers, trucks, and shipping bottlenecks.

For our experiments we trained the RL agents for **35,000** updates and updated and saved the model every **1,000** updates.
We used the following parameters to train our agent:
* Trained for a total of 35,000 updates.
* Updated and saved the model every 1,000 updates using flags `--model-save-interval 1000 --model-update-interval 1000`.
* Generated data that sampled boxs with edge lengths varying from 1 to 5 using the file `givenData.py` by editing the `lower` and `higher` edges of `item_size_set`.
* Trained using a bin size of either 10x10x10 or 20x10x10 by editing the `container_size` in `givenData.py`.
* A random seed of 42 with the flag `--seed 42`.
* Set the `internal node holder` to `800` to prevent the model from exiting training early with the flag `--set internal-node-holder 800`.
* Used an either __A2C__ or __acktr__ reinforcement learning agent using the flag `-use-acktr USE_ACKTR` to select the acktr agent as the A2C agent is used by default.

To reproduce, the general run command was similar to:
```
python main.py --seed 42 --internal-node-holder 800 --use-acktr USE_ACKTR --model-update-interval 1000  --model-save-interval 1000
```

We then evaluated the different trained models using several different selections of boxes by editing `givenData.py`:
* Uniform 2x2x2 cubes.
* The same generated data sampling.
* Long skinny boxes by sampling from boxes generated with 2 short edges (less than 3) and one long edge (greater than 5)
* Large flat boxes by sampling from boxes generate with 1 short edge (less than 3) and two long edges (greater than 5)

To reproduce, the general evaluation command was similar to: 
```python evaluation.py --evaluate --internal-node-holder 800  --load-model --model-path 'Path-to-saved-model/model.pt
```

## Scope
Open-ended research questions:
* Which package do I pick next and how do I set the order of items before placing/packing?
* For an item (id: 1, length: L, width: W, height: H): Where do I place it and do I rotate it? Do I force the first package to be in the bottom-left corner?
* How do I observe and encode the current state?

## Expected Learning Outcomes
1. Building a clean RL environment in python
2. Code testing and possibly test-driven development (TDD)
3. Learning to formulate real-world use-cases into ML/RL problems
4. Learning to implement and/or use advanced ML/RL algorithms and models

## How to get it work
1. Prepare environment
```
git clone git@github.com:sangnguyens/3D-Bin-Packing.git
cd 3D-Bin-Packing
conda env create --file packing_env.yml
```
2. Train model (default mode):
```
python main.py
```
3. Evaluate model from pretrained model (default mode):
```
python evaluation.py
```
## Rendering
run evaluation.py and come to `nb` folder run notebook to see how agent 
packs and places boxes.

## Help
```
python main.py -h
python evaluation.py -h
```

## Group Members
* Jongbum Lee
* Cristina Moody
* Sang Nguyen

