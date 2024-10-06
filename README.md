
# 🚴‍♂️ Bike Sharing Analysis Dashboard


## 🛠️ Tools and Libraries
The project uses the following libraries (as listed in the `requirements.txt` file):
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Plotly**

## 📂 Project Structure
```
📦proyek_analisis_data
 ┣ 📂data
 ┃ ┗ 📄bike_sharing_data.csv
 ┣ 📂scripts
 ┃ ┗ 📄data_preprocessing.py
 ┣ 📂dashboard
 ┃ ┗ 📄dashboard.py
 ┣ 📄requirements.txt
 ┣ 📄README.md
```

## 🚀 Installation and Setup

### Option 1: Using Anaconda
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Create a new environment and activate it:
    ```bash
    conda create --name bike-sharing python=3.9
    conda activate bike-sharing
    ```
3. Install the required dependencies using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Streamlit app:
    ```bash
    streamlit run dashboard/dashboard.py
    ```

### Option 2: Using Pipenv
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory and set up the environment:
    ```bash
    mkdir proyek_analisis_data
    cd proyek_analisis_data
    pipenv install
    pipenv shell
    ```
3. Install the dependencies using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Streamlit app:
    ```bash
    streamlit run dashboard/dashboard.py
    ```
