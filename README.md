# Reinforcement Learning with Goals

This repo hosts the code associated with my O'Reilly article, "Reinforcement Learning for Various, Complex Goals, Using TensorFlow," published on DATE.

This the code in this repository contains implementations of Deep Q-Network, and [Learning to Act by Predicting the Future](https://arxiv.org/abs/1611.01779).

## Requirements and installation
In order to run this notebook, you'll need to install:
* [TensorFlow v1.0](https://www.tensorflow.org/)
* [Jupyter](http://jupyter.org/)
* [NumPy](http://www.numpy.org/)
* [Scipy]
* [Matplotlib](http://matplotlib.org/)
* [Pillow]
* [Imageio]

There are two easy ways to install these libraries and their dependencies:

### Option A: use the provided Dockerfile configured for this notebook

1. Download and unzip [this entire repo from GitHub](https://github.com/awjuliani/dfp), either interactively, or by entering
    ```bash
    git clone https://github.com/awjuliani/dfp.git
    ```

2. Open your terminal and use `cd` to navigate into the top directory of the repo on your machine

3. To build the Dockerfile, enter
    ```bash
    docker build -t dfp_dockerfile -f dockerfile .
    ```
    If you get a permissions error on running this command, you may need to run it with `sudo`:
    ```bash
    sudo docker build -t dfp_dockerfile -f dockerfile .
    ```

4. Run Docker from the Dockerfile you've just built
    ```bash
    docker run -it -p 8888:8888 -p 6006:6006 dfp_dockerfile bash
    ```
    or
    ```bash
    sudo docker run -it -p 8888:8888 -p 6006:6006 dfp_dockerfile bash
    ```
    if you run into permission problems.

5. Launch Jupyter by entering
    ```bash
    jupyter notebook
    ```
    and, using your browser, navigate to the URL shown in the terminal output (usually http://localhost:8888/)

### Option B: install Anaconda Python, TensorFlow, and other requirements
NumPy can be tricky to install manually, so we recommend using the managed Anaconda Python distribution, which includes NumPy, Matplotlib, and Jupyter in a single installation. The Docker-based method above is much easier, but if you have a compatible NVIDIA GPU, manual installation makes it possible to use GPU acceleration to speed up training.

1. Follow the [installation instructions for Anaconda Python](https://www.continuum.io/downloads). **We recommend using Python 3.6.**

2. Follow the platform-specific [TensorFlow installation instructions](https://www.tensorflow.org/install/). Be sure to follow the "Installing with Anaconda" process, and create a Conda environment named `tensorflow`.

3. If you aren't still inside your Conda TensorFlow environment, enter it by typing
    ```bash
    source activate tensorflow
    ```

4. Install other requirements by entering
    ```bash
    pip install requirements.txt
    ```

5. Download and unzip [this entire repo from GitHub](https://github.com/awjuliani/dfp), either interactively, or by entering
    ```bash
    git clone https://github.com/awjuliani/dfp.git
    ```

6. Use `cd` to navigate into the top directory of the repo on your machine

7. Launch Jupyter by entering
    ```bash
    jupyter notebook
    ```
    and, using your browser, navigate to the URL shown in the terminal output (usually http://localhost:8888/)
