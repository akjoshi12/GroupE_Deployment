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

# Errors
![image](https://github.com/user-attachments/assets/5cebd1ef-8f1d-430c-9a37-ea5bc50b219f) 
![image](https://github.com/user-attachments/assets/9bbaaf82-f6ca-4694-a53f-2aa33f946f3a)



### Issue with credential
![image](https://github.com/user-attachments/assets/e616da79-ce48-493f-bfa5-838668667846)

![image](https://github.com/user-attachments/assets/734dfa95-89ad-4d85-beb6-ffa2219fe625)



### Running Playbook

![image](https://github.com/user-attachments/assets/5b2a6d52-4e43-4ca4-b0b2-a75819ca36b9)

### Super User Permission
![image](https://github.com/user-attachments/assets/58321fed-83ab-46f2-9ed9-b221fba91a60)


### Module issue 
![image](https://github.com/user-attachments/assets/fc610499-aeb9-4f0a-813e-049b399899eb)




## Application V
![image](https://github.com/user-attachments/assets/568d6fa8-1cf9-4429-bda9-6ef467e31d45) 
## Final Live Demo

https://sentiment-nxrfibmeyktq4mjfsm4usw.streamlit.app/ 


