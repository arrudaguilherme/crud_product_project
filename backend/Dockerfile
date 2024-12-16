FROM python:3.9

#define directory
WORKDIR /app

#copy files and install dependecies
COPY requirements.txt /app/requirements.txt

#install dependecies
RUN pip install --no-cache-dir -r requirements.txt

## Copy the rest of the files
COPY . /app

# Define entry point to execute the server
ENTRYPOINT [ "uvicorn","main:app","--host","0.0.0.0","--port","8501"]