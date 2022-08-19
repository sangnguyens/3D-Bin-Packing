# Bin Packing Problem Experiments using Packing Configuration Trees

## We used the code from the GitHub [repo](https://github.com/alexfrom0815/Online-3D-BPP-PCT) by Hang Zhao on 3D bin packing with configuration trees.

## For our experiments we trained the RL agents for 35,000 updates and updated and saved the model every 1,000 updates.
### We used the following parameters to train our agent:
* Trained for a total of 35,000 updates.
* Updated and saved the model every 1,000 updates using flags `--model-save-interval 1000 --model-update-interval 1000`.
* Generated data that sampled boxs with edge lengths varying from 1 to 5 using the file `givenData.py` by editing the `lower` and `higher` edges of `item_size_set`.
* Trained using a bin size of either 10x10x10 or 20x10x10 by editing the `container_size` in `givenData.py`.
* A random seed of 42 with the flag `--seed 42`.
* Set the `internal node holder` to `800` to prevent the model from exiting training early with the flag `--set internal-node-holder 800`.
* Used an either __A2C__ or __acktr__ reinforcement learning agent using the flag `-use-acktr USE_ACKTR` to select the acktr agent as the A2C agent is used by default.

The general run command was similar to: `python main.py --seed 42 --internal-node-holder 800 --use-acktr USE_ACKTR --model-update-interval 1000  --model-save-interval 1000` .

### We then evaluated the different trained models using several different selections of boxes by editing `givenData.py`:
* The same generated data set using *random placement* (no RL agent) for a baseline (added a flag of `--heuristic RANDOM`)
* Uniform 2x2x2 cubes.
* The same generated data sampling.
* Long skinny boxes by sampling from boxes generated with 2 short edges (less than 3) and one long edge (greater than 5)
* Large flat boxes by sampling from boxes generate with 1 short edge (less than 3) and two long edges (greater than 5)


The general evaluation command was similar to: `python evaluation.py --evaluate --internal-node-holder 800  --load-model --model-path 'Path-to-saved-model/model.pt'`

### After running the evaluation, the results are stored in a file named `trajs.npy` file under the `logs/evaluation/`. Using this file, we then produced images of the bin with the packed boxes.


### From there experiments we conclude:
* 
* 


# Experiment instructions
## Important files for creating and training RL agent
* Test_Log.txt
* givenData.py
* heuristic.py 
* tools.py

## Test_Log.txt
Keep track of all of the training sessions attempted in this file. Copy bottom section and create your own.

        ****************************************************************************************************
    Next Test:
    Run name:
    Run command:
    givenData.py settings:
* `Run name` is the name of the run you entered
* `Run command` is the command you used to execute the run.
* `givenData.py settings` is a copy of the lines in givenData.py that indicates what bin size and box sizes were used in the experiment.

