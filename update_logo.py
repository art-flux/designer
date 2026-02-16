import os
import re

directory = r'c:\Users\LENOVO\Desktop\art otc'
logo_replacement = '''<div class="container mx-auto px-2 py-2 flex justify-between items-center">
            <a href="index.html" class="flex items-center"><img src="im/x8.png" alt="ART FLUX DESIGNER"
                    class="h-[60px] w-auto"></a>'''

# Pattern to match the existing logo section
# Matches <div class="container mx-auto ... flex justify-between items-center">
# Followed by <a href="index.html" ...><img ...></a>
pattern = re.compile(
    r'<div class="container mx-auto .*? flex justify-between items-center">\s*'
    r'<a href="index.html" class="flex items-center"><img src="im/x8\.png" alt="ART FLUX DESIGNER"\s*'
    r'class="h-\[\d+px\] w-auto"></a>',
    re.DOTALL
)

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if pattern.search(content):
            print(f"Updating {filename}...")
            new_content = pattern.sub(logo_replacement, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        else:
            print(f"Pattern not found in {filename}")

