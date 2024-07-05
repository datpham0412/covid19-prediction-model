# 🦠 Covid 19 Prediction Model

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/datpham0412/Covid19_Prediction_Model/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/datpham0412/Covid19_Prediction_Model)](https://github.com/datpham0412/Covid19_Prediction_Model/issues)
[![GitHub stars](https://img.shields.io/github/stars/datpham0412/Covid19_Prediction_Model)](https://github.com/datpham0412/Covid19_Prediction_Model/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/datpham0412/Covid19_Prediction_Model)](https://github.com/datpham0412/Covid19_Prediction_Model/network/members)

## 📋 Project Description

The **Covid 19 Prediction Model** is a comprehensive tool designed to predict the spread and impact of Covid-19 using historical data and advanced statistical techniques. The model leverages multiple data sources, including Covid-19 case data and mobility data, to provide accurate forecasts and insights into the pandemic's trends. The project aims to assist policymakers, healthcare professionals, and the general public in understanding and responding to the ongoing Covid-19 crisis.

## 🛠 Technologies Used

<p align="left">
<a href="
https://www.python.org/downloads"
target="_blank" rel="noreferrer">
<img src="
https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"
alt="python" width="40" height="40"/>
</a>
<a href="
https://www.w3schools.com/cpp/"
target="_blank" rel="noreferrer">
<img src="
https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg"
alt="cplusplus" width="40" height="40"/>
</a>
<a href="
https://www.sqlite.org/download.html"
target="_blank" rel="noreferrer">
<img src="
https://upload.wikimedia.org/wikipedia/commons/9/97/Sqlite-square-icon.svg"
alt="sqlite" width="40" height="40"/>
</a>
<a href="
https://pandas.pydata.org/"
target="_blank" rel="noreferrer">
<img src="
https://miro.medium.com/v2/resize:fit:640/format:webp/1*uyUj__HJekKIkx58kMxlcA.png"
alt="pandas" width="40" height="40"/>
</a>
<a href="
https://scikit-learn.org/stable/"
target="_blank" rel="noreferrer">
<img src="
https://avatars.githubusercontent.com/u/17349883?s=200&v=4"
alt="scikit-learn" width="40" height="40"/>
</a>
<a href="
https://matplotlib.org/"
target="_blank" rel="noreferrer">
<img src="
https://cdn.phidgets.com/education/wp-content/uploads/2021/04/Matplotlib_icon.png"
alt="matplotlib" width="40" height="40"/>
</a>
<a href="
https://seaborn.pydata.org/"
target="_blank" rel="noreferrer">
<img src="
https://cdn.worldvectorlogo.com/logos/seaborn-1.svg"
alt="seaborn" width="40" height="40"/>
</a>
<a href="
https://cmake.org/"
target="_blank" rel="noreferrer">
<img src="
https://upload.wikimedia.org/wikipedia/commons/1/13/Cmake.svg"
alt="cmake" width="40" height="40"/>
</a>
<a href="
https://github.com/google/googletest"
target="_blank" rel="noreferrer">
<img src="
https://banner2.cleanpng.com/20180423/gkw/kisspng-google-logo-logo-logo-5ade7dc753b015.9317679115245306313428.jpg"
alt="google-test" width="40" height="40"/>
</a>
<a href="
https://pypi.org/project/dill/"
target="_blank" rel="noreferrer">
<img src="
https://dill.readthedocs.io/en/latest/_static/pathos.png"
alt="dill" width="40" height="40"/>
</a>
<a href="
https://jupyter.org/"
target="_blank" rel="noreferrer">
<img src="
https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg"
alt="jupyter-notebook" width="40" height="40"/>
</a>
</p>
- **Python**: Core programming language for data processing and model training.
- **C++**: For efficient data processing and handling large datasets.
- **SQLite**: Database management for storing and querying data.
- **Pandas**: Data manipulation and analysis.
- **Scikit-learn**: Machine learning library for building predictive models.
- **Matplotlib & Seaborn**: Data visualization.
- **CMake**: Cross-platform build system.
- **Google Test**: Unit testing framework for C++.
- **Dill**: For model serialization in Python.
- **Jupyter Notebook**: For interactive data analysis and visualization.

## 📚 Features

- Fetch and preprocess Covid-19 and mobility data from multiple sources.
- Integrate and clean data, ensuring consistency and accuracy.
- Create various date-based, lag, and rolling average features to enhance model performance.
- Train and evaluate machine learning models to predict new Covid-19 cases.
- Visualize actual vs. predicted cases, residuals, and other key metrics to interpret model performance.
- Generate detailed reports and visualizations for data exploration and model results.
- Support for user-defined country data extraction and analysis.

## 🚀 Installation and Running the Project

### Prerequisites

- Ensure you have `git` installed for cloning repositories.
- Ensure you have CMake installed and added to your system's PATH.

### Steps

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/yourusername/Covid19_Prediction_Model.git
   cd Covid19_Prediction_Model
   ```

2. **Install CMake**:

   - Download CMake from [here](https://github.com/Kitware/CMake/releases/download/v3.30.0-rc3/cmake-3.30.0-rc3-windows-x86_64.msi)
   - Add the CMake binary path (e.g., `C:\Program Files\CMake\bin`) to your environment variables.

3. **Clone SQLiteCpp**:

   ```sh
   cd external
   git clone https://github.com/SRombauts/SQLiteCpp.git
   ```

4. **Modify SQLiteCpp CMakeLists.txt**:

   - Open `CMakeLists.txt` in the `external/SQLiteCpp` folder.
   - Change line 388 from:
     ```cmake
     option(SQLITECPP_RUN_CPPLINT "Run cpplint.py tool for Google C++ StyleGuide." ON)
     ```
     to:
     ```cmake
     option(SQLITECPP_RUN_CPPLINT "Run cpplint.py tool for Google C++ StyleGuide." OFF)
     ```

5. **Build the Project**:

   ```sh
   cd ..
   mkdir build
   cd build
   cmake ..
   cmake --build . --config Release
   ```

6. **Run the Application**:
   ```sh
   cd Release
   Covid19_Prediction.exe
   ```

### Python Dependencies

Install the required Python libraries:

```sh
pip install pandas numpy scikit-learn sqlite3 matplotlib seaborn dill joblib notebook
```

## Running the scripts

1. **Fetch Data**

```sh
python scripts/fetch_data.py
```

This script fetches COVID-19 and mobility data. Note that this may take up to 10-20 minutes.

2. **Migrate Data**

```sh
python scripts/migrate_data.py
```

This script migrates COVID-19 and mobility data for a specified country from the raw datasets to processed CSV files.

3. **Build the project**

```sh
cd ..
mkdir build
cd build
cmake ..
cmake --build . --config Release
cd Release
Covid19_Prediction.exe
```

Follow these steps to configure, build, and run the C++ project.

4. **Process Data**

```sh
python scripts/data_processing.py
```

This script processes the COVID-19 and mobility data for a specific country provided by the user.

5. **Perform EDA**

```sh
python scripts/eda_visualization.py
```

This script performs Exploratory Data Analysis on the processed data.

6. **Feature Engineering**

```sh
python scripts/feature_engineering.py
```

This script performs feature engineering on the processed data.

7. **Split Data**

```sh
python scripts/split_data.py
```

This script splits the data into training and testing sets.

8. **Model Training**

```sh
python scripts/model_training.py
```

This script trains the machine learning model.

9. **Model Evaluation**

```sh
python scripts/model_evaluation.py
```

This script evaluates the performance of the trained model.

10. **Interpret Predictions**

```sh
cd notebooks
jupyter notebook
```

Open interpret_predictions.ipynb in Jupyter Notebook to visualize and interpret the model's predictions.

## 📷 Screenshots

![CorrelationHeatMatrix](https://github.com/datpham0412/Covid19_Prediction_Model/assets/100574389/0f403266-8b3d-4c3c-ab27-28e8f5963ce1)
![JupyterNotebook2](https://github.com/datpham0412/Covid19_Prediction_Model/assets/100574389/da923b42-92c2-493f-84c4-c6d08ffae03d)
![NewCases_NewDeathsOverTime](https://github.com/datpham0412/Covid19_Prediction_Model/assets/100574389/a51787f3-ef7f-4366-8849-ec641186a30e)
![CorrelationScatterPlot](https://github.com/datpham0412/Covid19_Prediction_Model/assets/100574389/3f1631c3-b8dc-4c8e-8732-92c6166ac63c)
![DistributionNewCases](https://github.com/datpham0412/Covid19_Prediction_Model/assets/100574389/59cddbbc-ca2c-4050-9b85-bd045380cac9)
![JupyterNotebook1](https://github.com/datpham0412/Covid19_Prediction_Model/assets/100574389/dc8a5a02-ab51-4044-98dc-4f17bd901111)
![JupyterNotebook2](https://github.com/datpham0412/Covid19_Prediction_Model/assets/100574389/49d71df3-e149-4238-919c-c7791d5420f3)
![JupyterNotebook3](https://github.com/datpham0412/Covid19_Prediction_Model/assets/100574389/b1db4032-039b-49c5-b804-4a8a780bcca4)
![JupyterNotebook4](https://github.com/datpham0412/Covid19_Prediction_Model/assets/100574389/787fbf82-9a6e-430c-83b7-e474e8af2eff)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/datpham0412/Covid19_Prediction_Model/blob/main/LICENSE)) file for details.

## 📞 Contact

## For any inquiries, please contact [tiendat041202@gmail.com](mailto:tiendat041202@gmail.com).

Made with ❤️ by [Dat Pham](https://github.com/datpham0412)
