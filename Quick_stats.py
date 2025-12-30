import streamlit as st
import numpy as np
from collections import Counter

st.title("📊 Statistical Calculator")

clean = lambda x: int(x) if x.is_integer() else round(x, 2)

data = st.text_input("Enter values (comma separated)")

if data.strip() != "":
    arr = np.array([float(x.strip()) for x in data.split(",")])
    s = np.sort(arr)

    mean = arr.mean()
    median = np.median(arr)
    mode = Counter(arr).most_common(1)[0][0]
    var = arr.var()
    std = arr.std()
    
    st.write("**Values:**", ", ".join(str(clean(x)) for x in arr))
    st.
    write("**Sorted:**", ", ".join(str(clean(x)) for x in s))

    st.markdown("### Mean")
    st.latex(r"\text{Mean }(\bar{x}) = \frac{\sum x}{n}")
    st.write(f"Mean = {clean(mean)}")


    st.markdown("### Median")
    st.write(f"Median = {clean(median)}")


    st.markdown("### Mode")
    st.write(f"Mode = {clean(mode)}")


    st.markdown("### Variance")
    st.latex(r"\text{Variance }(\sigma^2) = \frac{\sum (x-\bar{x})^2}{n}")
    st.write(f"Variance = {round(var,2)}")


    st.markdown("### Standard Deviation")
    st.latex(r"\text{Std Dev }(\sigma) = \sqrt{\frac{\sum (x-\bar{x})^2}{n}}")
    st.write(f"Std Dev = {round(std,2)}")
