from music_utils import (
    search_by_name,
    get_track_info,
    search_similar_tracks,
    create_collection,
    show_radar_chart,
     VECTOR_COLS, audio_df)

import streamlit as st
create_collection()

st.set_page_config(page_title="Music Recommender", layout="wide")
st.title("🎧 Music Recommendation System (Qdrant)")

search_query = st.text_input("🔍 Search for a song")

if search_query:
    results = search_by_name(search_query)
    if len(results) == 0:
        st.warning("No matching tracks found.")
    else:
        selected = st.selectbox("Select a track", results["track_name"])
        track_id = results[results["track_name"] == selected]["track_id"].values[0]
        main_track = get_track_info(track_id)

        # Display current song
        st.markdown("### ▶️ Now Playing")
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(main_track["image_album"], use_column_width=True)
        with col2:
            st.markdown(f"**🎵 {main_track['track_name']}**")
            st.markdown(f"*🎤 {main_track['artist_name']}*")
            st.markdown(f"🔗 [Spotify Link]({main_track.get('external_urls_tracks', '#')})")
            st.markdown("### 📊 Audio Feature Vector")
            selected_vector = audio_df[audio_df["track_id"] == track_id][VECTOR_COLS].values[0]
            st.json(dict(zip(VECTOR_COLS, selected_vector)))
            show_radar_chart(selected_vector, VECTOR_COLS)

        st.markdown("### 🎶 Similar Recommendations")
        similar_ids = search_similar_tracks(track_id)

        rec_cols = st.columns(5)
        for i, (sid,score) in enumerate(similar_ids):
            info = get_track_info(sid)
            with rec_cols[i % 5]:
                st.image(info.get("image_album", ""), use_column_width=True)
                st.markdown(f"**{info['track_name']}**", help=info.get("artist_name", ""))

                st.markdown(f"Similarity Score: `{score:.4f}`", unsafe_allow_html=True)
