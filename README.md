<img src="icta.png" alt="icta" style=auto/>

## An automatic machine learning based customer segmentation model with RFM analysis ICTA 2024
---

### 1. Install Hadoop and Spark
First, you need install Hadoop and Spark tools. Follow the two installation instructions below:

+ [Installing latest Hadoop 3.4 on Ubuntu 2024](https://medium.com/@nsidana123/installing-latest-hadoop-3-4-on-ubuntu-2024-easy-installation-guide-874f889fede7)

+ [How to Install Spark on Ubuntu](https://medium.com/@redswitches/how-to-install-spark-on-ubuntu-965266d290d6)

---
### 2. Environments settings
#### 2.1 Create environments

Create virtual environments to ensure that libraries between applications do not conflict.You can create virtual environments anywhere you want. Using `python` for Window or `python3` for Linux.

```bash
$ python3 -m venv customer_segmentation_project
```
#### 2.2 Download source code
Download repo from github to local.

```bash
$ git clone https://github.com/nthaihoc/segmentation-customer-hadoop-spark-mlops-icta-2024.git
```
---
### 3. Start application
#### 3.1 Directory structure

<img src="folder_structure.png" alt="folder structure" style=auto/>

There are some important files as `artifacts`, `src` and `dvc.yaml`.

+ `artifact` include model and results file
+ `src` include source code of application
+ `dvc.yaml` is a configuration file, supporting automatic command line execution, for building and managing pipelines

See more infomation about `dvc`: https://dvc.org/

#### 3.2 Run pipeline

After successfully installing all the above steps, run the following command to start testing the application.
```bash
$ source customer_segmentation_project/bin/activate
$ cd customer_segmentation_project
$ cd segmentation-customer-hadoop-spark-mlops-icta-2024
$ dvc repro
```
---