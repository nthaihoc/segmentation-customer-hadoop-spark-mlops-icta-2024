import numpy as np
import pandas as pd
import datetime
from scipy import stats
from pathlib import Path

class PrepareData:
    def __init__ (self, path):
        self.path = path

    def load_data(self):
        """
            Load datasets
        """
        self.df_customer = pd.read_csv(self.path)

    def feature_engineering(self):
        """
            Feature engineering using boxcox
        """
        self.customer = self.calculate_rfm(self.df_customer)
        df_transform = pd.DataFrame()
        df_transform["Recency"] = stats.boxcox(self.customer['Recency'])[0]
        df_transform["Frequency"] = stats.boxcox(self.customer["Frequency"])[0]
        df_transform["Monetary"] = pd.Series(np.cbrt(self.customer['Monetary'])).values
        df_transform.to_csv("datasets/rfm-customer.csv", index=False)
        return df_transform

    @staticmethod
    def calculate_rfm(df):
        """
            Calculate rfm values
        """
        data = df.dropna(subset=["CustomerID"], axis=0)
        
        data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"], errors="coerce")
        current_date = max(data["InvoiceDate"]) + datetime.timedelta(days=1)
        data["TotalPay"] = data["Quantity"] * data["UnitPrice"]
        customer_seg_df = data.groupby(['CustomerID']).agg(
            {'InvoiceDate': lambda x: (current_date - x.max()).days,
            'InvoiceNo':'count',
            'TotalPay':'sum'
            }
        )

        customer_seg_df.rename(columns={"InvoiceDate": "Recency", 
                                        "InvoiceNo": "Frequency", 
                                        "TotalPay": "Monetary"}, inplace=True)
        return customer_seg_df
