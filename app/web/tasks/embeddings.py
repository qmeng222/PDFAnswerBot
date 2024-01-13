from celery import shared_task # import the shared_task decorator from the Celery library
from app.web.db.models import Pdf
from app.web.files import download
from app.chat.create_embeddings import create_embeddings_for_pdf

# the decorator function takes the original function as an argument and returns a new function with the desired modifications:
@shared_task()
def process_document(pdf_id: int):
    pdf = Pdf.find_by(id=pdf_id)
    with download(pdf.id) as pdf_path:
        create_embeddings_for_pdf(pdf.id, pdf_path)
