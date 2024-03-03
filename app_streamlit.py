import streamlit as st



image_path = "8-surprising-facts-about-lungs-1692982415-removebg-preview.png"


st.markdown("<h1 style='text-align: center;'>Lung Scan Detection System</h1>", unsafe_allow_html=True)


# Add image to the content
st.image(image_path, caption='', use_column_width=True)


# Use st.file_uploader to create a file uploader widget
uploaded_file = st.file_uploader("Please Upload your CT scan here", type=["jpg", "jpeg", "png"])
#new commit

# Check if a file was uploaded
if __name__ == "__main__":
    if uploaded_file is not None:
        # Use the uploaded file object to read the image data
        image = uploaded_file.read()
        
        # Display the uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)
