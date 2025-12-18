"""
SH1W4 Profile README Generator
Automatically generates the projects section from projects.json
"""
import json

def load_projects():
    with open('projects.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_mermaid_graph(data):
    """Generate the Pure Architectural Manifest with Access Levels"""
    lines = [
        "```mermaid",
        "graph LR",
        "    %% Themes & Styles (Pure Cyberpunk Architecture)",
        "    classDef core fill:#000,stroke:#00ff41,stroke-width:2px,color:#fff,font-weight:bold;",
        "    classDef agent fill:#111,stroke:#bd93f9,stroke-width:1.5px,color:#ddd;",
        "    classDef tool fill:#111,stroke:#00d9ff,stroke-width:1px,color:#ddd;",
        "    classDef ethics fill:#111,stroke:#f1c40f,stroke-width:1.5px,color:#fff;",
        "    classDef research fill:#111,stroke:#ff5555,stroke-width:1px,color:#ddd;",
        "    classDef restricted fill:#0d1117,stroke:#333,color:#666,stroke-dasharray: 5 5;",
        "",
        "    User((USER)):::core -->|Directives| Core[SH1W4 / CORE]:::core",
        "",
        "    subgraph INTELLIGENCE_LAYER",
        "        Core --> VIREON[\"🧬 AGENTIC_ORCHESTRATOR <br/> [ACCESS: L1]\"]:::agent",
        "        Core --> TRINITY[\"🧠 COGNITIVE_PROCESSOR <br/> [ACCESS: L1]\"]:::agent",
        "    end",
        "",
        "    subgraph TOOL_LAYER",
        "        direction TB",
        "        VIREON --> DX_KIT[\"👁️ DEV_EXP_MODULE <br/> [ACCESS: L1]\"]:::tool",
        "        VIREON --> ARKITECH[\"🏗️ STRAT_INFRA_TOOL <br/> [ACCESS: L1]\"]:::tool",
        "        VIREON -.-> RD_TOOLS[\"📡 R&D_EXTENSIONS <br/> [ACCESS: RESTRICTED]\"]:::restricted",
        "    end",
        "",
        "    subgraph DOMAIN_LAYER",
        "        VIREON --> LEGAL[\"⚖️ LEGAL_INTEL_CORE <br/> [ACCESS: L1]\"]:::agent",
        "        LEGAL --> SHIELD[\"🛡️ IP_GUARD_PROTOCOL <br/> [ACCESS: L1]\"]:::tool",
        "        VIREON -.-> RD_DOMAIN[\"⚖️ LEGAL_TECH_R&D <br/> [ACCESS: RESTRICTED]\"]:::restricted",
        "    end",
        "",
        "    subgraph ETHICS_GOVERNANCE",
        "        SEVE[\"⚖️ SEVE_ALIGNMENT_FWK <br/> [ACCESS: L1]\"]:::ethics",
        "    end",
        "",
        "    subgraph RESEARCH_LABS",
        "        direction TB",
        "        BIO[\"🔬 BIO_COMPUTATION_R&D <br/> [ACCESS: L2]\"]:::research",
        "        PROTO[\"📐 SEMANTIC_STANDARDS <br/> [ACCESS: L2]\"]:::research",
        "    end",
        "",
        "    %% Strategic Relationship Links",
        "    SEVE -.->|Guards| TRINITY",
        "    SEVE -.->|Aligns| VIREON",
        "    BIO -.->|Data| TRINITY",
        "    PROTO -.->|Specs| VIREON",
        "    DX_KIT -.->|Telemetry| Core",
        "",
        "```"
    ]
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
    
    # Target the Dashboard section to add telemetry
    dashboard_pattern = r'(<img src="\./biostats\.svg".*?\/>)'
    telemetry_md = '\n<br/>\n<h3><code>🧠 COGNITIVE_PULSE</code></h3>\n<img src="./telemetry.svg" width="90%" alt="Cognitive Telemetry"/>'
    
    new_readme = re.sub(dashboard_pattern, f'\\1{telemetry_md}', new_readme, flags=re.DOTALL)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
    
    print("✅ README.md updated with Neural Project Map!")

if __name__ == "__main__":
    generate_readme()
