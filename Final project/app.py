import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import time
import pandas as pd
from utils import calculate_angle, RepCounter, AngleSmoother, play_beep, speak

# ---------------------
# Streamlit UI Setup
# ---------------------
st.set_page_config(page_title="AI Fitness Coach", layout="wide")
st.title("🏋️ AI Virtual Fitness Coach")
st.markdown("Track your reps and form in real time using your webcam and AI pose detection.")

# Sidebar settings
exercise = st.sidebar.selectbox("Choose Exercise", ["Bicep Curls", "Squats"])
run_webcam = st.sidebar.checkbox("Start Webcam", key="start_webcam_checkbox")

# Session state
if "previous_count" not in st.session_state:
    st.session_state.previous_count = 0

# Repetition Counter Setup
if exercise == "Bicep Curls":
    joint_points = ["LEFT_SHOULDER", "LEFT_ELBOW", "LEFT_WRIST"]
    counter = RepCounter(up_angle_thresh=160, down_angle_thresh=30)
elif exercise == "Squats":
    joint_points = ["LEFT_HIP", "LEFT_KNEE", "LEFT_ANKLE"]
    counter = RepCounter(up_angle_thresh=170, down_angle_thresh=90)

# Pose and drawing setup
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Webcam Display Placeholder
stframe = st.empty()
start_time = None

if run_webcam:
    cap = cv2.VideoCapture(0)
    smoother = AngleSmoother()
    start_time = time.time()

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while run_webcam and cap.isOpened():
            run_webcam = st.session_state["start_webcam_checkbox"]
            ret, frame = cap.read()
            if not ret:
                st.warning("Failed to access webcam.")
                break

            frame = cv2.flip(frame, 1)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                landmarks = results.pose_landmarks.landmark
                h, w, _ = image.shape

                try:
                    a = [landmarks[getattr(mp_pose.PoseLandmark, joint_points[0])].x * w,
                         landmarks[getattr(mp_pose.PoseLandmark, joint_points[0])].y * h]
                    b = [landmarks[getattr(mp_pose.PoseLandmark, joint_points[1])].x * w,
                         landmarks[getattr(mp_pose.PoseLandmark, joint_points[1])].y * h]
                    c = [landmarks[getattr(mp_pose.PoseLandmark, joint_points[2])].x * w,
                         landmarks[getattr(mp_pose.PoseLandmark, joint_points[2])].y * h]

                    raw_angle = calculate_angle(a, b, c)
                    angle = smoother.smooth(raw_angle)
                    count, stage = counter.update(angle)

                    # 🧠 Voice Feedback Here
                    if stage == "up" and count > st.session_state.previous_count:
                        speak(str(count))
                        if count % 5 == 0:
                            speak("Great job!")
                        st.session_state.previous_count = count

                    # Display info
                    cv2.putText(image, f"Angle: {int(angle)}", (10, 60),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)
                    cv2.putText(image, f"Reps: {count}", (10, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

                except Exception as e:
                    st.error(f"Pose tracking error: {e}")

            stframe.image(image, channels='BGR')

        elapsed_time = int(time.time() - start_time)
        cap.release()
        cv2.destroyAllWindows()

        log = {
            "Exercise": exercise,
            "Reps": counter.counter,
            "Time (sec)": elapsed_time,
            "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        df = pd.DataFrame([log])
        try:
            df_existing = pd.read_csv("workout_logs.csv")
            df_existing = pd.concat([df_existing, df], ignore_index=True)
            df_existing.to_csv("workout_logs.csv", index=False)
        except FileNotFoundError:
            df.to_csv("workout_logs.csv", index=False)

        st.success("✅ Workout saved to workout_logs.csv")

# Sidebar Live & Final Metrics
if run_webcam and "counter" in locals():
    st.sidebar.metric("Total Reps", counter.counter)

if not run_webcam and "counter" in locals() and start_time is not None:
    elapsed_time = int(time.time() - start_time)
    st.sidebar.metric("Workout Time", f"{elapsed_time} sec")
    st.sidebar.metric("Total Reps", counter.counter)
