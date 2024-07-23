# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR  /home/autogen/autogen/myapp

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
# If you don't have a requirements.txt, you can remove this line
COPY ../requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install numpy and scipy
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install --trusted-host -r pypi.python.org pyautogen docker


# Run main.py when the container launches
CMD ["python", "./app.py"]
