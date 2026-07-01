# train_test_split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split[df.drop['column_value'], df['coulmn_vlaue'], test_size=0.3, random_state=3]

# StandardScaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

--fit the data (extracts information from the data like mean and standard deviation)--
scaler.fit(x_train)

--scaling the data-- (returns the dataset in numpy array form)
x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)


