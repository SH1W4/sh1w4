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
    
    # 1. STRATEGIC DIRECTIVE (Top Placement)
    directive_md = '\n<div align="center">\n    <img src="./directive.svg" width="100%" alt="Strategic Directive"/>\n</div>\n<br/>'
    if '<img src="./directive.svg"' not in readme_content:
        header_pattern = r'(<\/div>\n\n<br\/>)(\n\n<!-- DASHBOARD)'
        new_readme = re.sub(header_pattern, f'\\1{directive_md}\\2', readme_content, flags=re.DOTALL)
    else:
        new_readme = readme_content

    # 2. SYSTEM MANIFEST (Projects Graph)
    start_marker = "### 📂 S Y S T E M _ M A N I F E S T"
    pattern = re.escape(start_marker) + r".*?```mermaid.*?```"
    new_manifest = f"{start_marker} (Symbeon Ecosystem)\n\n"
    new_manifest += '<div align="center">\n'
    new_manifest += '    <img src="./neural_network.svg" width="80%" alt="Symbeon Neural Fabric"/>\n'
    new_manifest += '</div>\n\n'
    new_manifest += projects_md
    new_readme = re.sub(pattern, new_manifest, new_readme, flags=re.DOTALL)

    # 3. DASHBOARD TELEMETRY
    dashboard_pattern = r'(<img src="\./biostats\.svg".*?\/>)'
    if '<img src="./telemetry.svg"' not in new_readme:
        telemetry_md = '\n<br/>\n<h3><code>🧠 COGNITIVE_PULSE</code></h3>\n<img src="./telemetry.svg" width="90%" alt="Cognitive Telemetry"/>'
        new_readme = re.sub(dashboard_pattern, f'\\1{telemetry_md}', new_readme, flags=re.DOTALL)

    # 4. AGENT DOSSIERS (New Section after Manifest)
    if '### 👥 A G E N T _ D O S S I E R S' not in new_readme:
        dossiers_md = """
### 👥 A G E N T _ D O S S I E R S (Identity Core)

| IDENTITY | ROLE | COGNITIVE_PROFILE | PRIMARY_DIRECTIVE |
| :--- | :--- | :--- | :--- |
| **🧬 VIREON** | Orchestrator | Aggressive / Precise | Universal Scaling |
| **🧠 TRINITY** | Analytics | Reflective / Recursive | Pattern Synthesis |

---
"""
        new_readme = new_readme.replace("> **MISSION PROTOCOL:**", dossiers_md + "> **MISSION PROTOCOL:**")

    # 5. EVOLUTION JOURNEY (New Section after Methodology)
    if '### 🚀 E V O L U T I O N _ J O U R N E Y' not in new_readme:
        journey_md = """
### 🚀 E V O L U T I O N _ J O U R N E Y

```mermaid
graph TD
    V1[v1.0: THE KERNEL] -->|Agentic Infusion| V2[v2.0: THE ARCHITECT]
    V2 -->|Neural Scaling| V3[v3.0: THE SINGULARITY]
    V3 -->|Global Orchestration| V4((v?.0: THE OVERMIND))
    
    classDef past fill:#111,stroke:#333,color:#666;
    classDef current fill:#000,stroke:#00ff41,stroke-width:2px,color:#fff;
    classDef future fill:#000,stroke:#bd93f9,stroke-width:2px,color:#fff,stroke-dasharray: 5 5;
    
    class V1,V2 past
    class V3 current
    class V4 future
```

---
"""
        new_readme = new_readme.replace('### 🎨 D I G I T A L _ S O U L', journey_md + '### 🎨 D I G I T A L _ S O U L')

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
    
    print("✅ README.md updated with Neural Project Map!")

if __name__ == "__main__":
    generate_readme()
