import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

Document1 = """Giving al priorities to physical facilities only, or to live solely on the basis of physical facilities, may be termed as ‘Animal Consciousness’. Living with al three: Right understanding, Relationship and Physical facilities are called ‘Human Consciousness'.
For animal, physical facility is necessary as well as complete – whereas for human beings it is necessary but not complete. Working only for physical facilities is living with Animal Consciousness.
Working for right understanding as the first priority followed by relationship and physical facilities implies living with Human Consciousness."""
 
Document2 = """Giving all priorities to physical facilities only, or to live solely on the basis 
of physical facilities be termed as 'Animal Consciousness'. Living with all three: Right 
understanding, Relationship Physical facilities is called 'Human Consciousness. For animal, 
physical facility is necessary as well as complete — whereas for human beings it is necessary 
but not complete. Working only for physical facilities is living with Animal Consciousness. 
Working for light understanding as the first priority followed by relationship and physical 
facilities implies living with Human Consciousness. """

corpus = [Document1, Document2]
Counts = count_vect.fit_transform(corpus)
pd.DataFrame(Counts.toarray(),columns=count_vect.get_feature_names_out(),index=['Document1', 'Document2'])

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
trsfm=vectorizer.fit_transform(corpus)
pd.DataFrame(trsfm.toarray(),columns=vectorizer.get_feature_names_out(),index=['Document 1','Document 2'])

from sklearn.metrics.pairwise import cosine_similarity
result = cosine_similarity(trsfm[0:1],trsfm)
print("Cosine Similarity: ", result)

