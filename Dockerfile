# base image
FROM python:3.11

# workdir
WORKDIR /app

# copy
COPY requirements.txt .
COPY app.py .
COPY main.pkl .

# run
RUN pip install -r requirements.txt

# port
EXPOSE 8501

# command
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]