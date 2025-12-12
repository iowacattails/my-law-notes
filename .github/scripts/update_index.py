#!/usr/bin/env python3
import os
import glob
import frontmatter
from datetime import datetime

# Path to notes and index
notes_dir = 'notes'
index_file = 'index.html'

# Get all .md files in notes/, sorted by date (newest first)
md_files = glob.glob(os.path.join(notes_dir, '*.md'))
posts = []

for md_path in md_files:
    with open(md_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
        metadata = post.metadata
        content = post.content
        
        # Extract title, date, image (assume frontmatter has title, date, image)
        title = metadata.get('title', os.path.basename(md_path).replace('.md', 'Untitled'))
        date_str = metadata.get('date', datetime.now().strftime('%Y-%m-%d'))
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
        except:
            date = datetime.now()
        
        image = metadata.get('image', '')  # e.g., 'images/my-pic.jpg'
        excerpt = content.split('\n')[0].strip() if content else ''
        
        posts.append({
            'title': title,
            'date': date,
            'url': os.path.basename(md_path).replace('.md', ''),
            'image': image,
            'excerpt': excerpt
        })

# Sort by date, newest first
posts.sort(key=lambda p: p['date'], reverse=True)

# Read current index.html template (assume it has a placeholder like <!-- POSTS -->)
with open(index_file, 'r', encoding='utf-8') as f:
    template = f.read()

# Generate HTML for posts list
posts_html = '<ul class="notes-list">\n'
for post in posts:
    img_tag = f'<img src="{post["image"]}" alt="{post["title"]}" class="thumb">' if post['image'] else ''
    posts_html += f'  <li>\n    <h3><a href="/{post["url"]}.html">{post["title"]}</a></h3>\n'
    posts_html += f'    <p class="date">{post["date"].strftime("%Y-%m-%d")}</p>\n'
    posts_html += f'    {img_tag}\n    <p class="excerpt">{post["excerpt"]}</p>\n  </li>\n'
posts_html += '</ul>'

# Replace placeholder in template (adjust if your index uses a different marker)
updated_index = template.replace('<!-- POSTS HERE -->', posts_html)

# Write back if changed
with open(index_file, 'w', encoding='utf-8') as f:
    f.write(updated_index)

print(f"Updated index with {len(posts)} posts.")
