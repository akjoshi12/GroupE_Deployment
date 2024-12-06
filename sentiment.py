import streamlit as st
from transformers import pipeline
import time
import random

# Custom CSS for styling
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    font-weight: bold;
    color: #2C3E50;
}
.sub-font {
    font-size:16px !important;
    color: #34495E;
}
.stButton>button {
    background-color: #3498DB;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #2980B9;
    transform: scale(1.05);
}
.result-box {
    background-color: #F7F9FA;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
body {
    background-color: #F0F2F6;
}
</style>
""", unsafe_allow_html=True)

# Amazon shoe review test cases
AMAZON_SHOE_REVIEWS = [
    {
        "text": "The shoes are very comfortable, but the color is not what I expected.",
        "description": "Positive sentiment with a slight negative aspect"
    },
    {
        "text": "These shoes started falling apart after just a week of use.",
        "description": "Strong negative sentiment about durability"
    },
    {
        "text": "I love these shoes! Perfect fit and they look great.",
        "description": "Clear positive sentiment"
    },
    {
        "text": "The shoes fit okay, but they feel too stiff. I'm unsure if I should keep them.",
        "description": "Neutral sentiment with a bit of uncertainty"
    },
    {
        "text": "Comfortable but they squeak loudly when walking. Not a fan.",
        "description": "Mixed sentiment with a product flaw"
    },
    {
        "text": "The size runs smaller than expected. I had to return them.",
        "description": "Negative sentiment about size and fit"
    },
    {
        "text": "Great for running, but not as stylish as I hoped.",
        "description": "Positive sentiment with a focus on performance over style"
    },
    {
        "text": "These shoes are too expensive for the quality they offer.",
        "description": "Negative sentiment based on price-to-quality ratio"
    }
]

# Load the sentiment pipeline
@st.cache_resource
def load_sentiment_pipeline():
    return pipeline("sentiment-analysis", model="sentiment_model")

# Main app
def main():
    # Custom title with styling
    st.markdown('<p class="big-font">🔍 Sentiment Analysis Insights</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-font">Uncover the emotional tone of your text</p>', unsafe_allow_html=True)

    # Add tabs for different analysis modes
    tab1, tab2 = st.tabs(["Custom Analysis", "Amazon Shoe Reviews"])

    with tab1:
        # Text input with enhanced styling
        text = st.text_area("Enter your text here:", 
                            height=200, 
                            help="Paste the text you want to analyze",
                            key="sentiment_input")

        # Analyze button
        if st.button("Analyze Sentiment"):
            # Validate input
            if not text.strip():
                st.error("Please enter some text to analyze!")
                return

            # Analyze sentiment
            analyze_sentiment(text)

    with tab2:
        st.markdown("### Amazon Shoe Review Sentiment Analysis")
        st.markdown("Explore how the sentiment analysis model handles different Amazon shoe reviews:")
        
        # Dropdown to select review case
        selected_case = st.selectbox(
            "Choose a review case", 
            options=[case['description'] for case in AMAZON_SHOE_REVIEWS]
        )

        # Find the selected test case
        review_case = next(case for case in AMAZON_SHOE_REVIEWS if case['description'] == selected_case)
        
        st.markdown(f"**Review:** {review_case['text']}")
        
        # Analyze button for review cases
        if st.button("Analyze Review"):
            analyze_sentiment(review_case['text'], is_test_case=True)

    # Sidebar with additional information
    with st.sidebar:
        st.markdown('<p class="big-font">🧠 About</p>', unsafe_allow_html=True)
        st.markdown("""
        This app demonstrates advanced sentiment analysis on Amazon shoe reviews.
        
        **Key Features:**
        - Instant sentiment detection
        - Handles complex linguistic nuances
        - Robust across different review types
        """)

    # Footer
    st.markdown("---")
    st.markdown('<p style="text-align:center; color:#7F8C8D;">Made with ❤️ by Group E</p>', unsafe_allow_html=True)

# Sentiment analysis function
def analyze_sentiment(text, is_test_case=False):
    # Load sentiment pipeline
    sentiment_pipeline = load_sentiment_pipeline()

    # Show loading spinner
    with st.spinner('Analyzing sentiment...'):
        # Small delay to simulate processing
        time.sleep(1)
        
        # Perform sentiment analysis
        result = sentiment_pipeline(text)[0]

    # Display results in a styled container
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    
    # Emoji based on sentiment
    emoji = "😊" if result['label'] == 'POSITIVE' else "😔"
    
    # Results with markdown styling
    st.markdown(f"""
    ### Sentiment Analysis Results {emoji}
    
    **Sentiment:** {result['label']}
    
    **Confidence Score:** {result['score']:.2%}
    """)
    
    # If it's a test case, add additional explanation
    if is_test_case:
        st.markdown("#### 🔍 Robustness Analysis")
        st.markdown("""
        This test case demonstrates the model's ability to handle:
        - Complex linguistic structures
        - Nuanced emotional expressions
        - Potentially ambiguous sentiments
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
