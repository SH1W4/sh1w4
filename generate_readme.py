"""
SH1W4 Profile README Generator
Automatically generates the projects section from projects.json
"""
import json

def load_projects():
    with open('projects.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_mermaid_graph(data):
    """Generate the Synthesized Symbeon Ecosystem Map (Privacy-First)"""
    featured = data.get('featured', [])
    additional = data.get('additional', [])
    
    # Track categories for abstract nodes
    add_categories = {}
    for p in additional:
        cat = p.get('type', 'Other')
        add_categories[cat] = add_categories.get(cat, 0) + 1

    lines = [
        "```mermaid",
        "graph LR",
        "    %% Themes & Styles",
        "    classDef core fill:#000,stroke:#00ff41,stroke-width:2px,color:#fff,font-weight:bold;",
        "    classDef agent fill:#111,stroke:#bd93f9,stroke-width:1.5px,color:#ddd;",
        "    classDef tool fill:#111,stroke:#00d9ff,stroke-width:1px,color:#ddd;",
        "    classDef ethics fill:#111,stroke:#f1c40f,stroke-width:1.5px,color:#fff;",
        "    classDef research fill:#111,stroke:#ff5555,stroke-width:1px,color:#ddd;",
        "    classDef private fill:#0d1117,stroke:#333,stroke-width:1px,color:#666,stroke-dasharray: 5 5;",
        "",
        "    User((USER)):::core -->|Commands| Core[SH1W4 / CORE]:::core",
        "",
        "    subgraph INTELLIGENCE_LAYER",
        "        Core --> VIREON[\"🧬 VIREON Core\"]:::agent",
        "        Core --> TRINITY[\"🧠 TRINITY AI\"]:::agent",
        "    end",
        "",
        "    subgraph TOOL_LAYER",
        "        direction TB"
    ]

    # Map featured tools
    for p in featured:
        if p.get('type') in ['Agentic Tool', 'Research AI', 'MCP Server']:
            p_id = p['name'].replace(" ", "_").upper()
            lines.append(f"        VIREON --> {p_id}[\"{p.get('icon', '')} {p['name']}\"]:::tool")
    
    # Add localized R&D node for additional tools to maintain privacy
    if add_categories.get('Agentic Tool') or add_categories.get('MCP Server'):
        lines.append(f"        VIREON -.-> RD_TOOLS[\"📡 R&D_EXTENSIONS\"]:::private")

    lines.append("    end\n")
    lines.append("    subgraph DOMAIN_LAYER")
    
    # Map featured domain projects
    for p in featured:
        if p.get('type') in ['Legal AI', 'Deep Tech']:
            p_id = p['name'].replace(" ", "_").upper()
            lines.append(f"        VIREON --> {p_id}[\"{p.get('icon', '')} {p['name']}\"]:::agent")
            
    # Abstract node for additional domain R&D
    if add_categories.get('Legal AI') or add_categories.get('Deep Tech'):
        lines.append(f"        VIREON -.-> RD_DOMAIN[\"⚖️ LEGAL_TECH_R&D\"]:::private")

    lines.append("    end\n")
    lines.append("    subgraph ETHICS_GOVERNANCE")
    lines.append("        SEVE[\"⚖️ SEVE ALIGNMENT\"]:::ethics")
    lines.append("    end\n")
    
    lines.append("    subgraph RESEARCH_LABS")
    lines.append("        direction TB")
    lines.append("        BIO[\"🔬 BIO_COMP R&D\"]:::research")
    lines.append("        PROTO[\"📐 SEMANTIC_SPECS\"]:::research")
    lines.append("    end\n")

    lines.append("    %% Strategic Relationship Links")
    lines.append("    SEVE -.->|Guards| TRINITY")
    lines.append("    SEVE -.->|Aligns| VIREON")
    lines.append("    BIO -.->|Feeds| TRINITY")
    lines.append("    PROTO -.->|Standards| VIREON")
    lines.append("    ")
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
