
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            potential=float(request.form['potential'])
            heading_accuracy= float(request.form['heading_accuracy'])
            short_passing= float(request.form['short_passing'])
            acceleration= float(request.form['acceleration'])
            reactions= float(request.form['reactions'])
            strength= float(request.form['strength'])
            marking= float(request.form['marking'])
            gk_diving= float(request.form['gk_diving'])
            gk_kicking= float(request.form['gk_kicking'])
            filename = 'mlproject.pkl'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[potential,heading_accuracy,short_passing,acceleration,reactions,strength,marking,gk_diving,gk_kicking]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app

    														