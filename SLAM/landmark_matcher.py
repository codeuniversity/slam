def match_landmarks(landmarks_found, stored_landmarks):
    #compare vectors
    matched_landmarks = []
    new_landmarks = []
    for landmark in landmarks_found:
        if landmark in stored_landmarks:
            matched_landmarks.append(landmark)
        else:
            new_landmarks.append(landmark)
    return matched_landmarks, new_landmarks
