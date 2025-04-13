# ML Score Predictor

This project is a web application that predicts student scores based on various input features using a machine learning model. The application is built using Flask and integrates a Jupyter Notebook that contains the machine learning code.

## Project Structure

```
ml-score-predictor-ui
├── src
│   ├── app.py                # Main application file that sets up the Flask web server
│   ├── templates
│   │   └── index.html        # HTML template for the user interface
│   └── static
│       └── style.css         # CSS styles for the HTML template
├── Student_Mark_Prediction_final1.ipynb  # Jupyter Notebook with machine learning code
├── requirements.txt          # Python dependencies for the project
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ml-score-predictor-ui
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask application:
   ```
   python src/app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Enter the required features in the input fields.
- Click the "Predict" button to see the predicted student score based on the input features.

## License

This project is licensed under the MIT License.