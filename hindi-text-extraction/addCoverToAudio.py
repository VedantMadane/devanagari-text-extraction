from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
from moviepy.editor import AudioFileClip
# Path to your audio file (MP3)
audio_path = "C://Users/vedantm/Ultimate/dhando.mp3"

# Path to your image file (e.g., JPG, PNG)
image_path = "C:/Users/vedantm/Pictures/Screenshots/dhando.png"

# Desired video output filename (e.g., MP4)
output_video = "C:/Users/vedantm/Pictures/Screenshots/dhando.mp4"

# Create a video clip from the audio file
audio_clip = AudioFileClip(audio_path)

# Read the image as a video clip (single frame)
image_clip = ImageClip(image_path).set_duration(audio_clip.duration)  # Set image duration to match audio
# Create a composite video clip with audio and image clips
final_clip = CompositeVideoClip([audio_clip, image_clip.set_duration(audio_clip.duration)])

# Set the position of the image clip within the composite clip
final_clip.set_position('center')
# Combine audio and image into a single clip (overlay)
# final_clip = image_clip.set_composite("src_over").set_position('center')  # Center image

# Write the combined clip to a new video file
final_clip.write_videofile(output_video, fps=1)  # Adjust fps if needed

print(f"Video created successfully: {output_video}")
