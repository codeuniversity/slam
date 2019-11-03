def extract_spike_landmark(results, laserdata):
    #array to keep track of found landmarks:
    landmarks = []
    threshold = 300 #in mm
    for i in range(len(laserdata)-2): #i = degree
        print(results[i][1]-results[i+1][1])
        if (results[i][1]-results[i+1][1])*(-1) >= threshold:
            landmarks.append([laserdata[i],[laserdata[i+1],laserdata[i+2]]])
    print(landmarks)


results = [[0, 30], [1,340],[2,100], [3,400], [4,200]]
laserdata = [(1,5), (10,34), (5,50), (30,10), (30,10)]
extract_spike_landmark(results,laserdata)


