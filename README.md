# Group E: Customer Feedback Sentiment Analysis

## Project Overview

This project is part of the Retail Industry Project module, where the objective is to develop an AI system that analyzes customer feedback (such as reviews and comments) to determine sentiment (positive, negative, neutral). The system aims to provide insights into customer satisfaction and identify areas for improvement in products and services. By leveraging Natural Language Processing (NLP) and machine learning models, the project delivers actionable insights to enhance the retail experience.

## Setup Instructions

### 1. Prerequisites
- Python (version 3.8 or later)
- Libraries: `pandas`, `matplotlib`, `scikit-learn`, `nltk`, `wordcloud`, `sqlalchemy`
- Jenkins for continuous integration setup.
- Ansible for automated deployment.
- MySQL for database management.
- GitHub for version control and collaboration.


## 2. Setup Environment
- Clone the repository:
- bash
- Copy code
- git clone https://github.com/GroupE/Sentiment-Analysis.git
- Create a virtual environment and install dependencies:
- bash
- Copy code
- python -m venv env
- source env/bin/activate  # On Windows use `env\Scripts\activate`pip install -r requirements.txt
- Set up a virtual environment and install dependencies:
  - `python -m venv env`
  - `source env/bin/activate` (On Windows use `env\Scripts\activate`)
  - `pip install -r requirements.txt`

## 3. Set up the MySQL database:
  - Create the database schema using the provided SQL file in the Data folder.
  - Configure your database credentials in `config.py`.

- Running the Project:
  - Data Preprocessing: Run the preprocessing script to clean and prepare the dataset:
    - `python source/data_preprocessing.py`
  - Model Development: Train the sentiment analysis model:
    - `python source/model_training.py`
  - Deployment: Use Ansible playbooks located in the Deployment folder to automate deployment:
    - `ansible-playbook -i hosts.ini deploy.yml`

- Notes for Contributors:
  - Follow the branching model (main, development, and feature branches) as specified in the GitHub repository.
  - Write test cases for each new feature using PyTest and add them to the Tests folder.
  - Update the README.md and documentation files with any new changes or setup requirements.

 ## 4. Folder Structure Explanation:
  - **Documentation**:
    - Requirements document detailing the goals and objectives of the sentiment analysis project.
    - Design specifications explaining the architecture, model choices, and processing pipeline.
    - Project plan with milestones and timelines visualized using Gantt charts.
  - **Data**:
    - Raw dataset: `amazon_uk_shoes_reviews.csv`.
    - Processed dataset: `cleaned_reviews.csv`.
  - **Source**:
    - `data_preprocessing.py`: Script for cleaning and labeling the dataset.
    - `model_training.py`: Script for building and training the sentiment analysis model.
    - Other helper scripts for visualization, evaluation, and deployment.
  - **Deployment**:
    - Ansible playbooks and Jenkins configuration files for managing testing, staging, and production environments.
  - **README**:
    - Provides a comprehensive guide on the project, including setup instructions,

### Current status
### Creating an Ansible
![image](https://github.com/user-attachments/assets/7a3e1adb-2431-4fda-9d3a-819a68b4b6ff)

### Creating a Playbook
![image](https://github.com/user-attachments/assets/36498436-9817-4b0e-a683-4a42f1452c70)

### Running Playbook

![image](https://github.com/user-attachments/assets/7c14154d-9715-4bf3-9d35-51e14ed80edd)



## Application Video (Local)

https://www.youtube.com/watch?v=o0bNkMqTJZk&ab_channel=JoshiAtri 
