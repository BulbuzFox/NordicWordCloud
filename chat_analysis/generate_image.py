import wordcloud

def generate_image(word_counts, image_path):
    wc = wordcloud.WordCloud(width=1200,
                                 height=1024,
                                 max_words=400,
                                 random_state=1,
                                 background_color='black',
                                 margin=20,
                                 colormap='Pastel1',
                                 collocations=False)
    image = wc.generate_from_frequencies(word_counts).to_image()
    image.save(image_path)
