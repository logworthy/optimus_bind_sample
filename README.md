<h1 align="center">
<span style="color:red">
    <a href="https://www.quora.com/q/hxbiokqurmxybuec">
		<img src="https://user-images.githubusercontent.com/35203441/112711058-e2bc5300-8e9b-11eb-99e7-5b8708b70505.png" width="100" height="100"></span>
<img src="https://user-images.githubusercontent.com/35203441/112711020-bef90d00-8e9b-11eb-8471-046fd6998bfc.png" width="200" height="100">
</a>

 <!--| Optimus Bind-->

[![Build Status](https://travis-ci.org/tcardlab/optimus_bind_sample.png?branch=master)](https://travis-ci.org/tcardlab/optimus_bind_sample) 
[![Inline docs](http://inch-ci.org/github/tcardlab/optimus_bind_sample.svg?branch=master)](http://inch-ci.org/github/tcardlab/optimus_bind_sample)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/domainName.io.svg)](http://shields.io/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
</h1> 

The Human Genome Project amassed a wealth of data concerning human genetic variation anticipating further utilization. Although this data has provided a method of identifying potential subpopulations, the impact of specific mutations is often unknown. The first step to predict a mutation’s effect is to understand how it affects the binding partners within its interaction network. As such, Optimus Bind scans protein surfaces to evaluate mutations that may affect protein-protein binding. In knowing how the mutation works at the molecular level, you have made the first step toward understanding it at the cellular and organismal levels.

[Full Summary](https://www.quora.com/Quora-Bioscience-Club-is-considering-collaborative-computational-biology-research-projects-What-topics-are-you-interested-in-and-are-able-to-work-on/answer/Jeffrey-Brender?ch=10&share=fdebe6d2&srid=E3wB) 

<details>
<summary><b>Development Overview</b></summary>

### Goals <sup>[1](https://www.quora.com/q/hxbiokqurmxybuec/What-are-the-major-requirements-for-Optimus-Bind-the-collaborative-Quora-project-to-predict-the-impact-of-mutations-on)</sup>

Scientists have increasingly turned to computational methods to predict ΔΔG values (changes in the free energy ΔG upon mutation). These methods are computationally expensive for large datasets to the extent that it becomes prohibitive for genome-wide studies or even scanning mutations on a single protein. There is therefore a clear need for new methods that are both fast and accurate. As such, this collaborative computational biology project aims to predict the effects of mutation directly from protein sequences.

 - **Fast** – Upper limit of 30 minutes per mutation.  
	 - *Problem:* Accurately simulating the physics of the mutation’s effect on ∆∆G can take ~180 hrs for a single mutation.
	 - *Impact:* For every <u>cancer</u>, there can be hundreds of associated “driver” mutations whose identification may help save lives. <u>Protein engineering</u> is another case where speed is critical, as it generates hundreds of mutations if the binding sites are independent and many, many more if they are not.
 - **Accurate** – r>0.9 and an average error of <1 kcal/mol.
 - **Open source**
	 - Many computational projects are locked up in web servers. Anyone can use this program and may build off it if they so desire.
 - **Machine Learning**
	 - A random forest model tried to minimize the number of features to avoid overfitting. However, later versions got rid of machine learning altogether and used a linear sum of two terms. This project aims to bring reimplemt machine learning.
	 - improve scoring system
 -  **Small molecule binding**

### Challenges<sup>[1](https://www.quora.com/q/hxbiokqurmxybuec/Which-is-preferred-genetic-algorithms-neural-networks-or-a-combination-such-as-NEAT), [2](https://www.quora.com/q/hxbiokqurmxybuec?utm_source=quora&utm_medium=referral)</sup>
1. **There isn’t a lot of data** (7085 mutations skempi v2.0)
	 - You can’t get more of it (*easily*...).
	 - The data is not evenly distributed. 
		 - SKEMPI has not evenly sampled mutations we must consider. This sort of imbalanced dataset can skew the machine learning process (skewed toward the subpopulations with the heaviest coverage).
	 - Machine learning based methods are fast and appear to have good accuracy, But they are often overtrained and fall apart when confronted with new data. 
2. **Less than 10% of protein complexes have structures**
	 - While it is possible in most cases to make a model of the protein complex, the accuracy of the model is not perfect. 
3. **Large mutation space to explore** 
	 - (20 amino acids)^(the proteins length)
	 - Even restricted to single mutations, as we would if we are looking at the possible effect of SNPs (single nucleotide polymorphism), this still comes out to hundreds of mutations that need to be evaluated for each protein complex. 
4. **molecular dynamics is slow and dependent upon the structure’s resolution**

### Combative Design

1. Using stratified sampling we can sample all possible cases evenly. To do this we need a feature list that defines the effectively describes the different types of proteins we might encounter.
2. Accept some errors are going to exist and at least have the option of low resolution scoring, using both residue level scoring and local estimates of the accuracy and precision of the structure (either real or predicted) as a feature in machine learning.
3. 
4. One solution is to infer the dynamics of the protein by scaling interactions directly from the sequence (similar to DynaMine and antecedent to how FoldX’s operates).
</details>

<details>
<summary><b>Table of contents</b></summary>

## Table of content
 - [Features](#Features)
	 - [Screenshots](#Screenshots)
 - [Setup](#Setup)
	 - [Prerequisites](#Prerequisites)
	 - [Installing](#Installing)
	 - [Run Tests](#Run-Tests)
 - [For Developers](#For-Developers)
	 - [Project Organization](#Project-Organization)
	 - [Built With](#Built-With)
	 - [Contributing](#Contributing)
 - [Citations](#Citations)
</details>

## Features

### Screenshots

## Setup
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites 

    python3.6+
    git
    make
    curl
    gunzip
    ncbi-blast # (see https://www.ncbi.nlm.nih.gov/books/NBK569861/)

### Installing

working draft while under dev.

Semi-Automated via terminal:

    # Download repo
    git clone https://github.com/BioSciResearch/optimus_bind_sample.git
    cd path/optimus_bind_sample

    # Set up enviroment (Note: 'env' dir ignored by git)
    python3 -m venv env  # creates enviroment env named env
    source env/bin/activate  # activates enviroment
    pip install -r requirements.txt # installs requirements 

    # Database Setup (this can take a while - downloads a 4gb file then takes some time to process)
    # (see https://www.biostars.org/p/214726/)
    mkdir -p data/db
    curl http://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.fasta.gz -o data/db/Pfam-A.fasta.gz
    gunzip data/db/Pfam-A.fasta.gz
    cd data/db 
    makeblastdb -in Pfam-A.fasta -dbtype prot

    # Dataset setup 
    #  - This can take a while, ~1 hour for 10 iterations
    #  - Number of iterations can be updated within SKEMPI_loop.py loop_over_chains function
    #  - Some warnings generated but can be ignored
    make data  # only imports raw for now, must be in root directory
    python data/src/SKEMPI_loop.py # creates output in data/seq

<!--
entirely manual terminal:
    # Download repo
    git clone https://github.com/tcardlab/optimus_bind_sample.git
    cd path/optimus_bind_sample

    # Set up enviroment (Note: 'env' dir ignored by git)
    python3 -m venv env  # creates enviroment env named env
    source env/bin/activate  # activates enviroment
    pip install -r requirements.txt # installs requirements

    # Dataset setup
    python src/data/download_raw.py
    python src/data/make_dataset.py

IDK if this works...: 
    python setup.py install
add ^"Dataset setup" to scripts in setup.py to autorun?

    # Set up enviroment (See manual set up)
    make requirements
    (havent tested yet. I set up manually which satisfies this.)
-->

colab setup:
    #

### Run Tests

    python -i src/data/protein.py
    >>> pm = ProteinMethods('')
    >>> pm.readBlast('data/seq/1A22_A.xmld')
    >>> pm.PSSM[17]
    {'A': 24.0, 'C': 0, 'D': 38.0, 'E': 43.0, 'F': 0, 'G': 4.0, 'H': 99.0, 'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 5.0, 'P': 0, 'Q': 55.0, 'R': 6.0, 'S': 19.0, 'T': 3.0, 'V': 3.0, 'W': 0, 'X': 0, 'Y': 6.0}

<br>
<br>

# For Developers
<details id="Devs"> <!-- <details id="Devs" open> to open on init -->
<summary> <strong>Toggle</strong> </summary>

Project Organization
------------
Read: [CookieCutter DataSci](https://drivendata.github.io/cookiecutter-data-science)

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.   (post pdbfixer)
    │   ├── processed      <- The final, canonical data sets for modeling.   (idk yet)
    │   └── raw            <- The original, immutable data dump.    (OG .pdb's etc.)
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.     (contains tests + working toward colab compatability)
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   ├── download_raw.py     (download and maintain SKEMPI 2 & ZEMu)
    │   │   └── make_dataset.py     (parsing, formatting, sorting dataset)
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py    (need to see example for clarification)
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org

## Built With
too lazy to link them atm...
 - OpenMM
 - pdbfixer
 - Python Network X library
 - etc.

## Contributing
Please read [CONTRIBUTING.md](https://github.com/tcardlab/optimus_bind_sample/blob/develop/CONTRIBUTING.md) for details on getting set up and contributing code.

**Collaboration kit:** 
 - Dev Space:  [Quora](https://www.quora.com/q/hxbiokqurmxybuec) open for Q&A and Announcements
 - Chat room:  [Slack](https://bioscienceclub.slack.com/messages/CHK7D10MN/details/) by request
 - Ref. library:  [F1000Workspace](https://f1000.com/work/#/items/6730972/detail?collection=321381) by request
 - Repository:  [GitHub](https://github.com/tcardlab/optimus_bind_sample)
 - To-do list:     [Trello](https://trello.com/invite/b/V94BBx1d/4550ff50fe61eb27b8d304da57b00fe8/optimus-bind)

**Seeking people who are skilled in:**
 - Bioinformatics 
 - Molecular dynamics and force field development
 - Protein engineering and protein design 
 - Protein Folding and biophysics (computational or experimental) for insight into force field design
 - Basic graph theory and the Python Network X library 
 - Machine learning, particularly on small datasets 
 - Server and website design

</details>

## Citations

 1. "SKEMPI 2.0: An updated benchmark of changes in protein-protein binding energy, kinetics and thermodynamics upon mutation".  Justina Jankauskaitė, Brian Jiménez-García, Justas Dapkūnas, Juan Fernández-Recio, Iain H Moal  _**Bioinformatics**_ (2018), bty635, [https://doi.org/10.1093/bioinformatics/bty635](https://doi.org/10.1093/bioinformatics/bty635)
 2. "etc" et al.

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYxMjgyNDQzNywxMTUwMzIyMzQ4LC0xMD
Q5NTAyNTc3LC0xNTE3NjUxNDY3LDI2NzU0NTEzMSwtMjAwMTEw
NTU3NiwxNDc3ODM5NjI2LC0xMzI1NTU5NTY1LDIwNDIwMDcwNz
gsLTk0OTMwODAwOCwxNDI0NzE0OTIwLDE5MjQ0MzIxMzYsLTc5
MzYzNDU2NSwyMDY4OTkyNjcyLC01Nzg0NDY4NywyOTgzNjU3Mj
AsLTE4OTkwMTAyMzAsOTU3ODY5NDI3LDY2MzYwMjkxNiwxMDc3
NDEwMjM4XX0=
-->
