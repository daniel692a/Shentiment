from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def cloud(image, text, max_word, max_font, random):
    stopwords = set(STOPWORDS)
    stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may', 'little', 'say', 'must', 'way', 'long', 'yet', 'mean', 'put', 'seem', 'asked', 'made', 'half', 'much', 'certnainly', 'might', 'came'])

    wc = WordCloud(background_color="white", colormap="plasma", max_words=max_word, mask=image, stopwords=stopwords, max_font_size=max_font, random_state=random)

    wc.generate(text)

    image_colors = ImageColorGenerator(image)

    plt.figure(figsize=(200, 200))
    fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [3, 2]})
    axes[0].imshow(wc, interpolation="bilinear")
    axes[1].imshow(image, cmap=plt.cm.gray, interpolation="bilinear")
    for ax in axes:
        ax.set_axis_off()
    st.pyplot()

def main():
    st.write("# Resumen de texto con word clouds☁️😶‍🌫️")
    st.markdown("Herramientas para el proyecto:\n * python\n * wordcloud\n * streamlit\n * matplotlib\n * numpy")
    max_word = st.sidebar.slider("Máximo de palabras", 50, 200, 100)
    max_font = st.sidebar.slider("Tamaño Máximo de fuente", 50, 350, 60)
    random = st.sidebar.slider("Random State", 30, 100, 42 )
    image = st.file_uploader("Escoje un archivo (de preferencia una silueta)")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    text = st.text_area("Añade texto ..")
    if image and text is not None:
        if st.button("Plot"):
            st.markdown("### Word Cloud vs Imagen Original")
            image = np.array(Image.open(image))
            st.write(cloud(image, text, max_word, max_font, random), use_column_width=True)

if __name__=="__main__":
    main()