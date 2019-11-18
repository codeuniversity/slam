stored_landmarks = []

def match_landmarks(landmarks):
    #compare vectors
    matched_landmarks = []
    for landmark in landmarks:
        for existing_landmark in stored_landmarks:
            if landmark.AB==existing_landmark.AB and landmark.BC==landmark.BC:
                matched_landmarks.append(landmark)
            else:
                stored_landmarks.append(landmark)
    return matched_landmarks
