# Project Title: A/B Testing Analysis for Mobile Game Product Change and Fast Food Marketing Campaign

## Project Overview

This project involves analyzing A/B testing results for two distinct campaigns: one for a mobile game ("Cookie Cats") and another for a fast-food marketing promotion. Using two Jupyter Notebooks, the analysis explores the effectiveness of different strategies in each case. Additionally, a Looker Studio dashboard visualizes key metrics, accessible through a link provided in the first notebook and listed below.

## Objectives

This project aims to conduct a comprehensive analysis of two A/B testing scenarios to evaluate the effectiveness of different product change / marketing strategies, with a focus on measuring user behavior and sales impact. The objectives of the project are as follows:

***1. Assess the Effect of Changes in a Mobile Game App (Cookie Cats)***
- Conduct an A/B test analysis on user engagement and behavior in a mobile game application.
- Determine the impact of specific game changes on user retention and engagement metrics.
- Compare the analytical and bootstrapped confidence intervall on a A/B test metric.

***2. Evaluate the Impact of a Marketing Campaign in a Fast-Food Chain***
- Analyze the effectiveness of a marketing campaign on the sales of a new item in a fast-food chain.
- Compare sales metrics across different promotional strategies to identify the most successful approach.
- Visualize Key Insights through a Looker Studio Dashboard.
 
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Custom Modules](#custom-modules)
- [Data](#data)
- [Directory Structure](#directory-structure)
- [Requirements](#requirements)
- [Notebooks Overview](#notebooks-overview)
- [Dashboard](#dashboard)

## Installation

To set up this project locally, please follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/razzf/mobile-game-data-analysis
   ```
2. **Navigate to the project directory**:
   ```bash
   cd jwerne-DS.v3.2.2.5
   ```
3. **Install the required packages**:
   Make sure you have Python installed. Install the packages listed in the `requirements.txt` file using:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

After installation, open the notebooks in Jupyter or JupyterLab to explore the analysis. You can execute each cell to walk through the data preparation, exploration, and statistical testing stages. Use the Looker Studio dashboard to gain quick insights into the overall trends and effectiveness of the Fast Food Marketing Campaign A/B Test Analysis.

## Custom Modules

This project includes custom Python modules located in the `custom_modules` directory. These modules contain reusable functions and utilities used throughout the analysis. Ensure you download this directory when cloning the repository.

You can import these modules into your notebook or scripts as follows:

```python
from custom_modules import module_name
```

Replace `module_name` with the specific module you want to use.

## Data

The datasets used in this analysis is available in the `data` subdirectory. It includes the necessary CSV files for running the analysis. Ensure that this directory is in the project root, as the notebook depends on relative paths to load the data. Originally both datasets were sourced from Kaggle [here](https://www.kaggle.com/datasets/mursideyarkin/mobile-games-ab-testing-cookie-cats) and [here](https://www.kaggle.com/datasets/chebotinaa/fast-food-marketing-campaign-ab-test).
 
## Directory Structure

The project structure is organized as follows:

```
project-root/
├── custom models/
    ├── bootstrapping.py                # custom module for bootstrapping
    └── plot_formatting.py              # custom module for plot formatting
├── data/
    ├── cookie_cats.csv                 # data for Cookie Cats A/B test analysis
    └── WA_Marketing-Campaign.csv       # data for fast-food marketing campaign analysis
├── notebooks/
    ├── Mobile Games AB Testing - Cookie Cats test analysis.ipynb  # Notebook for Cookie Cats A/B test analysis
    └── Fast Food Marketing Campaign_A-B test analysis.ipynb       # Notebook for fast-food marketing campaign analysis
├── README.md                           # Project overview and setup guide
└── requirements.txt                    # Package requirements file
```

## Requirements

All dependencies for running the notebooks are listed in `requirements.txt`. You can install these dependencies with the command provided above. 

## Notebooks Overview

### 1. Mobile Games A/B Testing - Cookie Cats Test Analysis

This notebook analyzes an A/B test conducted in a mobile game. The objective is to understand the effect of specific changes in the game on player retention.

#### Table of Contents (Notebook 1)
    1. Introduction
    2. Data Preparation
    3. Data Cleaning
    4. A/B Testing
    - 4.1. Mission/Goal Definition
    - 4.2. Metrics Definition
    - 4.3. Calculations
    - 4.4. Results and Decisions

### 2. Fast Food Marketing Campaign A/B Test Analysis

In this notebook, we evaluate the impact of a marketing campaign on sales in a fast-food chain. The analysis aims to identify which promotional strategies are most effective in boosting item sales.

#### Table of Contents (Notebook 2)
    1. Introduction
    2. Data Preparation
    3. Data Cleaning
    4. A/B Testing
    - 4.1. Mission/Goal Definition
    - 4.2. Metrics Definition
    - 4.3. Calculations
    - 4.4. Results and Decisions
    5. Dashboard
 
## Dashboard

The Looker Studio dashboard provides an interactive way to explore key metrics and trends identified in the Fast Food Marketing Campaign A/B Test Analysis. Access it [here](https://lookerstudio.google.com/reporting/2963e7f0-3892-40cc-a343-32ebf5ee1bdd) to visualize the main findings and observe data insights from a high-level perspective.

