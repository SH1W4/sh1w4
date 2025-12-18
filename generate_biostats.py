import os
import requests
import random
from datetime import datetime

# ==============================================================================
# 🧬 CONFIGURATION: THE GENETIC CODE
# ==============================================================================
USERNAME = "SH1W4" 
TOKEN = os.getenv("GH_TOKEN")
THEME_COLORS = {
    "HEALTHY": "#00ff41",  # High activity
    "MUTATING": "#bd93f9", # Moderate activity
    "DORMANT": "#ff5555",  # Low activity
    "VOID": "#0d1117"      # Background
}

# ==============================================================================
# 🧪 LIVE DATA FETCHING
# ==============================================================================
def fetch_github_data():
    if not TOKEN:
        print("⚠️ No GH_TOKEN found. Using MOCK data.")
        # Mock data: activity_level, commit_count, top_language, repos_count, languages_count, daily_activity
        return "MOCK_HIGH", 42, "Python", 12, 5, [8, 12, 6, 15, 10, 9, 14]

    headers = {"Authorization": f"token {TOKEN}"}
    
    # 1. Fetch Recent Activity (Events) + Daily breakdown
    try:
        commit_count = 0
        events = []
        daily_activity = [0] * 7  # Last 7 days
        
        # Fetch up to 3 pages (300 events) to capture more history
        for page in range(1, 4):
            events_url = f"https://api.github.com/users/{USERNAME}/events?per_page=100&page={page}"
            response = requests.get(events_url, headers=headers)
            if response.status_code == 200:
                page_data = response.json()
                if not page_data:
                    break
                events.extend(page_data)
            else:
                break
        
        # Count events and build daily activity sparkline
        from datetime import datetime, timedelta
        now = datetime.utcnow()
        
        for event in events:
            event_date = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            days_ago = (now - event_date).days
            if days_ago < 7:
                daily_activity[6 - days_ago] += 1
        
        commit_count = len(events)
            
        # Determine Activity Level
        if commit_count > 50: activity_level = "HIGH"
        elif commit_count > 10: activity_level = "MEDIUM"
        else: activity_level = "LOW"
    except Exception as e:
        print(f"Error fetching events: {e}")
        activity_level = "LOW"
        commit_count = 0
        daily_activity = [0] * 7

    # 2. Fetch Top Language + Language diversity
    try:
        repos_url = f"https://api.github.com/users/{USERNAME}/repos?sort=updated&per_page=30"
        response = requests.get(repos_url, headers=headers)
        langs = {}
        repos_count = 0
        
        if response.status_code == 200:
            repos = response.json()
            repos_count = len(repos)
            for repo in repos:
                lang = repo["language"]
                if lang:
                    langs[lang] = langs.get(lang, 0) + 1
            top_language = max(langs, key=langs.get) if langs else "Unknown"
            languages_count = len(langs)
        else:
            top_language = "System"
            languages_count = 0
    except Exception as e:
        print(f"Error fetching repos: {e}")
        top_language = "Polyglot"
        repos_count = 0
        languages_count = 0

    return activity_level, commit_count, top_language, repos_count, languages_count, daily_activity

# FETCH REAL DATA
activity_level, commit_count, top_language, repos_count, languages_count, daily_activity = fetch_github_data()

# Logic to determine organism state
if activity_level == "HIGH":
    status_text = "HYPER-EVOLUTION"
    core_color = THEME_COLORS["HEALTHY"]
    pulse_rate = "0.5s"
elif activity_level == "MEDIUM" or activity_level == "MOCK_HIGH":
    status_text = "STEADY_GROWTH"
    core_color = THEME_COLORS["MUTATING"]
    pulse_rate = "1.5s"
else:
    status_text = "HIBERNATION"
    core_color = THEME_COLORS["DORMANT"]
    pulse_rate = "4s"

# ==============================================================================
# 🎨 SVG GENERATION ENGINE
# ==============================================================================
def generate_svg():
    # Calculate sparkline points (normalized to height 30, width 100)
    max_act = max(daily_activity) if max(daily_activity) > 0 else 1
    points = []
    for i, val in enumerate(daily_activity):
        x = 280 + (i * 15)
        y = 100 - (val / max_act * 30)
        points.append(f"{x},{y}")
    sparkline_path = "M " + " L ".join(points)

    svg_content = f"""
    <svg width="400" height="200" viewBox="0 0 400 200" fill="none" xmlns="http://www.w3.org/2000/svg">
        <style>
            .text {{ font-family: 'Segoe UI', Consolas, monospace; fill: #e6e6e6; }}
            .label {{ font-size: 9px; opacity: 0.6; text-transform: uppercase; letter-spacing: 1px; }}
            .value {{ font-size: 14px; font-weight: bold; }}
            
            @keyframes pulse {{
                0%, 100% {{ opacity: 0.5; filter: drop-shadow(0 0 2px {core_color}); }}
                50% {{ opacity: 1; filter: drop-shadow(0 0 10px {core_color}); }}
            }}
            
            @keyframes scan {{
                0% {{ transform: translateY(0); opacity: 0; }}
                10% {{ opacity: 0.5; }}
                90% {{ opacity: 0.5; }}
                100% {{ transform: translateY(200px); opacity: 0; }}
            }}

            @keyframes slide {{
                from {{ stroke-dashoffset: 200; }}
                to {{ stroke-dashoffset: 0; }}
            }}

            .core {{
                animation: pulse {pulse_rate} infinite ease-in-out;
                fill: {core_color};
            }}
            
            .scanner {{
                animation: scan 4s linear infinite;
                stroke: {core_color};
                stroke-width: 1;
                opacity: 0.2;
            }}

            .sparkline {{
                stroke: {core_color};
                stroke-width: 2;
                fill: none;
                stroke-dasharray: 200;
                animation: slide 2s ease-out forwards;
            }}
        </style>

        <!-- BACKGROUND MODULE -->
        <rect width="400" height="200" rx="12" fill="{THEME_COLORS['VOID']}" stroke="#21262d" stroke-width="2"/>
        
        <!-- SCANNER LINE -->
        <line x1="0" y1="0" x2="400" y2="0" class="scanner" />

        <!-- HEADER STATUS -->
        <g transform="translate(20, 25)">
            <text class="text label">COGNITIVE_ID</text>
            <text y="18" class="text" font-size="16" font-weight="900" fill="#ffffff">{USERNAME}</text>
            
            <rect x="280" y="-10" width="80" height="14" rx="3" fill="{core_color}" fill-opacity="0.1"/>
            <text x="320" y="0" class="text" font-size="8" text-anchor="middle" font-weight="bold" fill="{core_color}">{status_text}</text>
        </g>

        <!-- CENTRAL BIO-CORE -->
        <g transform="translate(60, 100)">
            <circle r="40" stroke="#30363d" stroke-width="1" stroke-dasharray="4 4" />
            <circle r="18" class="core" />
            <circle r="25" stroke="{core_color}" stroke-width="0.5" opacity="0.3" />
        </g>

        <!-- DATA READOUTS (Left Grid) -->
        <g transform="translate(140, 65)">
            <g>
                <text class="text label">RECURRENT_MUTATIONS</text>
                <text y="18" class="text value" fill="{core_color}">{commit_count} <tspan font-size="10" opacity="0.5">EVTS</tspan></text>
            </g>
            
            <g transform="translate(0, 45)">
                <text class="text label">NEURAL_CONNECTIONS</text>
                <text y="18" class="text value">{repos_count} <tspan font-size="10" opacity="0.5">NODES</tspan></text>
            </g>
        </g>

        <!-- DATA READOUTS (Right Grid) -->
        <g transform="translate(270, 65)">
            <g>
                <text class="text label">DOMINANT_STRAIN</text>
                <text y="18" class="text value" fill="#ffffff">> {top_language}</text>
            </g>
            
            <g transform="translate(0, 45)">
                <text class="text label">ACTIVE_NODES</text>
                <text y="18" class="text value">{languages_count} <tspan font-size="10" opacity="0.5">STRAND</tspan></text>
            </g>
        </g>

        <!-- ACTIVITY SPARKLINE -->
        <g transform="translate(0, 40)">
             <text x="280" y="45" class="text label" opacity="0.4">ACTIVITY_TREND (7D)</text>
             <path d="{sparkline_path}" class="sparkline" />
        </g>

        <!-- FOOTER -->
        <rect y="170" width="400" height="30" fill="#161b22" opacity="0.5" />
        <text x="20" y="188" class="text label" font-size="8">LAST_SCAN: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC</text>
        <text x="380" y="188" class="text label" font-size="8" text-anchor="end">KERNEL_VER: 2.2.0-STABLE</text>

    </svg>
    """
    return svg_content

# ==============================================================================
# 💾 SAVE OUTPUT
# ==============================================================================
if __name__ == "__main__":
    svg = generate_svg()
    # Save locally to test
    with open("biostats.svg", "w", encoding='utf-8') as f:
        f.write(svg)
    print("✅ Bio-Stats Generated successfully: biostats.svg")
