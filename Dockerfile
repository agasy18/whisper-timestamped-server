# Use an official Python runtime as a parent image
FROM python:3.9-slim


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ffmpeg git

RUN python3 -m pip install --upgrade pip


# Install whisper-timestamped
RUN git clone https://github.com/linto-ai/whisper-timestamped.git /tmp/whisper-timestamped
RUN cd /tmp/whisper-timestamped && pip install --trusted-host pypi.python.org -r requirements.txt
RUN cd /tmp/whisper-timestamped && python3 setup.py install
RUN rm -rf /tmp/whisper-timestamped


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install  --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run whisper_app.py when the container launches
CMD ["uvicorn", "whisper_app:app", "--host", "0.0.0.0", "--port", "8000"]