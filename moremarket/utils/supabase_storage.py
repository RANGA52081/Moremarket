from supabase import create_client
from django.conf import settings
import uuid

supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_KEY
)

def upload_image_to_supabase(file):
    file_extension = file.name.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{file_extension}"

    supabase.storage.from_(settings.SUPABASE_BUCKET).upload(
        unique_filename,
        file.read(),
        {"content-type": file.content_type}
    )

    public_url = supabase.storage.from_(settings.SUPABASE_BUCKET).get_public_url(unique_filename)

    return public_url