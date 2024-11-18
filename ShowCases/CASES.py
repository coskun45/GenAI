
import streamlit as st

# Sidebar
with st.sidebar:
    st.header("Contact Information")

    # Website link
    st.markdown("[adesso Website](https://www.adesso.de/)", unsafe_allow_html=True)

    # Email link
    st.markdown("[Email](mailto:info@adesso.de)", unsafe_allow_html=True)

    # Phone number
    st.markdown("[Phone](tel:+4923170007000)", unsafe_allow_html=True)

    # Address information
    st.markdown("**Address:**")
    st.write("adesso SE")
    st.write("Adessoplatz 1")
    st.write("44268 Dortmund")



st.title("Welcome to Data Driven Insurance")
st.caption("This website will present use cases developed by DDI, illustrating how artificial intelligence can be applied within the insurance sector.")


image_url = "./Docs/Bilder_PPT_DigitaleTransformation.jpg"  # Replace with your image URL
st.image(image_url, use_column_width=True, output_format="auto")

