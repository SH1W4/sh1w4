"""
SH1W4 Profile README Generator
Automatically generates the projects section from projects.json
"""
import json

def load_projects():
    with open('projects.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_mermaid_graph(data):
    """Generate the Pure Architectural Manifest (Maximum Privacy)"""
    # This version ignores literal names and focuses on functional architecture
    lines = [
        "```mermaid",
        "graph LR",
        "    %% Themes & Styles (Pure Cyberpunk Architecture)",
        "    classDef core fill:#000,stroke:#00ff41,stroke-width:2px,color:#fff,font-weight:bold;",
        "    classDef agent fill:#111,stroke:#bd93f9,stroke-width:1.5px,color:#ddd;",
        "    classDef tool fill:#111,stroke:#00d9ff,stroke-width:1px,color:#ddd;",
        "    classDef ethics fill:#111,stroke:#f1c40f,stroke-width:1.5px,color:#fff;",
        "    classDef research fill:#111,stroke:#ff5555,stroke-width:1px,color:#ddd;",
        "",
        "    User((USER)):::core -->|Directives| Core[SH1W4 / CORE]:::core",
        "",
        "    subgraph INTELLIGENCE_LAYER",
        "        Core --> VIREON[🧬 AGENTIC_ORCHESTRATOR]:::agent",
        "        Core --> TRINITY[🧠 COGNITIVE_PROCESSOR]:::agent",
        "    end",
        "",
        "    subgraph TOOL_LAYER",
        "        direction TB",
        "        VIREON --> DX_KIT[👁️ DEV_EXP_MODULE]:::tool",
        "        VIREON --> ARKITECH[🏗️ STRAT_INFRA_TOOL]:::tool",
        "    end",
        "",
        "    subgraph DOMAIN_LAYER",
        "        VIREON --> LEGAL[⚖️ LEGAL_INTEL_CORE]:::agent",
        "        LEGAL --> SHIELD[🛡️ IP_GUARD_PROTOCOL]:::tool",
        "    end",
        "",
        "    subgraph ETHICS_GOVERNANCE",
        "        SEVE[⚖️ SEVE_ALIGNMENT_FWK]:::ethics",
        "    end",
        "",
        "    subgraph RESEARCH_LABS",
        "        direction TB",
        "        BIO[🔬 BIO_COMPUTATION_R&D]:::research",
        "        PROTO[📐 SEMANTIC_STANDARDS]:::research",
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
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
    
    print("✅ README.md updated with Neural Project Map!")

if __name__ == "__main__":
    generate_readme()
