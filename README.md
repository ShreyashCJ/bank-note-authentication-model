# BankNote Authentication

This project implements a machine learning model to authenticate banknotes. The main goal of this project is to accurately classify whether a banknote is genuine or counterfeit based on specific features extracted from the banknote images.

## Project Description

This project focuses on developing a robust model to distinguish between genuine and counterfeit banknotes using a Random Forest classifier. By leveraging various statistical features of banknote images, the model aims to provide a reliable solution for banknote authentication.

- **What the application does**: It classifies banknotes as genuine or counterfeit based on input features.
- **Why these technologies were used**: The Random Forest classifier was chosen for its accuracy and ability to handle complex data without requiring extensive feature scaling.
- **Challenges faced**: Some challenges included feature selection and ensuring the model generalized well on unseen data. Future features might include enhancing the model with additional image processing techniques and expanding the dataset.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Data](#data)
5. [Model](#model)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

## Installation

To run this project, you'll need to have Python installed along with several packages. You can install the required packages using the following command:

```bash
pip install pandas numpy scikit-learn fastapi uvicorn
```
## Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```
## Run the FastAPI application:

Ensure your dataset BankNote_Authentication.csv is in the project directory, then run:
```bash
uvicorn app:app --reload
```

This will start the FastAPI server, and you can make API requests to classify banknotes.

## Make a prediction:
You can use a tool like Postman or cURL to make POST requests to the FastAPI server. Example request:
```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{
  "variance": 2,
  "skewness": 3,
  "curtosis": 2,
  "entropy": 1
}'
```

## Project Structure
```bash
.
├── BankNote_Authentication.csv   # Dataset file
├── README.md                     # Project documentation
├── app.py                        # FastAPI application script
├── BankNotes.py                  # BankNote dataclass definition
├── classifier.pkl                # Serialized model file
└── .gitignore                    # Git ignore file
```

## Data
The dataset used for this project is BankNote_Authentication.csv, which contains features extracted from images of genuine and counterfeit banknotes.
```bash
variance: Variance of Wavelet Transformed image
skewness: Skewness of Wavelet Transformed image
curtosis: Curtosis of Wavelet Transformed image
entropy: Entropy of image
```
## Model
A Random Forest classifier is used for this project. The model is trained using the scikit-learn library and serialized for later use in predictions.

## Results
The performance of the model can be evaluated using the accuracy score. After training, the model achieves a satisfactory level of accuracy on the test set.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request to contribute.

## Fork the Project
```bash

Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
```

## License
Distributed under the MIT License. See LICENSE for more information.


