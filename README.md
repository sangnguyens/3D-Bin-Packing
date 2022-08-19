# 3D-Packing Project
This project is a 3D Packing Optimization project in partnership with InstaDeep. The ultimate goal is to pack a Unit Load Device [Unit Load Device Description](https://en.wikipedia.org/wiki/Unit_load_device)


<p style="text-align: center;"><img src="https://upload.wikimedia.org/wikipedia/commons/8/81/Unit_load_device_sizes.png" height="99" width="136.5" > 

[image credit Marc Lacoste](https://commons.wikimedia.org/wiki/User:Marc_Lacoste)</p>


Specific dimensions for several [Unit Load Devices](https://freight.qantas.com/freight-planning/equipment-uld.html).

### Why?
Is it possible to pack shipping containers more efficiently? Save space, save time, save money - pack efficiently.
Packing efficiently has the potential to reduce shipping costs that have increased due to the increase in fuel costs, shipping containers, trucks, and shipping bottlenecks.

### Scope
Open-ended research questions:
* Which package do I pick next and how do I set the order of items before placing/packing?
* For an item (id: 1, length: L, width: W, height: H): Where do I place it and do I rotate it? Do I force the first package to be in the bottom-left corner?
* How do I observe and encode the current state?

### Expected Learning Outcomes
1. Building a clean RL environment in python
2. Code testing and possibly test-driven development (TDD)
3. Learning to formulate real-world use-cases into ML/RL problems
4. Learning to implement and/or use advanced ML/RL algorithms and models


## Group Members
* Jongbum Lee
* Cristina Moody
* Sang Nguyen


This is the repository of 3D Packing capstone project designed to productionize MLops with Reinforcement Learning.

## What we've done so far:
* We've started completing our own environments in 
  * [2D-packing.ipynb](https://github.com/seive76/3D-Packing/blob/main/2D-packing.ipynb) & 
  * [BBP_w_alexfrom0815.ipynb](https://github.com/seive76/3D-Packing/blob/main/BBP_w_alexfrom0815.ipynb) & 
  * [Env2D.ipynb](https://github.com/seive76/3D-Packing/blob/main/nb/Env2D.ipynb)
* We're working with code from [Hang Zhao](https://github.com/alexfrom0815)

### 

### Experiment Code From alexfrom0815
* [Online-3D-BPP-DRL](https://github.com/alexfrom0815/Online-3D-BPP-DRL)
  * @inproceedings{DBLP:conf/aaai/ZhaoS0Y021,
  author    = {Hang Zhao and
               Qijin She and
               Chenyang Zhu and
               Yin Yang and
               Kai Xu},
  title     = {Online 3D Bin Packing with Constrained Deep Reinforcement Learning},
  booktitle = {Thirty-Fifth {AAAI} Conference on Artificial Intelligence, {AAAI}
               2021, Thirty-Third Conference on Innovative Applications of Artificial
               Intelligence, {IAAI} 2021, The Eleventh Symposium on Educational Advances
               in Artificial Intelligence, {EAAI} 2021, Virtual Event, February 2-9,
               2021},
  pages     = {741--749},
  publisher = {{AAAI} Press},
  year      = {2021},
  url       = {https://ojs.aaai.org/index.php/AAAI/article/view/16155},
  timestamp = {Wed, 02 Jun 2021 18:09:11 +0200},
  biburl    = {https://dblp.org/rec/conf/aaai/ZhaoS0Y021.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
* [Online-3D-BPP-PCT](https://github.com/alexfrom0815/Online-3D-BPP-PCT)
  * @inproceedings{ zhao2022learning, title={Learning Efficient Online 3D Bin Packing on Packing Configuration Trees}, author={Hang Zhao and Yang Yu and Kai Xu}, booktitle={International Conference on Learning Representations}, year={2022}, url={https://openreview.net/forum?id=bfuGjlCwAq} }

