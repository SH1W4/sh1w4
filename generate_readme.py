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

    # 4. Research DNA
    segments["RESEARCH"] = """| VECTOR | SPECIALIZATION | STATUS |
| :--- | :--- | :--- |
| **[V_01]** | **Agentic Orchestration** (Swarm Logic & MCP) | `STABLE` |
| **[V_02]** | **Deep Tech Compliance** (Semantic Prior Art) | `ACTIVE` |
| **[V_03]** | **Bio-Computational Sim** (Organic Logic) | `R&D` |

> "Information is not knowledge. The only source of knowledge is **experience** and **pattern synthesis**."

---"""

    # 5. Engine
    segments["ENGINE"] = """```mermaid
stateDiagram-v2
    %% Theme: Dark & Strategic
    classDef space fill:#0d1117,stroke:#30363d,stroke-width:1px,color:#8b949e;
    classDef active fill:#0d1117,stroke:#00ff41,stroke-width:2px,color:#fff;
    classDef check fill:#0d1117,stroke:#f1c40f,stroke-width:2px,color:#fff;
    
    [*] --> 🔭_OBSERVATION:::space : Pattern_Recognition
    🔭_OBSERVATION --> 💡_HYPOTHESIS:::space : Signal_Synthesis
    💡_HYPOTHESIS --> 🧬_PROTOTYPING:::active : Rapid_Cycle
    
    state "SEVE ALIGNMENT" as GOV {
        direction LR
        ⚠️_RISK_ANALYSIS --> ⚖️_ETHICAL_CHECK
    }
    
    🧬_PROTOTYPING --> GOV:::check : Validation
    GOV --> 🚀_MATERIALIZATION:::active : Deployment
    🚀_MATERIALIZATION --> [*] : Impact_Loop
```

> "We do not guess. We **observe** patterns, **synthesize** solutions, and **align** them with human values before writing a single line of production code."

---"""

    # 6. Journey
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

    # 7. Environment
    segments["ENVIRONMENT"] = """| SYSTEM | SPECIFICATION | ROLE |
| :--- | :--- | :--- |
| **OS** | **Arch Linux / WSL2** | Primary Cognitive Host |
| **CORE** | **M3 Max / Ryzen 9** | Neural Processing Unit |
| **SHELL** | **ZSH / Powerlevel10k** | Tactical Command Link |

---"""

    # 8. Alliance
    segments["ALLIANCE"] = """<div align="center">
    <p>Open for high-impact joint ventures in <b>Agencia Artificial</b> and <b>Cognitive Systems</b>.</p>
    <a href="https://linkedin.com/in/joaomartins-ai">
        <img src="https://img.shields.io/badge/INITIATE_UPLINK-LINKEDIN-0a66c2?style=for-the-badge&logo=linkedin&labelColor=1a1a1a" height="35">
    </a>
    &nbsp;&nbsp;
    <a href="mailto:contact@symbeon.com">
        <img src="https://img.shields.io/badge/ENCRYPTED_CHANNEL-PROTONMAIL-6d4aff?style=for-the-badge&logo=protonmail&labelColor=1a1a1a" height="35">
    </a>
    <br/><br/>
    <a href="./MANIFESTO.md">
        <img src="https://img.shields.io/badge/VIEW-MANIFESTO-00ff41?style=for-the-badge&logo=markdown&labelColor=1a1a1a" height="35">
    </a>
    <br/><br/>
    <code>// PGP_FINGERPRINT: 4A7B 1C92 D3E4 F5G6... [ACTIVE]</code>
</div>

---"""

    # 9. Activity
    segments["ACTIVITY"] = """<div align="center">
    <a href="https://git.io/typing-svg">
      <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=14&duration=3000&pause=1000&color=00FF41&background=0D111700&center=true&vCenter=true&width=600&height=100&lines=Subject%3A+SH1W4+%7C+STATUS%3A+HYPER-EVOLUTION;%3E+ANALYZING+GITHUB+EVENT_STREAM...;%3E+OPTIMIZING+DEVELOPER+EXPERIENCE...;%3E+SYSTEM_READY." alt="Typing SVG" />
    </a>
</div>

---"""

    # 10. SOUL (THE FINAL SIGNATURE)
    segments["SOUL"] = """<div align="center">
    <img src="./art_core_anonymous.png" width="100%" style="border-radius: 8px; border: 1px solid #30363d;" alt="Bio-Digital Soul"/>
    <br/>
    <sub><i>"The ghost in the machine."</i></sub>
</div>"""

    # Snake Animation (Special placement)
    snake_html = '<div align="center">\n    <img src="https://raw.githubusercontent.com/SH1W4/sh1w4/output/github-contribution-grid-snake-dark.svg" width="100%" alt="Snake Animation" />\n</div>\n'

    # Terminal status (Special injection)
    terminal_lines = [
        "root@symbeon:~$ ./status_check.sh",
        "> UPTIME: 99.9% [STABLE]",
        "> NEURAL_SYNC: OPTIMAL",
        "> NEXT_GOAL: AGI_INFRASTRUCTURE",
        "[█▒▒▒▒▒▒▒▒▒] 12% EVOLUTION_COMPLETE"
    ]
    terminal_url = f"https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=16&duration=4000&pause=1000&color=00FF41&background=0D111700&center=true&vCenter=true&width=500&height=180&lines={';'.join([line.replace(' ', '+') for line in terminal_lines])}"
    terminal_md = f'<div align="center">\n    <img src="{terminal_url}" alt="Terminal Status" />\n</div>\n\n'

    # --- CONSTRUCTION ---
    import re

    # 1. Capture the Full Header (Everything before the first ### section)
    # We use a pattern that finds the first section title
    section_patterns = [r'### 🧩 C O N C E P T', r'### 🎨 D I G I T A L', r'### 📡 N E T W O R K']
    split_point = len(content)
    for p in section_patterns:
        match = re.search(p, content)
        if match and match.start() < split_point:
            split_point = match.start()
    
    header_raw = content[:split_point]

    # 2. Aggressive Cleaning of Header (Remove all dynamic tags to prevent duplication)
    # Remove existing Snake
    header_raw = re.sub(r'<div align="center">\s*<img src="[^"]*snake-dark\.svg"[^>]*>\s*</div>', '', header_raw, flags=re.DOTALL)
    # Remove existing Biostats (if it was already outside the table)
    header_raw = re.sub(r'<div align="center">\s*<a href="https://github.com/SH1W4">\s*<img src="\./biostats\.svg"[^>]*>\s*</a>\s*</div>', '', header_raw, flags=re.DOTALL)
    # Remove existing Terminal
    header_raw = re.sub(r'<div align="center">\s*<img src="https://readme-typing-svg\.herokuapp\.com[^"]*status_check\.sh[^"]*"[^>]*>\s*</div>', '', header_raw, flags=re.DOTALL)
    # Remove existing Soul from header
    header_raw = re.sub(r'<div align="center">\s*<img src="\./art_core_anonymous\.png"[^>]*>.*?</div>', '', header_raw, flags=re.DOTALL)
    # Remove legacy section titles that might have leaked
    header_raw = re.sub(r'### [^\n]+', '', header_raw)

    # 3. Define metrics for top (Snake + BioStats)
    metrics_html = f"""
<div align="center">
    <img src="https://raw.githubusercontent.com/SH1W4/sh1w4/output/github-contribution-grid-snake-dark.svg" width="100%" alt="Snake Animation" />
</div>
<div align="center">
    <a href="https://github.com/SH1W4">
        <img src="./biostats.svg" width="45%" alt="Official Contribution Bar"/>
    </a>
</div>
"""

    # 4. Inject metrics below Banner
    # Banner ends at the first </div>
    banner_end = header_raw.find("</div>") + 6
    if banner_end > 5:
        header_part = header_raw[:banner_end] + "\n" + metrics_html + header_raw[banner_end:]
    else:
        header_part = metrics_html + header_raw

    # Final polish for header_part (remove excessive whitespace/dashes)
    header_part = header_part.strip()
    while header_part.endswith('-') or header_part.endswith('\n') or header_part.endswith(' '):
        header_part = header_part.rstrip('-').rstrip()

    new_readme = header_part + "\n\n---\n\n"
    
    # 5. Assemble Main Body (Ordered Sections)
    ordered_keys = ["CONCEPT", "MANIFEST", "DOSSIERS", "RESEARCH", "ENGINE", "JOURNEY", "ENVIRONMENT", "ALLIANCE"]
    
    for key in ordered_keys:
        title = sections[key]
        new_readme += f"{title}\n\n{segments[key].strip()}\n\n"

    # 6. Assemble Footer (Terminal + Digital Soul)
    new_readme += terminal_md
    new_readme += sections["SOUL"] + "\n\n" + segments["SOUL"].strip() + "\n\n"

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
    
    print("✅ README.md sanitized. Duplicates purged. Official Bar at top.")

if __name__ == "__main__":
    generate_readme()
