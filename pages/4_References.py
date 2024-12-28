import streamlit as st

# Title in the sidebar
st.sidebar.markdown("References")

# Title of the page with center alignment and added spacing
st.markdown(
    "<h1 style='text-align: center; margin-bottom: 20px;'>References</h1>", 
    unsafe_allow_html=True
)

# Works Cited - formatted using HTML for custom styling with added link style
st.markdown("""
<p style="font-size: 16px; margin-bottom: 20px;">Jennifer L. Harris, et al. “TV Exposure, Attitudes about Targeted Food Ads and Brands, and Unhealthy Consumption by Adolescents: Modeling a Hierarchical Relationship.” Appetite, Academic Press, 12 Nov. 2021, <a href="https://www.sciencedirect.com/science/article/abs/pii/S019566632100711X?via%3Dihub" target="_blank" style="color: inherit; text-decoration: none;">www.sciencedirect.com</a>.</p>

<p style="font-size: 16px;">Uconn, <a href="https://media.ruddcenter.uconn.edu/wp-content/uploads/sites/2909/2024/06/FACTS2021.pdf" target="_blank" style="color: inherit; text-decoration: none;">media.ruddcenter.uconn.edu/wp-content/uploads/sites/2909/2024/06/FACTS2021.pdf</a>. Accessed 27 Dec. 2024.</p>
""", unsafe_allow_html=True)


