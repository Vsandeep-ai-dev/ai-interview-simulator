from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_feedback_pdf(feedback, filename="interview_feedback.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    textobject = c.beginText(40, 750)
    textobject.setFont("Helvetica", 12)

    for line in feedback.split("\n"):
        textobject.textLine(line)

    c.drawText(textobject)
    c.save()

