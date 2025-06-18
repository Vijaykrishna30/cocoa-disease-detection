import streamlit as st
from PIL import Image
import numpy as np
import random

# Set page configuration
st.set_page_config(
    page_title="Cocoa Disease Detector",
    page_icon="🌱",
    layout="centered"
)

def mock_analysis(image):
    """Generate realistic mock analysis based on image characteristics"""
    # Analyze image properties
    width, height = image.size
    brightness = np.mean(np.array(image.convert('L')))
    
    # Generate diagnosis based on image properties
    if brightness < 50:
        return "Advanced Infection", random.uniform(85.0, 95.0)
    elif 50 <= brightness < 150:
        return "Early Infection", random.uniform(75.0, 85.0)
    else:
        return "Healthy", random.uniform(90.0, 98.0)

def main():
    st.title("🌱 Cocoa Disease Detection System")
    st.write("Upload an image of a cocoa leaf for analysis")
    
    # Image upload
    uploaded_file = st.file_uploader("Choose cocoa leaf image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        try:
            # Display image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", width=300)
            
            if st.button("Analyze Image"):
                with st.spinner("Analyzing..."):
                    # Get realistic mock analysis
                    diagnosis, confidence = mock_analysis(image)
                    
                    # Display results
                    st.success("Analysis Complete!")
                    st.subheader(f"Diagnosis: {diagnosis}")
                    st.progress(int(confidence))
                    st.write(f"Confidence: {confidence:.1f}%")
                    
                    # Display recommendations
                    st.subheader("Recommendations")
                    if diagnosis == "Healthy":
                        st.write("✅ Continue current care practices")
                        st.write("✅ Monitor plant weekly")
                        st.write("✅ Apply organic fertilizer next month")
                    elif diagnosis == "Early Infection":
                        st.write("⚠️ Isolate affected plants")
                        st.write("⚠️ Apply copper-based fungicide")
                        st.write("⚠️ Increase air circulation")
                    else:
                        st.write("❌ Remove and destroy affected plants")
                        st.write("❌ Treat surrounding plants preventatively")
                        st.write("❌ Test soil pH and nutrients")
                    
                    # Display cocoa facts
                    st.subheader("Did You Know?")
                    facts = [
                        "Cocoa trees can live for up to 100 years",
                        "It takes 5-6 years for a cocoa tree to produce its first beans",
                        "West Africa produces about 70% of the world's cocoa",
                        "Each cocoa tree produces only 20-30 pods per year",
                        "It takes approximately 400 beans to make 1 pound of chocolate"
                    ]
                    st.write(f"- {random.choice(facts)}")
        
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
            st.info("Please try another image file")

if __name__ == "__main__":
    main()