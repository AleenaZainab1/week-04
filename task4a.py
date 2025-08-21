import gradio as gr

# Function: Character count
def char_count(text):
    return len(text)

# Gradio Interface
demo = gr.Interface(
    fn=char_count,
    inputs="text",
    outputs="number",
    title="Text Analyzer - Character Count",
    description="Enter any text and get the total number of characters."
)

# Launch App
demo.launch()
