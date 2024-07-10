# Flying Price Prediction Webapp

## Overview
A flight fare prediction web application combines data analytics, machine learning, and user-centric design to help travelers find the best deals on flights by predicting fare changes.

## Software Requirements
1. [VSCode IDE](https://code.visualstudio.com/)
2. [GitHub Account](https://github.com/)
3. [Git CLI](https://git-scm.com/downloads)
4. [Streamlit](https://streamlit.io/cloud)
5. [Data Source](https://www.kaggle.com/)

## Getting Started

To use the flight fare prediction web application, follow these steps:

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/sohel1807/Flight_fare_prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd Flight_fare_prediction
```

### 3. Install Dependencies

```bash
pip install streamlit
```

### 4. Run the Development Server
Run the project on your local machine:

```bash
streamlit run app.py
```

The web application will start running.

## API Usage

You can also use the provided API to predict flight fares. Here is the API endpoint and a sample input:

### Endpoint
`https://sohel1807--fare-predict.modal.run`

### Sample Input
```json
{
   "Airline": "IndiGo",
   "Source": "Delhi",
   "Destination": "Banglore",
   "Total_Stops": 1,
   "Journey_date": 15,
   "Journey_month": "March",
   "Departure_hour": 10,
   "Departure_minute": 30,
   "Arrival_hour": 13,
   "Arrival_minute": 45
}
```

### Sample Output
```json
{
   "predicted_fare (Rs)": 4500
}
```

## Contributing

If you'd like to contribute to the project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are welcome and appreciated!

## Issues

If you encounter any issues or have suggestions for improvement, please open an issue on GitHub, and we'll address it as soon as possible.

