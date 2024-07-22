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

1. Clone the repository:
   ```bash
   git clone https://github.com/harbingeroftrades/YouStock.AI.git
   cd YouStock.AI
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the Streamlit application:
   ```bash
   streamlit run youstock.py
   ```
4. Access the application through your web browser at `http://localhost:8501`.


For more detailed information, refer to the documentation within the repository. Happy investing!



## Streamlit UI Sample Images:

![app_ss_001](<WhatsApp Image 2024-07-22 at 23.07.31_d1b40d9e.jpg>)
![app_ss_002](<WhatsApp Image 2024-07-22 at 23.08.06_38ca9a0e.jpg>)
![app_ss_003](<WhatsApp Image 2024-07-22 at 23.08.50_06e1d9ac.jpg>)
![app_ss_004](<WhatsApp Image 2024-07-22 at 23.09.28_e970067c.jpg>)
![app_ss_005](<WhatsApp Image 2024-07-22 at 23.10.12_497a260a.jpg>)
![app_ss_006](<WhatsApp Image 2024-07-22 at 23.10.37_7e0134c4.jpg>)
![app_ss_007](<WhatsApp Image 2024-07-22 at 23.11.36_e559053c.jpg>)
![app_ss_008](<WhatsApp Image 2024-07-22 at 23.13.23_d9cbf611.jpg>)
![app_ss_009](<WhatsApp Image 2024-07-22 at 23.13.58_34414e4d.jpg>)

## UI Demo Video:
<!-- [![Here is the DEMO Video](https://github.com/Karthick-ng/Real-Time-Market-Insights/assets/116434132/1f6d8395-96f0-4d7f-8efe-42e9336ede0d)]() -->


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


## Getting Started

1. Clone the repository.
   ```bash
   git clone [repository_url]
   
2. Move into project directory.
    ```bash
    cd Real-Time-Market-Insights
    cd Streamlit_app

3. Create a Virtual Environment and install Requirements.
    ```bash
    python -m venv venv
    venv\Scripts\activate  (on windows)
    source venv/bin/activate (on MAC)
  
    pip install -r requirements.txt

4. Run Streamlit code.
   ```bash
   streamlit run youstock.py


## Development Phase
The development of YouStock.AI follows an iterative process, with continuous integration and continuous deployment (CI/CD) practices ensuring robust and seamless updates. The phases include:

1. **Initial Setup and Data Collection:** Setting up the environment and gathering data from APIs like Alpha Vantage and Twitter API.
2. **Data Processing and Analysis:** Utilizing Hadoop and Spark for big data processing, and performing sentiment analysis with spaCy, NLTK, and APIs like Google NLP and IBM Watson.
3. **Model Development:** Developing machine learning models using TensorFlow and PyTorch, and implementing time series analysis with statsmodels and Prophet.
4. **Risk Assessment and Stress Testing:** Conducting risk assessments and stress testing using PowerBi, MATLAB, and Monte Carlo simulations.
5. **Automated Trading and Decision Support:** Integrating automated trading platforms like MetaTrader and NinjaTrader, and developing custom decision support systems.
6. **Continuous Improvement:** Implementing CI/CD with Jenkins and GitLab, and monitoring performance with Splunk and New Relic.

## Dataset Information
YouStock.AI utilizes datasets sourced from various reliable providers via APIs such as Alpha Vantage and Twitter API. Additionally, YouData.ai is used to enrich the datasets with high-quality, relevant financial data. This enables comprehensive analysis and more accurate predictive modeling.

![Dataset ScreenShot](image.png)

[Database link here at YouData.AI](https://datalink.youdata.ai/yc597789)


---

*Harbinger of Trades Team*