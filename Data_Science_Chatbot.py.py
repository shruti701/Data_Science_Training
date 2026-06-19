"""Chat UI using gr.ChatInterface.


The chat function receives the latest message and full conversation history.
Run: python g3_chat_demo.py
"""


import gradio as gr




def chat(message: str, history) -> str:
    """Respond to the user message using simple rules (stand-in for an LLM).


    Args:
        message: The user's latest input.
        history: Prior turns — list of (user, assistant) pairs or message dicts.


    Returns:
        Assistant reply text shown in the chat window.
    """
    if not message or not message.strip():
        return ""


    user_text = message.strip().lower()


    if "hello" in user_text:
        return "Hello! Ask me about pandas, ML, or Gradio."
    if "pandas" in user_text:
        return "Pandas is Python's tabular data library. Start with pd.read_csv() and .head()."
    if "gradio" in user_text:
        return "Gradio wraps Python functions in a web UI. ChatInterface is built for chat apps."
    if "history" in user_text:
        turn_count = len(history) if history else 0
        return f"This conversation has {turn_count} previous turn(s) in history."


    return (
        f"You asked: \"{message.strip()}\"\n\n"
        "In a full chatbot, this function would call an LLM with the conversation history."
    )




demo = gr.ChatInterface(
    fn=chat,
    title="Data Science Chat",
    description="A simple chat UI built with gr.ChatInterface.",
    examples=["What is pandas?", "How does Gradio work?", "How many messages in history?"],
)


if __name__ == "__main__":
    demo.launch()
