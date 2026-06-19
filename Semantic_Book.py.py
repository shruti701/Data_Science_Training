"""Dashboard app with filters and gr.Gallery output.


Same layout pattern as the GenAI-project book recommender dashboard.
Run: python g4_gallery_demo.py
"""


import gradio as gr


BOOKS = [
    {
        "title": "The Nature Explorer",
        "author": "Jane Miller",
        "category": "Children's Nonfiction",
        "tone": "Happy",
        "description": "A curious child discovers forests, rivers, and wildlife on weekend adventures.",
        "thumbnail": "https://picsum.photos/seed/nature/100/140",
    },
    {
        "title": "Shadows in the Library",
        "author": "Tom Reed",
        "category": "Fiction",
        "tone": "Suspenseful",
        "description": "A librarian uncovers secrets hidden between the shelves of a centuries-old building.",
        "thumbnail": "https://picsum.photos/seed/library/100/140",
    },
    {
        "title": "Forgiveness Road",
        "author": "Amina Khan",
        "category": "Fiction",
        "tone": "Sad",
        "description": "Two siblings reunite after years apart and learn to heal old wounds.",
        "thumbnail": "https://picsum.photos/seed/forgive/100/140",
    },
    {
        "title": "Quantum Questions",
        "author": "Dr. Lee Park",
        "category": "Nonfiction",
        "tone": "Surprising",
        "description": "An accessible tour of quantum physics for curious beginners.",
        "thumbnail": "https://picsum.photos/seed/quantum/100/140",
    },
    {
        "title": "Laughing Lab Coats",
        "author": "Chris & Dana Wu",
        "category": "Nonfiction",
        "tone": "Happy",
        "description": "Funny stories from real scientists about experiments gone wrong.",
        "thumbnail": "https://picsum.photos/seed/lab/100/140",
    },
    {
        "title": "Storm Over Harbor",
        "author": "Elena Voss",
        "category": "Fiction",
        "tone": "Angry",
        "description": "A fishing town fights corruption as a hurricane approaches the coast.",
        "thumbnail": "https://picsum.photos/seed/storm/100/140",
    },
]


CATEGORIES = ["All"] + sorted({b["category"] for b in BOOKS})
TONES = ["All", "Happy", "Surprising", "Angry", "Suspenseful", "Sad"]




def search_books(query: str, category: str, tone: str) -> list[tuple[str, str]]:
    """Filter books by keyword, category, and tone.


    Returns a list of (image_url, caption) tuples for gr.Gallery.
    """
    query_words = set(query.lower().split()) if query.strip() else set()
    results = []


    for book in BOOKS:
        text = f"{book['title']} {book['description']}".lower()
        if query_words and not query_words & set(text.split()):
            continue
        if category != "All" and book["category"] != category:
            continue
        if tone != "All" and book["tone"] != tone:
            continue


        caption = f"{book['title']} by {book['author']}: {book['description'][:80]}..."
        results.append((book["thumbnail"], caption))


    if not results:
        return [("https://picsum.photos/seed/empty/100/140", "No books matched your filters.")]


    return results




with gr.Blocks(theme=gr.themes.Glass()) as demo:
    gr.Markdown("# Book Recommender")
    gr.Markdown("Describe a book, pick filters, and browse recommendations.")


    with gr.Row():
        user_query = gr.Textbox(
            label="Describe a book",
            placeholder="e.g. nature adventure for children",
            scale=2,
        )
        category_dropdown = gr.Dropdown(
            choices=CATEGORIES,
            value="All",
            label="Category",
        )
        tone_dropdown = gr.Dropdown(
            choices=TONES,
            value="All",
            label="Emotional tone",
        )
        submit_button = gr.Button("Find recommendations", variant="primary")


    gr.Markdown("## Recommendations")
    output = gr.Gallery(
        label="Recommended books",
        columns=5,
        rows=2,
        height=320,
        object_fit="contain",
        allow_preview=True,
        fit_columns=False,
    )


    submit_button.click(
        fn=search_books,
        inputs=[user_query, category_dropdown, tone_dropdown],
        outputs=output,
    )


if __name__ == "__main__":
    demo.launch()


