## An automatic machine learning based customer segmentation model with RFM analysis ICTA 2024

### 1. Install Hadoop and Spark

* Follow the two installation instructions below:
    + [Installing latest Hadoop 3.4 on Ubuntu 2024](https://medium.com/@nsidana123/installing-latest-hadoop-3-4-on-ubuntu-2024-easy-installation-guide-874f889fede7)
    + [How to Install Spark on Ubuntu](https://medium.com/@redswitches/how-to-install-spark-on-ubuntu-965266d290d6)

### 2. Environments settings

* Download repo from github to local:
```bash
$git clone https://github.com/nthaihoc/segmentation-customer-hadoop-spark-mlops-icta2024.git
```
* Install library necessary in requirements file. Before installing, make sure you are inside the folder containing the `requirement` file. Using `pip` for Window or `pip3` for Linux:

```bash
$pip3 install -r requirements
```

### 3. Run Application

* Start `namenode`, `datanode` and `yarn`:
```bash
$start-dfs.sh
$start-yarn.sh
```

* Then start `master` and `worker` on Spark:
```bash
$start-master.sh
$start-worker.sh
```

* Run pipeline
```bash
$spark-submit --master yarn \
              --deploy-mode client \
              segmentation-customer-hadoop-spark-mlops-icta2024/main.py 
```

---