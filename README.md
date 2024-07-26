# YouStock.AI

## Introduction
Welcome to YouStock.AI, an advanced AI-powered personal assistant designed to help investors analyze the stock market and make informed investment decisions. Developed by the Harbinger of Trades team for the Hack2Skill 'HumanAIze Hackathon FinTech Edition', YouStock leverages cutting-edge AI technologies to offer a comprehensive suite of features, including public opinion analysis, risk assessment, stress testing, and automated investment strategies. By integrating a feedback mechanism, YouStock continuously improves its reinforcement learning models, ensuring increasingly accurate predictions and investment strategies.

## Table of Contents
- [Introduction](#introduction)
- [How to Access the Files](#how-to-access-the-files)
- [Development Phase](#development-phase)
- [Dataset Information](#dataset-information)
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)

## How to Access the Files 
The project files are organized in a streamlined manner, allowing for easy navigation and access. We use Streamlit for the user interface, making it simple for users to interact with the application and access various functionalities. To get started with YouStock.AI, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Ankur2606/Algo-Trading-Youstock.git
    cd Algo-Trading-Youstock
    ```

2. **Create a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Setup GCP API Key**

    Place your GCP API key JSON file in the `Streamlit_app` directory and name it `tts_pdf_reader_key.json`.

5. **Add GCP API Key Path to the Code**

    Navigate to `Streamlit_app/youStocks.py` and add the following line to set the GCP API key JSON file path:

    ```python
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Streamlit_app/tts_pdf_reader_key.json"
    ```

6. Launch the Streamlit application:
   ```bash
   streamlit run Streamlit_app/youStocks.py
   ```

7. Access the application through your web browser at `http://localhost:8501`.


For more detailed information, refer to the documentation within the repository. Happy investing!



## Streamlit UI Sample Images:

![app_ss_001](https://github.com/user-attachments/assets/20912536-0bcb-4c5e-9113-fd15cf0532d2)
![app_ss_002](https://github.com/user-attachments/assets/f40afa83-8373-4c24-b5b7-0ff9c08af0b3)
![app_ss_003](https://github.com/user-attachments/assets/c50a2cf8-e83b-4f4e-aeed-3d6a262cad87)
![app_ss_004](https://github.com/user-attachments/assets/4df4fe36-dad5-4515-a292-1cc3f9e73663)
![app_ss_005](https://github.com/user-attachments/assets/ee0c39fb-12ad-44e5-9f91-bb6b09261fde)
![app_ss_006](https://github.com/user-attachments/assets/e6b51385-6606-45d0-9f63-1c3584fde606)
![app_ss_007](https://github.com/user-attachments/assets/9c3f5e27-7e5c-4a4c-aa44-759eff3995b4)
![app_ss_008](https://github.com/user-attachments/assets/657ffd40-239c-45bc-9d3e-89d77ae96a8e)
![app_ss_009](https://github.com/user-attachments/assets/4807bd85-a36a-4d6c-8272-38b92a17e776)


## UI Demo Video:
[![image](https://github.com/user-attachments/assets/be1c6cd2-ba13-45ac-9600-c5a387e8061e)
](https://www.youtube.com/watch?v=k9dXR4if8Zs)

Demo video link: [Click here!](https://www.youtube.com/watch?v=k9dXR4if8Zs)


## Project Overview

YouStock.AI stands out from other stock platforms by leveraging advanced AI technologies, including Generative AI and Natural Language Processing (NLP), to provide real-time, comprehensive sentiment analysis and sophisticated risk assessment. It offers personalized, automated investment strategies through AI-driven algorithmic trading and continuously improves its predictive accuracy via reinforcement learning and user feedback. Unique integrations with YouData.ai ensure continuous innovation and a balanced combination of AI insights with human expertise, providing users with a more intelligent, adaptive, and user-centric investment experience.

## Project Components

### 1. Algorithmic Trading Strategy (Strategy 1)

#### Focus Area: Banking Sector Analysis

**Metrics Considered:**
- Higher Net Interest Margin (NIM)
- Lower Non-Performing Assets (NPA)
- Pricing and Earnings Analysis (P/E Ratio and P/B Ratio)

### 2. Multifactor Market Dynamics (Strategy 2)

#### Collaborative Approach and Digitalization Analysis:

- Evaluate collaborations in diverse sectors (e.g., tech-automotive, pharma-tech).
- Analyze the impact of digitalization on banking stocks, including fintech collaborations and blockchain integration.

#### Micro and Macro Economics:

- Explore microeconomic factors (individual markets) and macroeconomic factors (national-level markets).
- Assess the influence of government policies and global economic interdependencies.

### 3. NLP - Sentiment Analysis (Strategy 2)

**Motivation:**
Combine Fundamental and Technical Analysis with sentiment analysis to enhance stock selection.

**Data Collection:**
- Scraping articles from sources like the Economic Times.
- Extracting features such as article date, headline, summary, and URL.

**NLP Techniques:**
- Preprocessing techniques (lemmatization, etc.).
- Sentiment analysis to classify news articles as positive or negative.

### 4. Quarterly Earnings Analysis (Strategy 2)

**Process:**
- Monitor and analyze quarterly earnings reports for insights.
- Adjust strategy based on emerging trends in individual companies.
- Backtest the strategy using historical data.
- Assess performance under various market conditions.

### 5. Personalized Investment Insights (Strategy 3)

**User-Centric Approach:**
- Collect user preferences for investment range, duration, and sectors of interest.
- Validate user inputs and retrieve historical stock data for a predefined list of banks.
- Utilize the Prophet time-series forecasting model to predict future stock prices.
- Rank stocks based on predicted profits and present results to the user.
- Integrate with a language model to generate personalized investment recommendations.

## Technologies Used

- **Data Visualization:**
  - `matplotlib`
  - `plotly`

- **Web App Development:**
  - `streamlit`
  - `streamlit_option_menu`

- **Data Manipulation:**
  - `pandas`
  - `numpy`

- **Time Series Forecasting:**
  - `prophet`

- **Financial Data Retrieval:**
  - `yfinance`

- **Web Scraping and API Requests:**
  - `requests`
  - `beautifulsoup4`

- **Natural Language Processing (NLP):**
  - `transformers`
  - `bs4`

- **Miscellaneous:**
  - `replicate`
  - `random`
  - `cufflinks`


## Development Phase
The development of YouStock.AI follows an iterative process, with continuous integration and continuous deployment (CI/CD) practices ensuring robust and seamless updates. The phases include:

1. **Initial Setup and Data Collection:** Setting up the environment and gathering data from APIs like Alpha Vantage and Twitter API.
2. **Data Processing and Analysis:** Utilizing Hadoop and Spark for big data processing, and performing sentiment analysis with spaCy, NLTK, and APIs like Google NLP and IBM Watson.
3. **Model Development:** Developing machine learning models using TensorFlow and PyTorch, and implementing time series analysis with stats models and Prophet.
4. **Risk Assessment and Stress Testing:** Conducting risk assessments and stress testing using PowerBi, MATLAB, and Monte Carlo simulations.
5. **Automated Trading and Decision Support:** Integrating automated trading platforms like MetaTrader and NinjaTrader, and developing custom decision support systems.
6. **Continuous Improvement:** Implementing CI/CD with Jenkins and GitLab, and monitoring performance with Splunk and New Relic.

## Dataset Information
YouStock.AI utilizes datasets sourced from various reliable providers via APIs such as Alpha Vantage and Twitter API. Additionally, YouData.ai is used to enrich the datasets with high-quality, relevant financial data. This enables comprehensive analysis and more accurate predictive modelling.

![Dataset ScreenShot](https://github.com/user-attachments/assets/f0f7d5a5-b66c-47c0-8623-b071d64525c6)

[Database link here at YouData.AI](https://datalink.youdata.ai/yc597789)


---

*Harbinger of Trades Team*
