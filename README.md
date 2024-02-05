# Project ReadMe

## Overview:

This project focuses on building a pipeline to analyze and visualize data related to the top 100 board games, sourced from Board Game Geek (BGG). The primary data frame, named "BGG100," was obtained from Kaggle, while the second data frame, "top_ten_votes," was extracted using the Board Game Geek API. The project involves data exploration, cleaning, and visualization, and the code is organized into multiple files within the project structure.

### Folder Structure:

- **data:**
  - *BGG100.csv:* Initial data frame with the top 100 board games from Kaggle.
  - *top_ten_votes.csv:* Data frame containing information on the top 10 board games extracted from the Board Game Geek API.

- **src:**
  - *exploring.py:* Python script containing functions for data exploration.
  - *cleaning.py:* Python script with functions for cleaning data frames.
  - *visualization.py:* Python script with functions to create plots.
  - *main.py:* Main script to execute the entire pipeline.

- **images:**
  - Contains images resulting from the visualization plots.

## Code Details:

### 1. Exploring:

- **Libraries Used:**
  - pandas as pd
  - requests
  - BeautifulSoup from bs4

- **Tasks:**
  - Extracted relevant information from the initial data frame (BGG100).
  - Initiated the extraction process of information from the Board Game Geek API using `requests.get()`, `BeautifulSoup()`, and `soup.find()`.
  - Created a function to extract information from all URLs in the top ten games according to the first data frame.
  - Exported the processed data to the "top_ten_votes.csv" file.

### 2. Cleaning:

- **Libraries Used:**
  - pandas as pd

- **Tasks:**
  - Imported the initial data frame (BGG100).
  - Created functions (`clean_dataframe(df)`, `unify_values(df)`) to clean and unify column names and values.
  - Processed the second data frame, eliminating a column and reducing game names for better visualization.
  - Imported both resulting data frames into new CSV files.

### 3. Visualization:

- **Libraries Used:**
  - pandas as pd
  - matplotlib
  - seaborn

- **Tasks:**
  - Created nine plots to visualize relevant information from the cleaned data frames.

## Execution:

1. Run `exploring.py` to explore and extract information from the BGG100 data frame and Board Game Geek API.
2. Execute `cleaning.py` to clean and process the data frames.
3. Run `visualization.py` to create visualizations based on the cleaned data.
4. Execute `main.py` to run the entire pipeline, utilizing functions from `exploring.py`, `cleaning.py`, and `visualization.py`.

The resulting visualizations are stored in the "images" folder.

Feel free to explore the code in the respective files for detailed implementation and function definitions.

### Author

[Guillermo Diaz]