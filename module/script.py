import streamlit as st

def decorator(func):
    def wrapper(*args, **kwargs) -> str:
        
        st.info("MISS")
        return f"{func()} is cached"

    return wrapper

@st.cache
@decorator
def foo():
    return "foo"


@st.cache
@decorator
def bar():
    return "bar"



def run():
    st.write(foo())
    st.write(bar())
