import gradio as gr


def chatbot(message):
    message = message.lower().strip()

    # Greeting
    if any(word in message for word in ["hello", "hi", "hey"]):
        return """Hello! 👋

Welcome to Student Research Assistant.

I can help you with:

📄 Research Papers
📚 Journal Papers
🔗 DOI
📖 Reading Research Papers
💡 Research Topics

What would you like to know?"""

    # DOI
    elif "doi" in message:
        return """🔗 DOI — Digital Object Identifier

A DOI is a unique and permanent identifier assigned
to a research publication.

You can use a DOI to:
• Identify a specific research paper
• Locate the paper online
• Verify publication information

Example:
10.xxxx/xxxxx"""

    # Finding papers
    elif any(word in message for word in [
        "find paper",
        "find papers",
        "search paper",
        "search papers",
        "journal paper",
        "journal papers"
    ]):
        return """📚 Finding Journal Papers

You can search for research papers using:

1. Google Scholar
2. IEEE Xplore
3. ScienceDirect
4. SpringerLink
5. PubMed

When checking a paper, look for:
• Journal name
• Publication year
• Volume and issue
• DOI
• Authors"""

    # Reading papers
    elif any(word in message for word in [
        "read paper",
        "read research",
        "how to read"
    ]):
        return """📖 How to Read a Research Paper

Follow this order:

1. Read the title
2. Read the abstract
3. Identify the research problem
4. Understand the methodology
5. Check the dataset
6. Examine the results
7. Identify limitations
8. Read the conclusion

Tip: Don't try to understand every technical detail
during your first reading."""

    # Research topic
    elif any(word in message for word in [
        "research topic",
        "choose topic",
        "select topic",
        "topic selection"
    ]):
        return """💡 Choosing a Research Topic

Consider these factors:

1. Your area of interest
2. Recent research trends
3. Research gaps
4. Dataset availability
5. Technical feasibility
6. Available time and resources

A good research topic should address
a clear and meaningful research problem."""

    # Research paper definition
    elif any(word in message for word in [
        "what is a research paper",
        "research paper meaning",
        "define research paper"
    ]):
        return """📄 What is a Research Paper?

A research paper is a scholarly document
that presents original research, analysis,
findings, or a review of existing research
on a specific topic.

A typical research paper contains:

• Abstract
• Introduction
• Literature Review
• Methodology
• Results
• Discussion
• Conclusion
• References"""

    # Fallback
    else:
        return """🤔 I'm not sure how to answer that.

I can currently help you with:

📄 Research Papers
📚 Journal Papers
🔗 DOI
📖 Reading Research Papers
💡 Research Topics

Try asking something like:

"What is DOI?"
"How do I find journal papers?"
"How do I read a research paper?"
"How do I choose a research topic?"
"""


demo = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(
        label="Ask your question",
        placeholder="Example: What is DOI?"
    ),
    outputs=gr.Textbox(
        label="Chatbot Response"
    ),
    title="🎓 Student Research Assistant",
    description="Ask questions about research papers, journals, DOI, and research topics."
)

demo.launch()
