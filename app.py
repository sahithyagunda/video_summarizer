import streamlit as st
import cv2
import os
import numpy as np
import tempfile
from moviepy.editor import ImageSequenceClip

def merge_frames_to_video(frames, output_path, fps=2):
    """Merge extracted frames into a video."""
    clip = ImageSequenceClip(frames, fps=fps)
    clip.write_videofile(output_path, codec="libx264")

def main():
    st.title("AI Video Summarizer")
    
    uploaded_file = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov", "mkv"])
    
    if uploaded_file is not None:
        temp_video_path = os.path.join(tempfile.gettempdir(), uploaded_file.name)
        with open(temp_video_path, "wb") as f:
            f.write(uploaded_file.read())
        
        st.video(temp_video_path)
        
        # Extract key frames (placeholder logic, replace with your own)
        cap = cv2.VideoCapture(temp_video_path)
        frames = []
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_interval = max(1, frame_count // 10)  # Extract 10 key frames
        
        for i in range(10):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i * frame_interval)
            ret, frame = cap.read()
            if ret:
                frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        cap.release()
        
        # Save summary video
        summary_video_path = os.path.join(tempfile.gettempdir(), "summary_video.mp4")
        merge_frames_to_video(frames, summary_video_path)
        
        st.subheader("Summarized Video")
        st.video(summary_video_path)
        
        # Display sample summary text (replace with AI-generated summary)
        summary_text = "Video captures a sequence of events showcasing urban cycling and navigation. A screen shot of a map with a red marker. A person holding a phone with a map on it. A website with a picture of people riding bikes."
        st.subheader("Summary")
        st.write(summary_text)

if __name__ == "__main__":
    main()
