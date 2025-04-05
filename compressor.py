import os
import subprocess

input_folder = r"C:\Users\boety\Documents\compression\uncompressed"
output_folder = r"C:\Users\boety\Documents\compression\compressed"

os.makedirs(output_folder, exist_ok=True)
ffmpeg_cmd = (
    "ffmpeg -y -i \"{input}\" -vf scale=-2:720 -c:v libx264 -crf 28 "
    "-preset medium -c:a aac -b:a 96k -movflags +faststart \"{output}\""
)
max_size = 10 * 1024 * 1024  # 10 MB change if u want idc

def compress_video(input_path, output_path):
    """Compress a video and ensure the size is under the limit."""
    subprocess.run(ffmpeg_cmd.format(input=input_path, output=output_path), shell=True)
    if os.path.getsize(output_path) > max_size:
        subprocess.run(
            ffmpeg_cmd.format(input=input_path, output=output_path).replace("-crf 28", "-crf 30"),
            shell=True
        )

def compress_videos_in_folder(input_folder, output_folder):
    """Compress all videos in the input folder and save to the output folder."""
    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        if not input_path.lower().endswith(('.mp4', '.mov', '.avi', '.mkv', '.wmv')):
            continue
        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".mp4")
        print(f"Compressing: {file_name}")
        compress_video(input_path, output_path)
        print(f"Saved to: {output_path}")

if __name__ == "__main__":
    compress_videos_in_folder(input_folder, output_folder)
    print("All videos have been processed.")
