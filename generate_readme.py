import os
import glob
from datetime import datetime

def generate_readme():
# Get all PDF files (certificates)
pdfs = glob.glob(’*.pdf’)
pdfs.sort()

```
# Start README content
readme = """# 🏆 My Certifications
```

Welcome to my certifications repository! This is a collection of all professional certificates and courses I’ve completed.

## 📜 All Certificates

“””

```
# Auto-add each certificate
for pdf in pdfs:
    # Clean filename for display (remove .pdf and replace special chars)
    cert_name = pdf.replace('.pdf', '')
    cert_name = cert_name.replace('%20', ' ')
    cert_name = cert_name.replace('_', ' ')
    cert_name = cert_name.replace('-', ' ')
    
    # Add to README
    readme += f"### {cert_name}\n"
    readme += f"![{cert_name}]({pdf})\n\n"
    readme += "---\n\n"

# Add footer with stats
readme += f"""## 🎯 About This Repository
```

This repository serves as a centralized location to store and showcase all my professional certifications. It automatically updates whenever new certificates are added!

## 📊 Stats

- **Total Certificates:** {len(pdfs)}
- **Last Updated:** {datetime.now().strftime(’%B %d, %Y at %I:%M %p’)}

## 🚀 How It Works

1. Just upload any certificate PDF to this repository
1. The README automatically updates to show it
1. No manual editing needed!

-----

**Keep learning, keep growing!** 🚀

*This README is auto-generated. Upload certificates and forget about it!*
“””

```
# Write README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print(f"✅ README generated with {len(pdfs)} certificates!")
for pdf in pdfs:
    print(f"   📄 {pdf}")
```

if **name** == “**main**”:
generate_readme()
