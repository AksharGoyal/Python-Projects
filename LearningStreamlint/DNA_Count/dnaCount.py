import streamlit as st
import pandas as pd
import altair as alt # for graph
from collections import Counter
from PIL import Image # for logo

# Note: The code has been taken from Data Professor for learning purposes

image = Image.open('./dna-logo.jpg') # Get the image
st.image(image, use_column_width=True)
st.write("""
         # DNA Nucleotide Count App
         
         This app counts the nucleotide composition of query DNA
         
         ***
         """)

st.header("Enter DNA sequence: ")
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
# we get a sequence
sequence = st.text_area("sequence input", sequence_input, height = 150)
# print(sequence)
sequence = sequence.splitlines()
# print(sequence)
sequence = sequence[1:] # first element is just sequence name
sequence = "".join(sequence)

st.write("""
         ***
         """)

st.header("INPUT (DNA Query)") # will print the input DNA sequence
sequence
st.header("OUTPUT (DNA Nucleotide Count)") # Give us the count, which is the purpose of the app

# Get the counts of each nucleotide
st.subheader("1. Print dictionary")
X = Counter(sequence)
X_list = list(X)
# print(X_list)
X_values = list(X.values())
X

# Display the data in raw text (Optional to do so)
st.subheader("2. Print text")
full_forms = {'A': 'adenine (A)', 'C': 'thymine (cytosine)', 'T': 'thymine (T)', 'G': 'adenine (guamine)'}

for ch in 'ATGC':
    st.write(f"There are {str(X[ch])} {full_forms[ch]}")

# Display the data in a dataframe which is better in readability
st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient='index')
# print(df[:5])
df.rename({0: 'count'}, axis = 'columns', inplace=True)
# print(df[:5])
df.reset_index(inplace=True) # the original index becomes a column now
# print(df)
df.rename(columns={'index':'Nucleotide'}, inplace=True)
# print(df)
st.write(df)

# Graph using Altair
st.subheader("4. Display Bar Chart")
p = alt.Chart(df).mark_bar().encode(x='Nucleotide', y='count')
p = p.properties(width=alt.Step(80)) # 80 otherwise bars would be thin
st.write(p)
