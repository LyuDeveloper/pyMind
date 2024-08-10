<img src="pyMind.png" width="256">

# pyMind
#### Version: CONCEPT 1.0.0 ( Public 1 )

##### What is this?
An attempt to implement a habit discovery feature similar to Xiaomi HyperMind using a Python algorithm.

##### How it works?
Collect user actions on smart appliances. After collection, determine user habits by checking whether the interval between two operations is less than thirty seconds and whether these two actions occur simultaneously multiple times.

The collected data will be saved locally.

##### Why CONCEPT VERSION?

The basic concept of the function has been completed, and there are still many things to fill in.

#### Directory structure
>├─Data: Store user operation records *.json\
├─Habit: Storing discovered habits habits.json\
├─Log: Log directory\
│  ├─Collector\
│  └─Mind

### ATTENTION
The current version has not been fully tested and may contain undiscovered bugs. It is not recommended to use it in production environments for a long time

If you want to conveniently test pyMind and discover more issues, you can try updating and improving Tester (main.py),
