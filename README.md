# Health Insurance Risk & Pricing Model

## Description of the Problem
In the insurance industry, assessing risk and pricing premiums is critical to maintaining a sustainable business. Traditional manual underwriting can be time-consuming and relies heavily on actuarial tables that may miss complex, non-linear interactions between a person's lifestyle and health metrics.

The goal of this project is to build a simple **Underwriting Tool**. It uses machine learning to predict the expected medical costs (financial liability) of an individual based on their demographic and health data. By automating this cost prediction, risk managers can:
- Instantly quote premiums for new applicants.
- Identify high-risk profiles based on interacting factors.
- Streamline the approval process for low-risk applicants.

This project was developed as the midterm project for the [Machine Learning Zoomcamp 2026](https://courses.datatalks.club/ml-zoomcamp-2026/).

## Dataset
The model is trained on the [Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance) from Kaggle. It contains 1,338 records with the following features:
- `age`: Age of primary beneficiary
- `sex`: Insurance contractor gender (female, male)
- `bmi`: Body mass index 
- `children`: Number of children covered by health insurance / Number of dependents
- `smoker`: Smoking status
- `region`: the beneficiary's residential area in the US (northeast, southeast, southwest, northwest)
- `charges` (Target): Individual medical costs billed by health insurance

## Instructions on How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/JonasMnsing/medical-cost-predictor.git
cd medical-cost-predictor
```

### 2. Environment Setup

This project uses `pipenv` for dependency management and virtual environment isolation.

1. Ensure you have `pipenv` installed:
    ```bash
    pip install pipenv
    ```
2. Install the required dependencies from the Pipfile.lock:
    ```bash
    pipenv install
    ```
3. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

### 3. Running the App locally (Docker)

To run the web service in an isolated Docker container, follow these steps:

1. Build the Docker image:
   Run this command in the directory containing the `Dockerfile`:
   ```bash
   docker build -t medical-cost-predictor .
   ```
2. Run the Docker container:
Map port 9696 of your local machine to port 9696 of the container:
```bash
docker run -it --rm -p 9696:9696 medical-cost-predictor
```
3. Test the API:
With the container running, open a new terminal and run your test script:
```bash
python test.py
```
