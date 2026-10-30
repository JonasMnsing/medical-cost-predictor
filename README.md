# Health Insurance Risk & Pricing Model

## Description of the Problem
In the insurance industry, assessing risk and pricing premiums is critical to maintaining a sustainable business. Traditional manual underwriting can be time-consuming and relies heavily on actuarial tables that may miss complex, non-linear interactions between a person's lifestyle and health metrics.

The goal of this project is to build a simple **Underwriting Tool**. It uses machine learning to predict the expected medical costs (financial liability) of an individual based on their demographic and health data. By automating this cost prediction, risk managers can:
* Instantly quote premiums for new applicants.
* Identify high-risk profiles based on interacting factors.
* Streamline the approval process for low-risk applicants.

This project was developed as the midterm project for the [Machine Learning Zoomcamp 2026](https://courses.datatalks.club/ml-zoomcamp-2026/).

## Dataset
The model is trained on the [Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance) from Kaggle. It contains 1,338 records with the following features:
* `age`: Age of primary beneficiary
* `sex`: Insurance contractor gender (female, male)
* `bmi`: Body mass index 
* `children`: Number of children covered by health insurance / Number of dependents
* `smoker`: Smoking status
* `region`: the beneficiary's residential area in the US (northeast, southeast, southwest, northwest)
* `charges` (Target): Individual medical costs billed by health insurance

## Instructions on How to Run the Project
...

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
