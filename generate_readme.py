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
    """Generate the full README.md with non-destructive section updates"""
    data = load_projects()
    
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return

    import re
    
    # helper to replace content between a marker and the next section/rule
    def replace_section(full_text, section_title, new_content, end_marker="---"):
        pattern = re.escape(section_title) + r".*?" + re.escape(end_marker)
        if re.search(pattern, full_text, re.DOTALL):
            return re.sub(pattern, f"{section_title}\n\n{new_content}\n\n{end_marker}", full_text, count=1, flags=re.DOTALL)
        return full_text

    # 1. STRATEGIC DIRECTIVE (Ensure it exists below header)
    if '<img src="./directive.svg"' not in content:
        directive_md = '\n<div align="center">\n    <img src="./directive.svg" width="100%" alt="Strategic Directive"/>\n</div>\n<br/>'
        content = content.replace(' alt="Neural Interface"/>\n</div>', ' alt="Neural Interface"/>\n</div>' + directive_md)

    # 2. CONCEPT CORE
    concept_body = """| IDENTIFIER | ATTRIBUTE | DESCRIPTION |
| :--- | :--- | :--- |
| **NAME** | **SH1W4** | Symbiotic Human-AI Workflow Architect |
| **ROLE** | **OPERATIONAL HUB** | The bridge where Human Vision meets AI Velocity |
| **NATURE** | **SYMBION ENTITY** | Human (Directives/Ethics) + AI (Materialization/Results) |

> **"SH1W4 is not a developer; it is an Operational Hub."**
> 
> It represents the bridge where human strategic vision meets high-velocity agentic execution. In this ecosystem, the human provides the **Directives** and the **Ethics**, while the AI enshrine (Vireon/Trinity/Aiden) materializes the **Results**."""
    content = replace_section(content, "### 🧩 C O N C E P T _ C O R E (The SH1W4 Entity)", concept_body)

    # 3. SYSTEM MANIFEST
    projects_md = generate_mermaid_graph(data)
    manifest_body = f'<div align="center">\n    <img src="./neural_network.svg" width="80%" alt="Symbeon Neural Fabric"/>\n</div>\n\n{projects_md}'
    content = replace_section(content, "### 📂 S Y S T E M _ M A N I F E S T (Symbeon Ecosystem)", manifest_body)

    # 4. AGENT DOSSIERS
    dossiers_body = """| IDENTITY | ROLE | COGNITIVE_PROFILE | PRIMARY_DIRECTIVE |
| :--- | :--- | :--- | :--- |
| **🧬 VIREON** | Orchestrator | Aggressive / Precise | Universal Scaling |
| **🧠 TRINITY** | Analytics | Reflective / Recursive | Pattern Synthesis |
| **📡 AIDEN** | Interface | Tactical / Adaptive | User Synchronization |"""
    content = replace_section(content, "### 👥 A G E N T _ D O S S I E R S (Identity Core)", dossiers_body)

    # 5. EVOLUTION JOURNEY
    journey_body = """```mermaid
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
```"""
    content = replace_section(content, "### 🚀 E V O L U T I O N _ J O U R N E Y", journey_body)

    # 6. ENVIRONMENTAL MANIFEST
    if '### 🖥️ E N V I R O N M E N T A L _ M A N I F E S T' not in content:
        env_md = """\n### 🖥️ E N V I R O N M E N T A L _ M A N I F E S T\n\n| SYSTEM | SPECIFICATION | ROLE |\n| :--- | :--- | :--- |\n| **OS** | **Arch Linux / WSL2** | Primary Cognitive Host |\n| **CORE** | **M3 Max / Ryzen 9** | Neural Processing Unit |\n| **SHELL** | **ZSH / Powerlevel10k** | Tactical Command Link |\n\n---"""
        content = content.replace('### 📡 N E T W O R K _ A C T I V I T Y', env_md + '\n\n### 📡 N E T W O R K _ A C T I V I T Y')

    # 7. TERMINAL STATUS
    terminal_lines = [
        "root@symbeon:~$ ./status_check.sh",
        "> UPTIME: 99.9% [STABLE]",
        "> NEURAL_SYNC: OPTIMAL",
        "> NEXT_GOAL: AGI_INFRASTRUCTURE",
        "[█▒▒▒▒▒▒▒▒▒] 12% EVOLUTION_COMPLETE"
    ]
    terminal_url = f"https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=16&duration=4000&pause=1000&color=00FF41&background=0D111700&center=true&vCenter=true&width=500&height=180&lines={';'.join([line.replace(' ', '+') for line in terminal_lines])}"
    
    terminal_md = f'<div align="center">\n    <img src="{terminal_url}" alt="Terminal Status" />\n</div>'
    
    if './status_check.sh' in content:
        content = re.sub(r'<div align="center">\s+<pre>.*?root@symbeon:.*?<\/pre>\s+<\/div>', terminal_md, content, flags=re.DOTALL)

    # 9. VERIFICATION SIGIL (Trust Layer)
    if '### 🛡️ V E R I F I C A T I O N _ S I G I L' not in content:
        sigil_md = """
### 🛡️ V E R I F I C A T I O N _ S I G I L

<div align="center">
    <img src="https://img.shields.io/badge/IDENTITY-VERIFIED-00ff41?style=for-the-badge&logo=opsgenie&labelColor=1a1a1a" height="30">
    <img src="https://img.shields.io/badge/SECURITY-PGP_SIGNED-bd93f9?style=for-the-badge&logo=gnupg&labelColor=1a1a1a" height="30">
    <br/>
    <sub><i>"Authenticity guaranteed via Symbeon Core."</i></sub>
</div>

---
"""
        content = content.replace('### 🤝 STRATEGIC ALLIANCE', sigil_md + '### 🤝 STRATEGIC ALLIANCE')

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ README.md synchronized with Demiurge V4.3 final schema.")

if __name__ == "__main__":
    generate_readme()
