# python-runtime

## Running with docker

Place all your resources under `python_files` folder

```sh
# Run with docker
$> docker-compose up -d
$> docker-compose exec python3 /bin/bash
```

## Using requirements file

```sh
# Go to python_files folder 
$> cd /python_files
# Getting used pip packages list
$> pip freeze > requirements.txt
# Installing used pip packages list
$> pip install -r requirements.txt
```

## Installed libraries

### Data Science

1. **[NumPy](https://numpy.org/)**  
NumPy is a well known general-purpose array-processing package. An extensive collection of high complexity mathematical functions make NumPy powerful to process large multi-dimensional arrays and matrices. NumPy is very useful for handling linear algebra, Fourier transforms, and random numbers. Other libraries like TensorFlow uses NumPy at the backend for manipulating tensors. 

    ```python
    import numpy
    numpy.__version__
    ```

2. **[Pandas](https://pandas.pydata.org/)**  
Pandas are turning up to be the most popular Python library that is used for data analysis with support for fast, flexible, and expressive data structures designed to work on both “relational” or “labeled” data. Pandas today is an inevitable library for solving practical, real-world data analysis in Python. Pandas is highly stable, providing highly optimized performance. The backend code is purely written in C or Python. 

    ```python
    import pandas
    pandas.__version__
    ```

3. **[Matplotlib](https://matplotlib.org/)**  
Matplotlib is a data visualization library that is used for 2D plotting to produce publication-quality image plots and figures in a variety of formats. The library helps to generate histograms, plots, error charts, scatter plots, bar charts with just a few lines of code. 

    ```python
    import matplotlib
    matplotlib.__version__
    ```

4. **[Seaborn](https://seaborn.pydata.org/)**  
Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

    ```python
    import seaborn
    seaborn.__version__
    ```

5. **[Scipy](https://www.scipy.org/)**  
SciPy (pronounced “Sigh Pie”) is a Python-based ecosystem of open-source software for mathematics, science, and engineering.

    ```python
    import scipy
    scipy.__version__
    ```

### Machine learning

1. **[scikit-learn](https://scikit-learn.org/stable/)**  
Scikit-learn (formerly scikits.learn and also known as sklearn) is a free software machine learning library for the Python programming language. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy. 

    ```python
    import sklearn
    sklearn.__version__
    ```

### Databases

1. **[psycopg2](https://www.psycopg.org/)**  
Psycopg is the most popular PostgreSQL adapter for the Python programming language. Its core is a complete implementation of the Python DB API 2.0 specifications. Several extensions allow access to many of the features offered by PostgreSQL.

    ```python
    import psycopg2
    psycopg2.__version__
    ```

2. **[pymssql](http://www.pymssql.org/)**  
A simple database interface for Python that builds on top of FreeTDS to provide a Python DB-API (PEP-249) interface to Microsoft SQL Server.

    ```python
    import pymssql
    pymssql.__version__
    ```