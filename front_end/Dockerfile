# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Streamlit app files into the container
COPY . /app

# Install Streamlit and any other dependencies
RUN pip install -r requirements.txt

# Expose the port that Streamlit runs on (default is 8501)
EXPOSE 8501

# Set the entrypoint to run the Streamlit app
ENTRYPOINT ["streamlit", "run", "gui.py", "--server.port=8501", "--server.address=0.0.0.0"]