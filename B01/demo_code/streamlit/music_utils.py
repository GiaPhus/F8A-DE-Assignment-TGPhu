# music_utils.py
import plotly.graph_objects as go
import streamlit as st

import pandas as pd
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go

scaler = StandardScaler()

VECTOR_COLS = [
    "danceability", "energy", "loudness", "speechiness",
    "acousticness", "instrumentalness", "liveness",
    "valence", "tempo"
]
COLLECTION_NAME = "music_recommendation"

audio_df = pd.read_csv("/notebooks/track_full.csv")
audio_df[VECTOR_COLS] = scaler.fit_transform(audio_df[VECTOR_COLS])
audio_df["vector"] = audio_df[VECTOR_COLS].values.tolist()

meta_df = pd.read_csv("/notebooks/track_full.csv")

client = QdrantClient(host="qdrant", port=6333)


def create_collection():
    """Recreate collection and upsert audio vectors into Qdrant"""
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=len(VECTOR_COLS),
            distance=Distance.COSINE
        )
    )
    points = [
        PointStruct(
            id=int(i),
            vector=row["vector"],
            payload={"track_id": row["track_id"]}
        )
        for i, row in audio_df.iterrows()
    ]
    client.upsert(collection_name=COLLECTION_NAME, points=points)


def search_similar_tracks(track_id, k=5):
    matched = audio_df[audio_df["track_id"] == track_id]
    if matched.empty:
        raise ValueError(f"Track ID {track_id} not found in audio features data.")
    
    vector = matched["vector"].values[0]

    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=k + 1
    )
    return [
        (r.payload["track_id"], r.score)
        for r in results
        if r.payload["track_id"] != track_id
    ][:k]




def get_track_info(track_id):
    """Return full metadata of a track by ID"""
    return meta_df[meta_df["track_id"] == track_id].iloc[0].to_dict()


def search_by_name(name):
    """Search for track name matching query"""
    return meta_df[meta_df["track_name"].str.contains(name, case=False)]


def show_radar_chart(vector, labels):
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=vector,
        theta=labels,
        fill='toself',
        name='Audio Vector'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
