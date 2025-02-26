import cv2
import mediapipe as mp

#def functions
def is_thumbs_up(landmarks):
    return (landmarks[4].y < landmarks[2].y and  # Thumb is up
            landmarks[8].y > landmarks[6].y and  # Index down
            landmarks[12].y > landmarks[10].y and  # Middle down
            landmarks[16].y > landmarks[14].y and  # Ring down
            landmarks[20].y > landmarks[18].y)  # Pinky down

def is_okay(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    return (abs(thumb_tip.x - index_tip.x) < 0.05 and  
            abs(thumb_tip.y - index_tip.y) < 0.05 and
            landmarks[12].y < landmarks[10].y and 
            landmarks[16].y < landmarks[14].y and  
            landmarks[20].y < landmarks[18].y)  

def is_peace(landmarks):
    return (landmarks[8].y < landmarks[6].y and  
            landmarks[12].y < landmarks[10].y and  
            landmarks[16].y > landmarks[14].y and  
            landmarks[20].y > landmarks[18].y)

def is_love(landmarks):
    return (landmarks[4].y < landmarks[2].y and
            landmarks[8].y < landmarks[6].y and  
            landmarks[12].y > landmarks[10].y and  
            landmarks[16].y > landmarks[14].y and  
            landmarks[20].y < landmarks[18].y)

def is_eyy(landmarks):
    return (landmarks[4].y < landmarks[2].y and
            landmarks[8].y > landmarks[6].y and  
            landmarks[12].y > landmarks[10].y and  
            landmarks[16].y > landmarks[14].y and  
            landmarks[20].y < landmarks[18].y)

def is_hello(landmarks):
    return (landmarks[4].y < landmarks[2].y and
            landmarks[8].y < landmarks[6].y and  
            landmarks[12].y < landmarks[10].y and  
            landmarks[16].y < landmarks[14].y and  
            landmarks[20].y < landmarks[18].y)

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark

            gesture = "Unknown"
            if is_thumbs_up(landmarks):
                gesture = "Thumbs Up"
            elif is_okay(landmarks):
                gesture = "Okay Symbol"
            elif is_peace(landmarks):
                gesture = "Peace sign"
            elif is_love(landmarks):
                gesture = "I Love You"
            elif is_eyy(landmarks):
                gesture = "Eyy Angas"
            elif is_hello(landmarks):
                gesture = "Hello"
            
            # Display Gesture
            cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 50, 0), 4)
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Gesture Recognition (press 'q' to exit)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()