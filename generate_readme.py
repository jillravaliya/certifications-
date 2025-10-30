import glob
from datetime import datetime

def clean_name(filename):
“”“Clean up filename for display”””
name = filename.replace(’.pdf’, ‘’)
name = name.replace(’%20’, ’ ‘)
name = name.replace(’_’, ’ ‘)
name = name.replace(’-’, ’ ’)
return name

def get_month_year(filename):
“”“Extract or estimate date from filename or return current date”””
# You can customize this to extract dates from your filenames
# For now, returns current date
return datetime.now().strftime(’%B %Y’)

def generate_readme():
# Get all PDF files
pdfs = glob.glob(’*.pdf’)
pdfs.sort()

```
cert_count = len(pdfs)
last_updated = datetime.now().strftime('%B %Y')

# Build README
readme = f"""<div align="center">
```

# 🏆 My Certifications

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=00D9FF&center=true&vCenter=true&random=false&width=600&lines=Professional+Certifications;Continuous+Learning+Journey;Technology+%26+Development" alt="Typing SVG" />

-----

### 📚 Certificate Collection

</div>

“””

```
# Add each certificate
for pdf in pdfs:
    cert_name = clean_name(pdf)
    date = get_month_year(pdf)
    
    # Determine issuer from filename (basic logic)
    issuer = "Professional Organization"
    if 'linux' in pdf.lower() or 'lfs' in pdf.lower():
        issuer = "**The Linux Foundation**"
    elif 'google' in pdf.lower() or 'networking' in pdf.lower():
        issuer = "**Google via Coursera**"
    elif 'meta' in pdf.lower():
        issuer = "**Meta**"
    elif 'aws' in pdf.lower():
        issuer = "**Amazon Web Services**"
    elif 'azure' in pdf.lower():
        issuer = "**Microsoft Azure**"
    elif 'docker' in pdf.lower():
        issuer = "**Docker**"
    elif 'python' in pdf.lower():
        issuer = "**Python Institute**"
    
    readme += f"## {cert_name}\n\n"
    readme += f"{issuer} | {date}\n\n"

readme += f"""---
```

<div align="center">

## 📊 Repository Stats

![Total Certificates](https://img.shields.io/badge/Total%20Certificates-{cert_count}-brightgreen?style=for-the-badge&logo=bookmeter)
![Last Updated](https://img.shields.io/badge/Last%20Updated-{last_updated}-blue?style=for-the-badge&logo=github)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</div>

-----

<div align="center">

### 🎯 About This Repository

This repository automatically showcases all my professional certifications.  
Just upload a certificate PDF and it appears here instantly!

### 🚀 Technologies & Skills

![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Networking](https://img.shields.io/badge/Networking-0078D4?style=flat-square&logo=googlecloud&logoColor=white)
![Cloud](https://img.shields.io/badge/Cloud-FF9900?style=flat-square&logo=amazon&logoColor=white)

-----

**Keep Learning, Keep Growing!** 🌱

*Auto-generated repository - No manual updates needed*

</div>"""

```
# Write to file
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print(f"✅ README generated with {cert_count} certificates!")
for pdf in pdfs:
    print(f"   📄 {clean_name(pdf)}")
```

if **name** == “**main**”:
generate_readme()
