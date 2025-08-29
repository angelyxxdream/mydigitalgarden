import fitz
import os
import json

pdf_path = "pdfs/gallery.pdf"
output_folder = "images_from_pdf"
os.makedirs(output_folder, exist_ok=True)

# Open PDF
doc = fitz.open(pdf_path)

# Extract images
for page_num in range(len(doc)):
    page = doc[page_num]
    images = page.get_images(full=True)

    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        ext = base_image["ext"]
        image_filename = f"{output_folder}/page{page_num+1}_{img_index}.{ext}"

        with open(image_filename, "wb") as f:
            f.write(image_bytes)

        print("saved", image_filename)

# Generate JSON
items = []

for filename in sorted(os.listdir(output_folder)):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        items.append({
            "type": "image",
            "src": f"{output_folder}/{filename}",
            "title": filename.split('.')[0].capitalize()
        })

# Add PDF itself
items.append({
    "type": "pdf",
    "src": pdf_path,
    "title": "Download full PDF"
})

with open("gallery.json", "w") as f:
    json.dump(items, f, indent=2)

print("gallery.json created with", len(items), "items")
