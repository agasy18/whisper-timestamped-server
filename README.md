# Whisper Timestamped Transcription API
(not for production use)


This repository contains a FastAPI implementation of the Whisper Transcription API. 
The API receives an audio containing file and transcribes it using the [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped.git). 

## Getting Started

### Build the Docker Image
To build the Docker image, navigate to the directory containing the Dockerfile and run:

```bash
docker build -t whisper-transcription-api .
```

### Run the Docker Container
To run the Docker container, execute:

```bash
docker run -it -e "DEVICE=cpu" -p 8000:8000 whisper-transcription-api 
```

#### Environment Variables

* `MODEL`: (optional) The Whisper model to use. Default is "small".
* `DEVICE`: (optional) The device to run the model on. Default is "cuda".


The API will be accessible at http://localhost:8000/docs

