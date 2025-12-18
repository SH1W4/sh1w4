"""
SH1W4 Strategic Directive Generator
Generates a "Live Mission Briefing" SVG for the profile.
"""
import random
from datetime import datetime

DIRECTIVES = [
    "SCALING_MCP_INFRASTRUCTURE // TARGET: UNIVERSAL_INTEROP",
    "OPTIMIZING_NEURAL_ROUTING // TARGET: LATENCY_MINIMIZATION",
    "REFINING_SEVE_FRAMEWORK // TARGET: ETHICAL_ALIGNMENT_STABILITY",
    "DECODING_BIO_COMPUTATIONAL_VECTORS // TARGET: ORGANIC_LOGIC_SIM",
    "REINFORCING_AGENTIC_SECURITY // TARGET: IP_PROTECTION_V3",
    "MAPPING_SYMBEON_NODES // TARGET: ECOSYSTEM_SYNCHRONIZATION"
]

def generate_directive_svg():
    directive = random.choice(DIRECTIVES)
    
    # Colors matching the theme
    COLOR_BG = "#0d1117"
    COLOR_ACCENT = "#00ff41" # Bio-Green
    COLOR_WARN = "#f1c40f" # Warning Yellow
    
    svg = f"""
    <svg width="600" height="60" viewBox="0 0 600 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <style>
            .text {{ font-family: 'Segoe UI', Consolas, monospace; fill: {COLOR_ACCENT}; font-size: 10px; letter-spacing: 2px; font-weight: bold; }}
            .label {{ fill: #8b949e; font-size: 8px; letter-spacing: 1px; }}
            .cursor {{ animation: blink 1s infinite; fill: {COLOR_ACCENT}; }}
            @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
        </style>

        <rect width="600" height="60" rx="4" fill="{COLOR_BG}" stroke="#30363d" stroke-width="1"/>
        
        <g transform="translate(20, 20)">
            <text class="label">CURRENT_STRATEGIC_DIRECTIVE:</text>
            <text y="20" class="text">> {directive}<tspan class="cursor">_</tspan></text>
        </g>
        
        <circle cx="580" cy="15" r="3" fill="{COLOR_WARN}">
            <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite" />
        </circle>
    </svg>
    """
    
    with open('directive.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("✅ Strategic Directive SVG generated.")

if __name__ == "__main__":
    generate_directive_svg()
