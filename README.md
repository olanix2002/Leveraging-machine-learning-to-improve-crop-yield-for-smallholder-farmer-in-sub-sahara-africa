# Leveraging Machine Learning to Improve Crop Yield for Smallholder Farmers in Sub-Saharan Africa

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Crop Selection](#crop-selection)
- [Country Selection](#country-selection)
- [Machine Learning Models](#machine-learning-models)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to leverage machine learning techniques to improve crop yield for smallholder farmers in Sub-Saharan Africa. The project utilizes data from the Food and Agriculture Organization (FAO) and the World Bank to build predictive models that can help optimize agricultural practices and increase crop production for the selected crops in the chosen countries.

## Project Overview

Agriculture plays a vital role in the economies of many Sub-Saharan African countries, and smallholder farmers form the backbone of the agricultural sector. However, they often face challenges such as limited access to advanced agricultural technologies and resources, unpredictable weather patterns, and inefficient farming practices, which can lead to suboptimal crop yields.

This project aims to address these challenges by developing machine learning models that can analyze historical crop yield data, weather patterns, soil characteristics, and other relevant factors to provide insights and recommendations for optimizing crop production.

## Dataset

The dataset used in this project was obtained from the Food and Agriculture Organization (FAO) and the World Bank. It includes historical crop yield data, weather data, soil information, and other relevant agricultural indicators for the selected countries.

## Crop Selection

The following crops have been considered for analysis in this project:

1. Maize
2. Rice
3. Tomatoes
4. Potatoes
5. Seed cotton
6. Wheat
7. Soya beans
8. Coffee
9. Cocoa beans
10. Yams
11. Bananas

These crops were chosen based on their significance in the agricultural practices of Sub-Saharan African countries and their potential impact on food security and economic growth.

## Country Selection

The project focuses on the following countries in Sub-Saharan Africa:

1. South Africa
2. Nigeria
3. Kenya
4. Ethiopia
5. Mozambique
6. Tanzania
7. Ghana
8. Angola
9. Congo
10. Uganda

These countries were selected based on their agricultural importance, diverse agro-climatic conditions, and availability of relevant data.

## Machine Learning Models

To improve crop yield predictions, various machine learning models were employed and their performance evaluated. The following algorithms were explored:

- Linear Regression
- Lasso
- Ridge
- K-Neighbors Regressor
- Decision Tree
- Random Forest Regressor
- XGBRegressor
- CatBoosting Regressor
- AdaBoost Regressor

The models were trained using historical crop yield data and other relevant features from the dataset. Hyperparameter tuning and cross-validation techniques were employed to ensure robust and accurate predictions.

## Usage

To run this project locally, please follow these steps:

1. Clone the repository from [GitHub Repo URL].
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Execute the main script to train the machine learning models and generate predictions.

## Results

The performance of each machine learning model was evaluated using cross-validation R2 scores, which measure the goodness-of-fit of the models. Here are the results:


Based on the R2 scores obtained, we can see that the best performing model is CatBoostRegressor, with a mean R2 score of 0.78 and a relatively low standard deviation of 0.19. XGBRegressor also performed well with a mean R2 score of 0.70. K-Neighbors Regressor and Random Forest Regressor also performed relatively well with mean R2 scores of 0.64 and 0.69 respectively.

On the other hand, Linear Regression, Lasso, and Ridge performed poorly with negative mean R2 scores and high standard deviations of R2 scores.

## Contributing

Contributions to this project are welcome! If you want to contribute, please fork the repository and create a pull request, outlining the changes you propose to make. Your contributions will be reviewed and merged if they align with the project's objectives.

## License

This project is licensed under the [Apache License]. Feel free to use, modify, and distribute this code as per the terms of the license.
