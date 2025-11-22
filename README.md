#  Izmir House Price Prediction Application

This project is a machine learning-based web application designed to predict house prices in **Izmir, Turkey**. 

The application is the final product of an end-to-end data science pipeline, starting from raw data collection via **web scraping**, followed by extensive **data analysis**, and culminating in a **predictive model** deployed with Streamlit.



##  Live Demo
You can try the application directly in your browser without any installation:
 **[Click here to open the App](https://4wavnkvjv6jkyg6twbbyfc.streamlit.app)**

---

##  Project Pipeline

The development process consisted of four main stages:

1.  **Web Scraping:** Real estate data (prices, square meters, location, building age, etc.) was scraped from major Turkish real estate platforms.
2.  **Data Preprocessing & EDA:** The raw data was cleaned, missing values were handled, and Exploratory Data Analysis (EDA) was performed to understand price distributions across different districts of Izmir.
3.  **Model Building:** Various regression algorithms were tested. An optimized pipeline using **XGBoost/Scikit-learn** was created to achieve the best accuracy.
4.  **Deployment:** The final model was wrapped in a user-friendly **Streamlit** interface, allowing users to input property details and get instant price estimates.

##  Tech Stack

* **Python:** Core programming language.
* **Streamlit:** For creating the interactive web interface.
* **Scikit-Learn & XGBoost:** For machine learning modeling.
* **Pandas & NumPy:** For data manipulation and numerical operations.
* **BeautifulSoup/Selenium:** (Used in the preliminary phase) For web scraping.
* **Requests:** To fetch real-time location data (Districts/Neighborhoods) via API.

##  Features

* **Dynamic Location Selection:** Fetches up-to-date districts and neighborhoods of Izmir via API.
* **Detailed Parameters:** Input options for net area ($m^2$), building age, floor number, heating type, etc.
* **Instant Prediction:** Returns the estimated price immediately based on the trained ML model.

##  Local Installation

If you want to run this project on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ugurturkcan/Izmir_House_Price_Prediction_Application.git](https://github.com/ugurturkcan/Izmir_House_Price_Prediction_Application.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd Izmir_House_Price_Prediction_Application
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

---
*Developed by Uğur Türkcan*
