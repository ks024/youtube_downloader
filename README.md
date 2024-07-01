# YouTube Video Downloader

This project is a simple YouTube video downloader using Python and the `pytube` library, packaged in a Docker container for easy usage.

## Features

- List available video streams with resolution and file size.
- Download videos in the chosen resolution.
- Save downloaded videos directly to a specified directory on the host machine.

## Prerequisites

- Docker installed on your machine.

## Usage

### Building the Docker Image

First, you need to build the Docker image from the provided `Dockerfile`. Run the following command in the project directory:

```bash
docker build -t your_dockerhub_username/yt_downloader .
```

Replace `your_dockerhub_username` with your Docker Hub username.

### Running the Docker Container

To download a YouTube video, run the Docker container with the current directory mounted to `/app/downloads` in the container:

```bash
docker run -it --rm -v "$(pwd):/app/downloads" your_dockerhub_username/yt_downloader <youtube_url>
```

Replace `<youtube_url>` with the URL of the YouTube video you want to download.

### Example

```bash
docker run -it --rm -v "$(pwd):/app/downloads" your_dockerhub_username/yt_downloader <youtube_url>
```

The downloaded video will be saved in the current directory on your host machine.

## Python Script

The Python script `app.py` does the following:

1. Accepts a YouTube URL as a command-line argument.
2. Lists available video streams with their resolution, MIME type, and file size.
3. Prompts the user to choose a format to download.
4. Downloads the chosen video format and saves it to `/app/downloads`.

### Script Usage

You can run the script directly with Python (if you prefer not to use Docker):

```bash
python app.py <youtube_url>
```

Replace `<youtube_url>` with the URL of the YouTube video you want to download.