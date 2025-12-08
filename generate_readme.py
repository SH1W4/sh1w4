"""
SH1W4 Profile README Generator
Automatically generates the projects section from projects.json
"""
import json

def load_projects():
    with open('projects.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_projects_table(projects):
    """Generate markdown table from projects list"""
    lines = []
    lines.append("| PROJECT | TYPE | DESCRIPTION | STATUS |")
    lines.append("| :--- | :--- | :--- | :--- |")
    
    for project in projects:
        icon = project.get('icon', '')
        name = project['name']
        url = project['url']
        proj_type = project['type']
        desc = project['description']
        status = project['status']
        
        line = f"| **[{icon} {name}]({url})** | `{proj_type}` | {desc} | {status} |"
        lines.append(line)
    
    return "\n".join(lines)

def generate_readme():
    """Generate the full README.md"""
    data = load_projects()
    
    # Read template or current README to preserve other sections
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except:
        readme_content = ""
    
    # Generate projects section
    projects_md = generate_projects_table(data['featured'])
    
    # Find and replace the projects section
    # Look for the table between "S E L E C T E D _ W O R K S" and the next "---"
    import re
    
    pattern = r'(### S E L E C T E D _ W O R K S\s*\n\n)(.*?)(\n\n<br/>)'
    
    replacement = f'\\1{projects_md}\\3'
    
    new_readme = re.sub(pattern, replacement, readme_content, flags=re.DOTALL)
    
    # Write back
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
    
    print("✅ README.md updated successfully!")
    print(f"✅ Featured {len(data['featured'])} projects")
    if 'additional' in data and data['additional']:
        print(f"ℹ️  {len(data['additional'])} additional projects available in projects.json")

if __name__ == "__main__":
    generate_readme()
