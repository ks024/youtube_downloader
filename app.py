import sys
from pytube import YouTube


def get_available_streams(streams):
    print("Available Formats:")
    for i, stream in enumerate(streams):
        print(f"{i+1}. {stream.resolution} - {stream.mime_type} - {stream.filesize / (1024 * 1024):.2f} MB")


def download_video(stream):
    try:
        print(f"\nDownloading '{stream.title}'...")
        stream.download()
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error downloading video: {str(e)}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python app.py <youtube_url>")
        return

    url = sys.argv[1]
    try:
        yt = YouTube(url)
    except Exception as e:
        print(f"Error: {str(e)}")
        return

    print(f"Title: {yt.title}")

    # Filter streams and order by resolution
    streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
    get_available_streams(streams)

    while True:
        choice = input("\nEnter the number of the format you want to download or 'q' to quit: ")
        if choice.lower() == 'q':
            return

        try:
            choice = int(choice)
            if 0 <= choice <= len(streams):
                stream = streams[choice-1]
                download_video(stream)
            else:
                raise ValueError
        except ValueError:
            print("\nInvalid input: Enter a valid number or 'q' to quit.")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
