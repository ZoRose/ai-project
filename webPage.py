import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

st.title("Music Recommendation")

def printing(indVal):
    st.text("index         " + str(Labels['index'][indVal]))
    st.text("track_id      " + str(Labels['track_id'][indVal]))
    st.text("track_genre   " + str(Labels['track_genre'][indVal]))
    st.text("artists       " + str(Labels['artists'][indVal]))
    st.text("album_name    " + str(Labels['album_name'][indVal]))
    st.text("track_name    " + str(Labels['track_name'][indVal]))

GraphValues = pd.read_csv('data_labels-reduced_test-reduced_again.csv')
Labels = pd.read_csv('data_labels-reduced_labels-reduced.csv')

scale = StandardScaler()
X = scale.fit_transform(GraphValues)

nval = 30
knn = NearestNeighbors(n_neighbors=nval, metric='euclidean').fit(X)
distances, indices = knn.kneighbors(X)
st.header("Let's Recommend:", divider="rainbow")

choice = st.radio("Select Search Options: ", ('Index', 'Title', 'Artist', 'Title and Artist'))
if (choice == 'Index'):
    songRec = st.slider("Enter a Song Line: ", 0, 24999)
elif (choice == 'Title'):
    songVal = st.text_input("Enter a Song Title: ", "song title...")
    for z in range (0, len(X)-1):
        if (Labels['track_name'][z].casefold() == songVal.casefold()):
            songRec = Labels['index'][z]
            break
        else:
            songRec = 404
elif (choice == 'Artist'):
    songVal = st.text_input("Enter an Artist: ", "artist name...")
    for z in range (0, len(X)-1):
        if (Labels['artists'][z].casefold() == songVal.casefold()):
            songRec = Labels['index'][z]
            break
        else:
            songRec = 404
else:
    songVal = st.text_input("Enter a Song Title: ", "song title...")
    songVal2 = st.text_input("Enter an Artist: ", "artist name...")
    for z in range (0, len(X)-1):
        if ((Labels['track_name'][z].casefold() == songVal.casefold()) and (Labels['artists'][z].casefold() == songVal2.casefold())):
            songRec = Labels['index'][z]
            break
        else:
            songRec = 404
temp = indices[songRec]
st.text("Song Selected: ")
printing(songRec)
st.text("-------------------------------------------------------")
st.text("Recommendations")
st.text("-------------------------------------------------------")

z = 1
st.text("Recommendation 1:")
if ((Labels['track_name'][temp[0]].casefold() != Labels['track_name'][temp[z]].casefold())):
    printing(temp[z])
else:
    while (Labels['track_name'][temp[0]].casefold() == Labels['track_name'][temp[z]].casefold()):
        z = z+1
    printing(temp[z])  
st.text("-------------------------------------------------------")
    
st.text("Recommendation 2:")
g = z+1
if ((Labels['track_name'][temp[z]].casefold() != Labels['track_name'][temp[g]].casefold()) and (Labels['track_name'][temp[0]].casefold() != Labels['track_name'][temp[g]].casefold())):
    printing(temp[g])
else:
    while ((Labels['track_name'][temp[z]].casefold() == Labels['track_name'][temp[g]].casefold()) or (Labels['track_name'][temp[0]].casefold() == Labels['track_name'][temp[g]].casefold())):
        g = g+1
    printing(temp[g])
st.text("-------------------------------------------------------")
    
st.text("Recommendation 3:")
r = g+1
if ((Labels['track_name'][temp[r]].casefold() != Labels['track_name'][temp[z]].casefold()) and (Labels['track_name'][temp[r]].casefold() != Labels['track_name'][temp[g]].casefold()) and (Labels['track_name'][temp[r]].casefold() != Labels['track_name'][temp[0]].casefold())):
    printing(temp[r])
else:
    while ((Labels['track_name'][temp[z]].casefold() == Labels['track_name'][temp[g]].casefold()) or (Labels['track_name'][temp[g]].casefold() == Labels['track_name'][temp[r]].casefold()) or (Labels['track_name'][temp[0]].casefold() == Labels['track_name'][temp[r]].casefold())):
        r = r+1
    printing(temp[r])
st.text("-------------------------------------------------------")


