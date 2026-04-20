import os

directory = r'c:\Users\LENOVO\Desktop\art otc'
favicon_tag = '\n    <link rel="icon" type="image/png" href="im/X9.png">'

files_modified = 0

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if favicon already exists
        if '<link rel="icon"' in content:
            print(f"Favicon already exists in {filename}, skipping.")
            continue
            
        # Insert after </title>
        if '</title>' in content:
            new_content = content.replace('</title>', '</title>' + favicon_tag)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added favicon to {filename}")
            files_modified += 1
        else:
            print(f"Could not find </title> tag in {filename}")

print(f"Total files modified: {files_modified}")
