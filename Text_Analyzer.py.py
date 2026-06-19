"""Gradio app with custom layout using gr.Blocks.


Shows Row layout, multiple inputs, and button.click event wiring.
Run: python g2_blocks_demo.py
"""


import gradio as gr




def analyze_text(text: str, word_limit: int, style: str) -> str:
    """Count words and return a formatted preview of the input text."""
    if not text or not text.strip():
        return "Enter some text to analyze."


    words = text.split()
    preview = " ".join(words[:word_limit])
    if len(words) > word_limit:
        preview += "..."


    return (
        f"Style: {style}\n"
        f"Word count: {len(words)}\n"
        f"Preview ({min(word_limit, len(words))} words):\n{preview}"
    )




with gr.Blocks(title="Text Analyzer") as demo:
    gr.Markdown("# Text Analyzer")
    gr.Markdown("Enter text, choose options, and click **Analyze**.")


    with gr.Row():
        text_input = gr.Textbox(
            label="Paste text",
            placeholder="The quick brown fox jumps over the lazy dog.",
            lines=3,
            scale=3,
        )
        word_limit = gr.Slider(
            minimum=3,
            maximum=20,
            value=8,
            step=1,
            label="Preview length (words)",
        )
        style = gr.Dropdown(
            choices=["Formal", "Casual", "Bullet summary"],
            value="Casual",
            label="Output style",
        )


    analyze_btn = gr.Button("Analyze", variant="primary")


    gr.Markdown("## Result")
    output = gr.Textbox(label="Analysis", lines=5)


    analyze_btn.click(
        fn=analyze_text,
        inputs=[text_input, word_limit, style],
        outputs=output,
    )


if __name__ == "__main__":
    demo.launch()
