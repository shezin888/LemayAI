FROM python:3.10

# Working directory inside container
WORKDIR /app

# Copy files from host to /app in container
COPY . .

# Install all necessary dependencies
RUN pip install -r requirements.txt

EXPOSE 8000

# cmd to start app using Uvicorn when container runs
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
