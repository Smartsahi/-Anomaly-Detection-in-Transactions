import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.ensemble import IsolationForest

# Function to detect fraud
def detect_fraud(transaction_amount, avg_amount, frequency):
    model = IsolationForest(contamination=0.02, random_state=42)
    data = pd.DataFrame({
        'Transaction_Amount': [transaction_amount],
        'Average_Transaction_Amount': [avg_amount],
        'Frequency_of_Transactions': [frequency]
    })
    prediction = model.fit_predict(data)
    return 'Fraud' if prediction[0] == -1 else 'Normal'

# GUI Setup
app = tk.Tk()
app.title("Fraud Detection System")
app.geometry("300x250")

# Labels and Entry Fields
tk.Label(app, text="Transaction Amount:").pack()
entry_amount = tk.Entry(app)
entry_amount.pack()

tk.Label(app, text="Average Transaction Amount:").pack()
entry_avg = tk.Entry(app)
entry_avg.pack()

tk.Label(app, text="Frequency of Transactions:").pack()
entry_freq = tk.Entry(app)
entry_freq.pack()

# Result Label
result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Detect Button Function
def on_detect_click():
    try:
        txn_amount = float(entry_amount.get())
        avg_amount = float(entry_avg.get())
        freq = int(entry_freq.get())
        result = detect_fraud(txn_amount, avg_amount, freq)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Detect Button
detect_button = tk.Button(app, text="Detect Fraud", command=on_detect_click)
detect_button.pack(pady=10)

# Start the application
app.mainloop()
