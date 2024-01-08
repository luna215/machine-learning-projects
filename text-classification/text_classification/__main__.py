from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Input your two pieces of text
text1 = "Kathy is intent on utilizing her life experiences and lessons learned to help other women and “paying it forward”.  Her professional background is also one that thrives on supporting females.  After a successful 20-year career in corporate marketing/branding with companies such as Levi and Maybelline, Kathy made the brave decision to dive into entrepreneurship.  As CEO of her own company for the last two decades, Kathy has made an incredible impact cultivating leadership diversity by advancing more women and people of color into positions of influence. Her signature work is The Fearless Leader program, a group mentoring experience designed to help female and BIPOC individuals overcome barriers to leadership.  This program recently led her to coauthor her 5th book, Fearless Female Leaders, an imperative guide for women in leadership and those that support them, to be released early 2024.  The book deconstructs antiquated beliefs that have held women back from reaching their leadership potential and creates a roadmap on how to get there.  You can learn more about the incredible work Kathy is doing through the links below."
text2 = "Melissa Spratt’s story is equals parts tumultuous and incredible, right on par with real life. Melissa starts by sharing her journey through mental illness, low self-esteem and anorexia as a girl and young adult. Her story then winds through periods of solid ground and happy days upheaved by new obstacles including a heartbreaking miscarriage and being a new mom in the face of extreme isolation during the height of the pandemic."

# Create a CountVectorizer to convert text into a matrix of token counts
vectorizer = CountVectorizer().fit_transform([text1, text2])

# Calculate cosine similarity
cosine_sim = cosine_similarity(vectorizer)

# Print the cosine similarity value
print(f"Cosine Similarity: {cosine_sim[0, 1]}")