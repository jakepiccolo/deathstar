import subprocess

def play_video(file_path):
    # Construct the omxplayer command with the loop option
    command = f"omxplayer --loop {file_path}"

    # Start the omxplayer process
    process = subprocess.Popen(command, shell=True)

    # Wait for the process to finish (you can interrupt it with Ctrl+C)
    try:
        process.wait()
    except KeyboardInterrupt:
        # If you want to stop the video playback with Ctrl+C
        process.terminate()

# Path to the video file
video_file = "death_star.mp4"

# Call the play_video function
play_video(video_file)
