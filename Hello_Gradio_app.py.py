"""Minimal Gradio app using gr.Interface.


To install library in venv, use: pip install gradio


Wraps a Python function with automatic input/output widgets.
Run: python g1_interface_demo.py
"""


import gradio as gr


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    if not name or not name.strip():
        return "Please enter your name."
    return f"Hello, {name.strip()}! Welcome to Gradio."




demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your name", placeholder="e.g. Ada"),
    outputs=gr.Textbox(label="Greeting"),
    title="Hello Gradio",
    description="Type your name and see the greeting update.",
    # flagging_mode="never", # manual/never/auto
)


if __name__ == "__main__":
    demo.launch()
