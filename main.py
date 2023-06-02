import subprocess

def play_video(file_path):
    # Construct the VLC command to play the video in loop mode
    command = f"cvlc --loop {file_path}"

    # Start the VLC process
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