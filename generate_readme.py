"""
SH1W4 Profile README Generator
Automatically generates the projects section from projects.json
"""
import json
import datetime

def load_projects():
    with open('projects.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_mermaid_graph(data):
    """Generate the Pure Architectural Manifest with Access Levels"""
    lines = [
        "```mermaid",
        f"%% Cache-Bust: {datetime.datetime.now().isoformat()}",
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
    
        "    subgraph ETHICS_GOVERNANCE",
        "        SEVE[\"⚖️ SEVE_ALIGNMENT_FWK <br/> [ACCESS: L1]\"]:::ethics",
        "    end",

        "    subgraph RESEARCH_LABS",
        "        direction TB",
        "        BIO[\"🔬 BIO_COMPUTATION_R&D <br/> [ACCESS: L2]\"]:::research",
        "        PROTO[\"📐 SEMANTIC_STANDARDS <br/> [ACCESS: L2]\"]:::research",
        "    end",

        "    subgraph INTELLIGENCE_LAYER",
        "        Core --> VIREON[\"🧬 AGENTIC_ORCHESTRATOR <br/> [ACCESS: L1]\"]:::agent",
        "        Core --> TRINITY[\"🧠 COGNITIVE_PROCESSOR <br/> [ACCESS: L1]\"]:::agent",
        "        Core --> AIDEN[\"📡 TACTICAL_INTERFACER <br/> [ACCESS: L1]\"]:::agent",
        "    end",

        "    subgraph DOMAIN_LAYER",
        "        VIREON --> LEGAL[\"⚖️ LEGAL_INTEL_CORE <br/> [ACCESS: L1]\"]:::agent",
        "        LEGAL --> SHIELD[\"🛡️ IP_GUARD_PROTOCOL <br/> [ACCESS: L1]\"]:::tool",
        "        VIREON -.-> RD_DOMAIN[\"⚖️ LEGAL_TECH_R&D <br/> [ACCESS: RESTRICTED]\"]:::restricted",
        "    end",
        
        "    subgraph TOOL_LAYER",
        "        direction TB",
        "        VIREON --> DX_KIT[\"👁️ DEV_EXP_MODULE <br/> [ACCESS: L1]\"]:::tool",
        "        VIREON --> ARKITECH[\"🏗️ STRAT_INFRA_TOOL <br/> [ACCESS: L1]\"]:::tool",
        "        AIDEN -.-> RD_TOOLS[\"📡 R&D_EXTENSIONS <br/> [ACCESS: RESTRICTED]\"]:::restricted",
        "    end",

        "    %% Strategic Relationship Links",
        "    SEVE -.->|Guards| TRINITY",
        "    SEVE -.->|Aligns| VIREON",
        "    BIO -.->|Data| TRINITY",
        "    PROTO -.->|Specs| VIREON",
        "    DX_KIT -.->|Telemetry| Core",
        "    ",
        "    %% Implicit Vertical Order (Invisibly pinning Labs to bottom)",
        "    User ~~~ SEVE",
        "    User ~~~ BIO",
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

    # 2. CONCEPT CORE (Identity Definition)
    concept_pattern = r'(### 🧩 C O N C E P T _ C O R E.*?\n---)'
    concept_md = """### 🧩 C O N C E P T _ C O R E (The SH1W4 Entity)

| IDENTIFIER | ATTRIBUTE | DESCRIPTION |
| :--- | :--- | :--- |
| **NAME** | **SH1W4** | Symbiotic Human-AI Workflow Architect |
| **ROLE** | **OPERATIONAL HUB** | The bridge where Human Vision meets AI Velocity |
| **NATURE** | **SYMBION ENTITY** | Human (Directives/Ethics) + AI (Materialization/Results) |

> **"SH1W4 is not a developer; it is an Operational Hub."**
> 
> It represents the bridge where human strategic vision meets high-velocity agentic execution. In this ecosystem, the human provides the **Directives** and the **Ethics**, while the AI enshrine (Vireon/Trinity/Aiden) materializes the **Results**.

---"""
    
    if '### 🧩 C O N C E P T _ C O R E' in new_readme:
        new_readme = re.sub(concept_pattern, concept_md, new_readme, flags=re.DOTALL)
    else:
        new_readme = new_readme.replace("---", f"---\n\n{concept_md}", 1)

    # 3. SYSTEM MANIFEST (Projects Graph)
    start_marker = "### 📂 S Y S T E M _ M A N I F E S T"
    pattern = re.escape(start_marker) + r".*?```mermaid.*?```"
    new_manifest = f"{start_marker} (Symbeon Ecosystem)\n\n"
    new_manifest += '<div align="center">\n'
    new_manifest += '    <img src="./neural_network.svg" width="80%" alt="Symbeon Neural Fabric"/>\n'
    new_manifest += '</div>\n\n'
    new_manifest += projects_md
    new_readme = re.sub(pattern, new_manifest, new_readme, flags=re.DOTALL)

    # 4. DASHBOARD TELEMETRY
    dashboard_pattern = r'(<img src="\./biostats\.svg".*?\/>)'
    if '<img src="./telemetry.svg"' not in new_readme:
        telemetry_md = '\n<br/>\n<h3><code>🧠 COGNITIVE_PULSE</code></h3>\n<img src="./telemetry.svg" width="90%" alt="Cognitive Telemetry"/>'
        new_readme = re.sub(dashboard_pattern, f'\\1{telemetry_md}', new_readme, flags=re.DOTALL)

    # 5. AGENT DOSSIERS (New Section after Manifest)
    if '### 👥 A G E N T _ D O S S I E R S' not in new_readme:
        dossiers_md = """
### 👥 A G E N T _ D O S S I E R S (Identity Core)

| IDENTITY | ROLE | COGNITIVE_PROFILE | PRIMARY_DIRECTIVE |
| :--- | :--- | :--- | :--- |
| **🧬 VIREON** | Orchestrator | Aggressive / Precise | Universal Scaling |
| **🧠 TRINITY** | Analytics | Reflective / Recursive | Pattern Synthesis |
| **📡 AIDEN** | Interface | Tactical / Adaptive | User Synchronization |

---
"""
        new_readme = new_readme.replace("> **MISSION PROTOCOL:**", dossiers_md + "> **MISSION PROTOCOL:**")

    # 6. EVOLUTION JOURNEY (New Section after Methodology)
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

    # 7. ENVIRONMENTAL MANIFEST (Hardware/Compute)
    if '### 🖥️ E N V I R O N M E N T A L _ M A N I F E S T' not in new_readme:
        env_md = """
### 🖥️ E N V I R O N M E N T A L _ M A N I F E S T

| SYSTEM | SPECIFICATION | ROLE |
| :--- | :--- | :--- |
| **OS** | **Arch Linux / WSL2** | Primary Cognitive Host |
| **CORE** | **M3 Max / Ryzen 9** | Neural Processing Unit |
| **SHELL** | **ZSH / Powerlevel10k** | Tactical Command Link |

---
"""
        new_readme = new_readme.replace('### 📡 N E T W O R K _ A C T I V I T Y', env_md + '### 📡 N E T W O R K _ A C T I V I T Y')

    # 8. TERMINAL STATUS (Typing Effect)
    terminal_pattern = r'(<div align="center">.*?<pre>.*?root@symbeon:.*?<\/pre>.*?<\/div>)'
    terminal_lines = [
        "root@symbeon:~$ ./status_check.sh",
        "> UPTIME: 99.9% [STABLE]",
        "> NEURAL_SYNC: OPTIMAL",
        "> NEXT_GOAL: AGI_INFRASTRUCTURE",
        "[█▒▒▒▒▒▒▒▒▒] 12% EVOLUTION_COMPLETE"
    ]
    terminal_url = f"https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=16&duration=4000&pause=1000&color=00FF41&background=0D111700&center=true&vCenter=true&width=500&height=180&lines={';'.join([line.replace(' ', '+') for line in terminal_lines])}"
    
    terminal_md = f"""<div align="center">
    <img src="{terminal_url}" alt="Terminal Status" />
</div>"""

    if './status_check.sh' in new_readme:
        new_readme = re.sub(terminal_pattern, terminal_md, new_readme, flags=re.DOTALL)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
    
    print("✅ README.md synchronized with Demiurge V4.3 updates.")

if __name__ == "__main__":
    generate_readme()
