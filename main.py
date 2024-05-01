# Set your Cloudinary credentials
# import the CLOUDINARY_URL from .env
# ==============================
from dotenv import load_dotenv
load_dotenv()

# Import the Cloudinary libraries
# ==============================
import cloudinary
import cloudinary.uploader

file_name = "videos/short_video.mp4"

response = cloudinary.uploader.upload_large(file_name,
    resource_type = "video")

print(response["secure_url"])

file_name = "videos/long_video.mp4"

response = cloudinary.uploader.upload_large(file_name,
    resource_type = "video",
    chunk_size = 6000000)

print(response["secure_url"])