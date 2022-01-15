# getting base image python3
FROM python:3.8

# copying all files from current directory
COPY . /usr/app/

# working directory is same as current/copied directory
WORKDIR /usr/app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 
EXPOSE 5000

# Run the application:
CMD ["python", "app.py", "--host", "0.0.0.0", "-p", "5000"]