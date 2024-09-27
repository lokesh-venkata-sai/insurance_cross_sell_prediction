import numpy as np
from sklearn.impute import SimpleImputer


class Cleaner:
    def __init__(self):
        # Replace missing values using a descriptive statistic (e.g. mean, median, or most frequent) along each column,
        # or using a constant value.
        self.imputer = SimpleImputer(strategy='most_frequent', missing_values=np.nan)

    def clean_data(self, data):
        data.drop(['id', 'SalesChannelID', 'VehicleAge', 'DaysSinceCreated'], axis=1, inplace=True)
        # columns left
        # columns = ['Gender', 'Age', 'HasDrivingLicense', 'RegionID', 'Switch',
        #        'PastAccident', 'AnnualPremium']

        data['AnnualPremium'] = data['AnnualPremium'].str.replace('£', '').str.replace(',', '').astype(float)

        for col in ['Gender', 'RegionID']:
            data[col] = self.imputer.fit_transform(data[[col]]).flatten()

        data['Age'] = data['Age'].fillna(data['Age'].median())
        data['HasDrivingLicense'] = data['HasDrivingLicense'].fillna(1)
        data['Switch'] = data['Switch'].fillna(-1)
        data['PastAccident'] = data['PastAccident'].fillna("Unknown", inplace=False)

        q1 = data['AnnualPremium'].quantile(0.25)
        q3 = data['AnnualPremium'].quantile(0.75)
        iqr = q3 - q1
        upper_bound = q3 + 1.5 * iqr
        data = data[data['AnnualPremium'] <= upper_bound]

        return data
