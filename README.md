# -Anomaly-Detection-in-Transactions
This project implements an anomaly detection system using machine learning to identify unusual or fraudulent transactions in financial datasets. The project utilizes the Isolation Forest algorithm in Python, along with a graphical user interface for user interaction.

## Project Structure

```
/Anomaly-Detection-in-Transactions
│── README.md  
│── LICENSE  
│── .gitignore  
│── dataset/  
│   └── transaction_anomalies_dataset.csv  
│── src/  
│   └── main.py  
│   └── gui.py  
│   └── data_preprocessing.py  
│── requirements.txt  
│── docs/  
│   └── Project_Report.pdf  
```

## Installation
1. Clone the repository:  
```bash
$ git clone https://github.com/username/Anomaly-Detection-in-Transactions.git
```

2. Navigate to the project directory:
```bash
$ cd Anomaly-Detection-in-Transactions
```

3. Install the required libraries:
```bash
$ pip install -r requirements.txt
```

## Usage
- Run the main script to detect anomalies:  
```bash
$ python src/main.py
```

- Run the GUI for user input and fraud detection:  
```bash
$ python src/gui.py
```

## Dataset
The dataset is located in the `dataset/` folder and contains transaction data with attributes such as transaction amount, frequency, and average transaction amount.

## Evaluation
- Precision, Recall, and F1-score are used to evaluate the model's performance.
- The results are logged and visualized in the output folder.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
