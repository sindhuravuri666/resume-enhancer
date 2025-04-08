import streamlit as st
from huggingface_hub import InferenceClient

# Initialize client with model
client = InferenceClient("HuggingFaceH4/zephyr-7b-alpha")

def improve_bullet(task: str) -> str:
    prompt = (
        "<|system|>You are a helpful assistant that rewrites work tasks into professional resume bullet points.\n"
        f"<|user|>Rewrite this into a resume bullet point:\n{task}\n"
        "<|assistant|>"
    )
    try:
        output = client.text_generation(prompt, max_new_tokens=100, temperature=0.7)
        return output.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# Streamlit UI
st.title("💼 Resume Bullet Improver")

task = st.text_area("Enter your work task:")

if st.button("Improve"):
    if task.strip():
        result = improve_bullet(task)
        st.markdown(f"**💼 Resume Output:**\n\n{result}")
    else:
        st.warning("Please enter a task first.")
