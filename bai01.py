import tkinter as tk
import pyautogui

class FrameRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Frame Recorder")
        self.root.configure(background='pink')
        self.root.geometry("800x500")

        # Create the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame = tk.Frame(self.root, bg="pink")
        self.main_frame.pack(padx=10, pady=10)

        # Create the title label
        self.title_label = tk.Label(self.main_frame, text="Frame Recorder", font=("Arial", 24))
        self.title_label.pack(pady=10)
        self.title_label.configure(bg="pink")

        # Create the FPS frame
        self.fps_frame = tk.Frame(self.main_frame)
        self.fps_frame.configure(bg="pink")
        self.fps_frame.pack(pady=10)

        # Create the FPS label
        self.fps_label = tk.Label(self.fps_frame, text="FPS:")
        self.fps_frame.configure(bg="pink")
        self.fps_label.pack(side=tk.LEFT)

        # Create the FPS entry
        self.fps_entry = tk.Entry(self.fps_frame, width=5)
        self.fps_entry.pack(side=tk.LEFT)

        # Create the create video button
        self.create_video_button = tk.Button(self.main_frame, text="Create Video", command=self.create_video)
        self.create_video_button.pack(pady=10)

        # Create the control frame
        self.control_frame = tk.Frame(self.main_frame)
        self.control_frame.pack(pady=10)

        # Create the pause button
        self.pause_button = tk.Button(self.control_frame, text="Pause", command=self.pause_recording)
        self.pause_button.pack(side=tk.LEFT)

        # Create the start button
        self.start_button = tk.Button(self.control_frame, text="Start", command=self.start_recording)
        self.start_button.pack(side=tk.LEFT)

        # Create the end button
        self.end_button = tk.Button(self.control_frame, text="End", command=self.end_recording)
        self.end_button.pack(side=tk.LEFT)

        # Create the status label
        self.status_label = tk.Label(self.main_frame, text="Recording Paused")
        self.status_label.pack(pady=10)
        self.status_label.configure(bg="pink")

        # Set the default FPS
        self.fps_entry.insert(0, "100")

        # Start the GUI loop
        self.root.mainloop()

    def create_video(self):
        # Get the FPS
        fps = int(self.fps_entry.get())

        # Start recording
        recorder = pyautogui.record(duration=10, fps=fps)

        # Save the video
        with open("video.mp4", "wb") as f:
            f.write(recorder)

        # Update the status label
        self.status_label.config(text="Video Saved")

    def pause_recording(self):
        # Pause recording
        pyautogui.pause()

        # Update the status label
        self.status_label.config(text="Recording Paused")

    def start_recording(self):
        # Start recording
        pyautogui.resume()

        # Update the status label
        self.status_label.config(text="Recording")

    def end_recording(self):
        # Stop recording
        pyautogui.stop()

        # Update the status label
        self.status_label.config(text="Recording Stopped")

if __name__ == "__main__":
    recorder = FrameRecorder()
