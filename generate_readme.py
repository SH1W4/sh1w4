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
    """Refined non-destructive section generator (Split & Merge approach)"""
    data = load_projects()
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
    except: return

    # Define the 100% stable sections
    sections = {
        "CONCEPT": "### 🧩 C O N C E P T _ C O R E (The SH1W4 Entity)",
        "MANIFEST": "### 📂 S Y S T E M _ M A N I F E S T (Symbeon Ecosystem)",
        "DOSSIERS": "### 👥 A G E N T _ D O S S I E R S (Identity Core)",
        "RESEARCH": "### 🔬 R E S E A R C H _ D N A (Knowledge Vectors)",
        "ENGINE": "### ⚙️ THE SYMBEON ENGINE (Methodology)",
        "JOURNEY": "### 🚀 E V O L U T I O N _ J O U R N E Y",
        "SOUL": "### 🎨 D I G I T A L _ S O U L",
        "ENVIRONMENT": "### 🖥️ E N V I R O N M E N T A L _ M A N I F E S T",
        "ALLIANCE": "### 🤝 STRATEGIC ALLIANCE",
        "ACTIVITY": "### 📡 N E T W O R K _ A C T I V I T Y"
    }

    # Core content segments
    segments = {}
    
    # 1. Identity Core
    segments["CONCEPT"] = """| IDENTIFIER | ATTRIBUTE | DESCRIPTION |
| :--- | :--- | :--- |
| **NAME** | **SH1W4** | Symbiotic Human-AI Workflow Architect |
| **ROLE** | **OPERATIONAL HUB** | The bridge where Human Vision meets AI Velocity |
| **NATURE** | **SYMBION ENTITY** | Human (Directives/Ethics) + AI (Materialization/Results) |

> **"SH1W4 is not a developer; it is an Operational Hub."**
> 
> It represents the bridge where human strategic vision meets high-velocity agentic execution. In this ecosystem, the human provides the **Directives** and the **Ethics**, while the AI enshrine (Vireon/Trinity/Aiden) materializes the **Results**.

---"""

    # 2. Manifest
    projects_md = generate_mermaid_graph(data)
    segments["MANIFEST"] = f'<div align="center">\n    <img src="./neural_network.svg" width="80%" alt="Symbeon Neural Fabric"/>\n</div>\n\n{projects_md}\n\n---'

    # 3. Dossiers
    segments["DOSSIERS"] = """| IDENTITY | ROLE | COGNITIVE_PROFILE | PRIMARY_DIRECTIVE |
| :--- | :--- | :--- | :--- |
| **🧬 VIREON** | Orchestrator | Aggressive / Precise | Universal Scaling |
| **🧠 TRINITY** | Analytics | Reflective / Recursive | Pattern Synthesis |
| **📡 AIDEN** | Interface | Tactical / Adaptive | User Synchronization |

---"""

    # 4. Journey
    segments["JOURNEY"] = """```mermaid
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

---"""

    # 5. Environment
    segments["ENVIRONMENT"] = """| SYSTEM | SPECIFICATION | ROLE |
| :--- | :--- | :--- |
| **OS** | **Arch Linux / WSL2** | Primary Cognitive Host |
| **CORE** | **M3 Max / Ryzen 9** | Neural Processing Unit |
| **SHELL** | **ZSH / Powerlevel10k** | Tactical Command Link |

---"""

    # 6. Terminal status (Special injection)
    terminal_lines = [
        "root@symbeon:~$ ./status_check.sh",
        "> UPTIME: 99.9% [STABLE]",
        "> NEURAL_SYNC: OPTIMAL",
        "> NEXT_GOAL: AGI_INFRASTRUCTURE",
        "[█▒▒▒▒▒▒▒▒▒] 12% EVOLUTION_COMPLETE"
    ]
    terminal_url = f"https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=16&duration=4000&pause=1000&color=00FF41&background=0D111700&center=true&vCenter=true&width=500&height=180&lines={';'.join([line.replace(' ', '+') for line in terminal_lines])}"
    terminal_md = f'<div align="center">\n    <img src="{terminal_url}" alt="Terminal Status" />\n</div>\n\n'

    # Construction of New Content
    # We keep everything before the first section
    header_end = content.find("---") + 3
    if "### 🧩 C O N C E P T" in content:
        header_end = content.find("### 🧩 C O N C E P T")
    
    new_readme = content[:header_end].strip() + "\n\n---\n\n"
    
    # Ordered Assembly
    ordered_keys = ["CONCEPT", "MANIFEST", "DOSSIERS", "RESEARCH", "ENGINE", "JOURNEY", "ENVIRONMENT", "ALLIANCE", "ACTIVITY", "SOUL"]
    
    import re
    for key in ordered_keys:
        title = sections[key]
        if key in segments:
            new_readme += f"{title}\n\n{segments[key]}\n\n"
        else:
            # For sections we don't dynamically overwrite yet, try to find them in current content
            pattern = re.escape(title) + r"(.*?)(?=\n\n###|---|$)"
            match = re.search(pattern, content, re.DOTALL)
            if match:
                new_readme += f"{title}\n\n{match.group(1).strip()}\n\n---\n\n"
    
    # Final terminal injection before Network Activity
    if terminal_md not in new_readme:
        new_readme = new_readme.replace(sections["ACTIVITY"], terminal_md + sections["ACTIVITY"])

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
    
    print("✅ README.md restructured and synchronized (V4.3 Final).")

if __name__ == "__main__":
    generate_readme()
