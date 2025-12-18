"""
SH1W4 Profile README Generator
Automatically generates the projects section from projects.json
"""
import json

def load_projects():
    with open('projects.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_mermaid_graph(data):
    """Generate Mermaid graph from projects data"""
    featured = data.get('featured', [])
    additional = data.get('additional', [])
    all_projects = featured + additional
    
    lines = [
        "```mermaid",
        "graph TD",
        "    %% Styles",
        "    classDef core fill:#0d1117,stroke:#00ff41,stroke-width:2px,color:#fff,font-weight:bold;",
        "    classDef infra fill:#161b22,stroke:#bd93f9,stroke-width:1.5px,color:#fff;",
        "    classDef tool fill:#161b22,stroke:#00d9ff,stroke-width:1px,color:#ddd;",
        "    classDef legal fill:#161b22,stroke:#f1c40f,stroke-width:1.5px,color:#fff;",
        "    classDef stable stroke-dasharray: 0;",
        "    classDef alpha stroke-dasharray: 5 5;",
        "    classDef active stroke:#00ff41;",
        "",
        "    HUB((SH1W4 CORE)):::core",
        ""
    ]
    
    # Organize by type
    categories = {
        "Infrastructure": [],
        "Agentic Tool": [],
        "Legal AI": [],
        "Deep Tech": [],
        "Research AI": [],
        "MCP Server": []
    }
    
    for p in all_projects:
        cat = p.get('type', 'Other')
        if cat not in categories: categories[cat] = []
        categories[cat].append(p)
        
    # Build Subgraphs
    subgraph_map = {
        "Infrastructure": ("INFRA_LAYER", "infra"),
        "MCP Server": ("INFRA_LAYER", "infra"),
        "Agentic Tool": ("UTILITY_LAYER", "tool"),
        "Research AI": ("UTILITY_LAYER", "tool"),
        "Legal AI": ("DOMAIN_LAYER", "legal"),
        "Deep Tech": ("DOMAIN_LAYER", "legal")
    }
    
    layers = {}
    for cat, projs in categories.items():
        if not projs: continue
        layer_id, style_class = subgraph_map.get(cat, ("OTHER_LAYER", "tool"))
        if layer_id not in layers: layers[layer_id] = []
        layers[layer_id].extend([(p, style_class) for p in projs])

    for layer_id, p_list in layers.items():
        lines.append(f"    subgraph {layer_id}")
        for p, style in p_list:
            p_id = p['name'].replace(" ", "_").upper()
            status_style = "alpha" if "Alpha" in p['status'] or "Beta" in p['status'] else "stable"
            lines.append(f"        {p_id}[\"{p.get('icon', '')} {p['name']}\"]:::{style}")
            lines.append(f"        class {p_id} {status_style}")
        lines.append("    end")
        lines.append(f"    HUB --> {layer_id}")
        lines.append("")

    lines.append("```")
    return "\n".join(lines)

def generate_readme():
    """Generate the full README.md"""
    data = load_projects()
    
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except:
        readme_content = ""
    
    # Generate projects graph
    projects_md = generate_mermaid_graph(data)
    
    import re
    
    # Target the Mermaid block within the SYSTEM_MANIFEST section
    # We look for the start of the manifest and the mission protocol mission block
    start_marker = "### 📂 S Y S T E M _ M A N I F E S T"
    end_marker = "> **MISSION PROTOCOL:**"
    
    if start_marker in readme_content and end_marker in readme_content:
        # Construct pattern to find the mermaid block between these markers
        pattern = re.escape(start_marker) + r".*?```mermaid.*?```"
        
        # New manifest content: Header + SVG + Graph
        new_manifest = f"{start_marker} (Symbeon Ecosystem)\n\n"
        new_manifest += '<div align="center">\n'
        new_manifest += '    <img src="./neural_network.svg" width="80%" alt="Symbeon Neural Fabric"/>\n'
        new_manifest += '</div>\n\n'
        new_manifest += projects_md
        
        new_readme = re.sub(pattern, new_manifest, readme_content, flags=re.DOTALL)
    else:
        print("⚠️ Markers not found. Appending to end.")
        new_readme = readme_content + "\n\n" + projects_md
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
    
    print("✅ README.md updated with Neural Project Map!")

if __name__ == "__main__":
    generate_readme()
