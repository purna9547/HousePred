import json

from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd

df = pd.read_csv('C:\\Users\\User\\OneDrive\\Desktop\\HousePred\\ModelPython\\Housing.csv')

x = df[['area', 'bedrooms']]
y = df['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=1)

reg = LinearRegression()
reg.fit(x_train, y_train)


app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_data()
        data_dict = json.loads(data)
        price = reg.predict([[data_dict['area'], data_dict['bedrooms']]])
        return jsonify({
            'prediction': price[0]
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
