def match_landmarks(landmarks_found, stored_landmarks):
    #compare vectors
    matched_landmarks = []
    new_landmarks = []

    if len(stored_landmarks)==0:
        new_landmarks=landmarks_found
    else:
        for landmark in landmarks_found:
            for i in range(len(stored_landmarks)):
                if landmark==stored_landmarks[i]:
                    matched_landmarks.append(landmark)
                    similar_landmarks.append(landmark)
                else:
                    new_landmarks.append(landmark)
<<<<<<< HEAD
=======
            if len(similar_landmarks)>1: more than one new matched landmark aka if a found landmark has multiple matched landmarks
                landmark.transfer_coordinates(stored_landmarks[i])
                ignore landmarks that are further away than a certain threshold
                take average of all matched landmarks that are close to the
                update landmark in stored_landmarks
                extend matched_landmarks by
>>>>>>> extended draft

    return matched_landmarks, new_landmarks
