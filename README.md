# Multiple Disease Prediction

[![Language](https://img.shields.io/badge/language-Jupyter%20Notebook%20%7C%20Python-blue)](https://github.com/singhnavneet77/Multiple_Disease_Prediction)

## Description

Multiple Disease Prediction is a machine learning project designed to predict the likelihood of various diseases based on user input data. The project leverages multiple datasets and algorithms to provide an easy-to-use interface for disease risk assessment. It features both interactive Jupyter Notebooks and a user-friendly Streamlit web application for real-time predictions.

---

## Table of Contents

- [Features](#features)
- [Project Preview](#project-preview)
- [Tools and Technologies Used](#tools-and-technologies-used)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Future Scope](#future-scope)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Predicts risk for multiple diseases using input parameters.
- Interactive Jupyter Notebook interface for demonstration and experimentation.
- Streamlit web app for user-friendly, real-time predictions.
- Utilizes various machine learning algorithms for classification.
- Modular and extendable codebase for adding more diseases or ML models.

---

## Project Preview

Below are screenshots of the Streamlit web interface showing how the project allows users to select a disease and enter the required parameters for prediction.

**Heart Disease Prediction Interface**
![image1](image1)

**Kidney Disease Prediction Interface**
![image2](image2)

---

## Tools and Technologies Used

- **Jupyter Notebook:** Interactive computational environment for development and demonstration.
- **Python:** Core programming language.
- **Pandas:** Data manipulation and preprocessing.
- **NumPy:** Numerical computations.
- **scikit-learn:** Machine learning models and utilities.
- **Matplotlib / Seaborn:** Data visualization (if used in notebooks).
- **Streamlit:** Web application framework for deploying ML models with a simple UI.

---

## Installation

### Prerequisites

- Python (>=3.7 recommended)
- `pip` package manager

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/singhnavneet77/Multiple_Disease_Prediction.git
   cd Multiple_Disease_Prediction
   ```

2. **(Recommended) Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   > If `requirements.txt` is not present, manually install the following (or as per notebook and app imports):

   ```bash
   pip install jupyter pandas numpy scikit-learn matplotlib seaborn streamlit
   ```

---

## How to Use

### Using the Streamlit Web App

1. **Start the Streamlit app:**

   ```bash
   streamlit run app.py
   ```
   > Replace `app.py` with the actual Streamlit app filename if different.

2. **Navigate to the web page that opens in your browser.**

3. **Select the type of disease prediction you want (Heart Disease or Kidney Disease) from the sidebar.**

4. **Enter the required medical parameters in the provided fields.**

   - Example interfaces are shown in the screenshots above:
     - Heart Disease Prediction: Input fields such as age, blood pressure, cholesterol, etc. ![image1](image1)
     - Kidney Disease Prediction: Input fields such as blood pressure, specific gravity, albumin, etc. ![image2](image2)

5. **Click the respective button to get the prediction result.**

### Using Jupyter Notebooks

1. **Launch Jupyter Notebook:**

   ```bash
   jupyter notebook
   ```

2. **Open the main `.ipynb` notebook file.**
3. **Follow the instructions in the notebook to load data, train models, and make predictions.**

---

## Project Structure

```
Multiple_Disease_Prediction/
│
├── data/                # Datasets for various diseases (CSV files)
├── notebooks/           # Jupyter Notebooks with model code and analysis
├── src/                 # (If present) Source code for modular pipeline
├── app.py               # Streamlit web application (or similar)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── ...                  # Other files
```

---

## Future Scope

- **Enhanced Web Application:** Add authentication, history tracking, or additional visualization to the Streamlit app.
- **Mobile App Integration:** Implement a mobile app for real-time predictions.
- **Deep Learning Models:** Integrate advanced models for improved accuracy.
- **Expanded Dataset:** Incorporate more datasets covering additional diseases.
- **Explainable AI:** Add model interpretability features for user trust.
- **Automated Data Collection:** Integrate APIs for live data fetching.
- **Deployment:** Containerization with Docker and deployment to cloud platforms.

---

## Contributing

Pull requests and contributions are welcome! Please fork the repository and submit a PR.

---

## License

This project is licensed under the [MIT License](LICENSE).
