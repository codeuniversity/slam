stored_landmarks = []

def match_landmarks(landmarks_found):
    #compare vectors
    matched_landmarks = []
    for landmark in landmarks_found:
        if landmark in stored_landmarks:
            matched_landmarks.append(landmark)
        else:
            stored_landmarks.append(landmark)
    return matched_landmarks
