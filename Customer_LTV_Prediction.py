{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8d8e06a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE: 478.72\n",
      "RMSE: 5930.34\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Final predictions saved to Predicted_LTV.csv\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from datetime import datetime\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.metrics import mean_absolute_error, mean_squared_error\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# === Step 1: Load & Clean Data ===\n",
    "file_path = \"Online Retail.xlsx\"\n",
    "df = pd.read_excel(file_path)\n",
    "\n",
    "# Drop rows with missing CustomerID\n",
    "df.dropna(subset=['CustomerID'], inplace=True)\n",
    "\n",
    "# Convert InvoiceDate to datetime\n",
    "df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])\n",
    "\n",
    "# Remove cancelled orders\n",
    "df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]\n",
    "df = df[df['Quantity'] > 0]\n",
    "\n",
    "# Create TotalPrice\n",
    "df['TotalPrice'] = df['Quantity'] * df['UnitPrice']\n",
    "\n",
    "# === Step 2: Feature Engineering ===\n",
    "\n",
    "# Set reference date for recency calculation (e.g., last invoice date + 1)\n",
    "reference_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)\n",
    "\n",
    "# Group by CustomerID\n",
    "customer_df = df.groupby('CustomerID').agg({\n",
    "    'InvoiceDate': [lambda x: (reference_date - x.max()).days,  # Recency\n",
    "                    'count'],                                   # Frequency (transaction count)\n",
    "    'TotalPrice': ['sum', 'mean']                               # Total Spend (LTV), AOV\n",
    "})\n",
    "\n",
    "# Flatten column names\n",
    "customer_df.columns = ['Recency', 'Frequency', 'TotalSpend', 'AOV']\n",
    "customer_df.reset_index(inplace=True)\n",
    "\n",
    "# === Step 3: Model Training ===\n",
    "\n",
    "# Features and target\n",
    "X = customer_df[['Recency', 'Frequency', 'AOV']]\n",
    "y = customer_df['TotalSpend']\n",
    "\n",
    "# Train-test split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Model: Random Forest Regressor\n",
    "model = RandomForestRegressor(n_estimators=100, random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Predict\n",
    "y_pred = model.predict(X_test)\n",
    "\n",
    "# === Step 4: Evaluation ===\n",
    "mae = mean_absolute_error(y_test, y_pred)\n",
    "rmse = np.sqrt(mean_squared_error(y_test, y_pred))\n",
    "\n",
    "print(f\"MAE: {mae:.2f}\")\n",
    "print(f\"RMSE: {rmse:.2f}\")\n",
    "\n",
    "# === Step 5: Visualization ===\n",
    "plt.figure(figsize=(8,6))\n",
    "sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)\n",
    "plt.xlabel(\"Actual LTV\")\n",
    "plt.ylabel(\"Predicted LTV\")\n",
    "plt.title(\"Actual vs Predicted Customer Lifetime Value\")\n",
    "plt.grid(True)\n",
    "plt.show()\n",
    "\n",
    "# === Step 6: Customer Segmentation ===\n",
    "customer_df['PredictedLTV'] = model.predict(X)\n",
    "customer_df['Segment'] = pd.qcut(customer_df['PredictedLTV'], q=3, labels=[\"Low\", \"Medium\", \"High\"])\n",
    "\n",
    "# === Step 7: Export to CSV ===\n",
    "customer_df[['CustomerID', 'Recency', 'Frequency', 'AOV', 'PredictedLTV', 'Segment']].to_csv(\"Predicted_LTV.csv\", index=False)\n",
    "print(\"Final predictions saved to Predicted_LTV.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7873e11",
   "metadata": {},
   "outputs": [],
   "source": [
    " "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
