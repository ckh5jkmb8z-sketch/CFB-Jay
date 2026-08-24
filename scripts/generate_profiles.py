#!/usr/bin/env python3
"""
CFB-Jay Profile Generator
Generates individual player profiles organized by era, conference, and milestone type
Creates searchable HTML index with embedded YouTube links
"""

import csv
import os
from pathlib import Path
from datetime import datetime

class ProfileGenerator:
    def __init__(self, data_dir='data', output_dir='profiles'):
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.players = []
        self.eras = {}
        self.conferences = {}
        self.milestones = {}
        
    def load_all_data(self):
        """Load all conference CSV files"""
        csv_files = Path(self.data_dir).glob('*_performances.csv')
        for csv_file in csv_files:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.players.append(row)
                    self.organize_player(row)
    
    def organize_player(self, player):
        """Organize player by era, conference, and milestone"""
        era = player.get('Era', 'Unknown')
        conference = player.get('Conference', 'Unknown')
        milestone = player.get('Milestone_Type', 'Unknown')
        
        if era not in self.eras:
            self.eras[era] = []
        self.eras[era].append(player)
        
        if conference not in self.conferences:
            self.conferences[conference] = []
        self.conferences[conference].append(player)
        
        if milestone not in self.milestones:
            self.milestones[milestone] = []
        self.milestones[milestone].append(player)
    
    def generate_player_profile(self, player):
        """Generate HTML profile for individual player"""
        name = player.get('Player', 'Unknown')
        position = player.get('Position', 'N/A')
        school = player.get('School', 'N/A')
        year = player.get('Year', 'N/A')
        era = player.get('Era', 'N/A')
        opponent = player.get('Opponent', 'N/A')
        game_stats = player.get('Game_Stats_Rush_Rec_Pass', player.get('Game_Stats', 'N/A'))
        season_stats = player.get('Season_Stats', 'N/A')
        career_stats = player.get('Career_Stats', 'N/A')
        theoretical_max = player.get('Theoretical_Max', 'N/A')
        offensive_system = player.get('Offensive_System', 'N/A')
        defensive_system = player.get('Defensive_System', 'N/A')
        advanced_stats = player.get('Advanced_Stats_EPA_Success_Efficiency', player.get('Advanced_Stats', 'N/A'))
        milestone = player.get('Milestone_Type', 'N/A')
        full_game_link = player.get('YouTube_Full_Game', '#')
        highlights_link = player.get('YouTube_Highlights', '#')
        description = player.get('Spoiler_Free_Description', 'N/A')
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - {year} - CFB-Jay Vault</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }}
        .header {{
            border-bottom: 3px solid #2a5298;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        h1 {{
            font-size: 2.5em;
            color: #1e3c72;
            margin-bottom: 10px;
        }}
        .player-meta {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
            font-size: 0.95em;
        }}
        .meta-item {{
            background: #f5f5f5;
            padding: 10px 15px;
            border-left: 4px solid #2a5298;
        }}
        .meta-label {{
            font-weight: bold;
            color: #1e3c72;
        }}
        .stats-section {{
            margin: 30px 0;
        }}
        .stats-section h2 {{
            color: #1e3c72;
            margin-bottom: 15px;
            font-size: 1.5em;
            border-bottom: 2px solid #2a5298;
            padding-bottom: 10px;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }}
        .stat-box {{
            background: #f9f9f9;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #2a5298;
        }}
        .stat-label {{
            font-weight: bold;
            color: #1e3c72;
            margin-bottom: 5px;
        }}
        .stat-value {{
            color: #666;
            font-size: 0.95em;
        }}
        .video-section {{
            margin: 30px 0;
            background: #f0f0f0;
            padding: 20px;
            border-radius: 8px;
        }}
        .video-section h2 {{
            color: #1e3c72;
            margin-bottom: 15px;
        }}
        .video-links {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }}
        .video-link {{
            background: white;
            padding: 15px;
            border-radius: 5px;
            border: 2px solid #2a5298;
            text-align: center;
        }}
        .video-link a {{
            display: inline-block;
            background: #2a5298;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.3s;
        }}
        .video-link a:hover {{
            background: #1e3c72;
        }}
        .description {{
            background: #e8f4f8;
            padding: 20px;
            border-left: 4px solid #2a5298;
            border-radius: 5px;
            margin: 30px 0;
            line-height: 1.8;
        }}
        .milestone-badge {{
            display: inline-block;
            background: #2a5298;
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        .back-link {{
            margin-top: 30px;
            padding-top: 20px;
            border-top: 2px solid #eee;
        }}
        .back-link a {{
            color: #2a5298;
            text-decoration: none;
            font-weight: bold;
        }}
        .back-link a:hover {{
            text-decoration: underline;
        }}
        @media (max-width: 768px) {{
            .video-links {{
                grid-template-columns: 1fr;
            }}
            h1 {{
                font-size: 1.8em;
            }}
            .container {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{name}</h1>
            <span class="milestone-badge">{milestone}</span>
        </div>
        
        <div class="player-meta">
            <div class="meta-item">
                <div class="meta-label">Position:</div>
                <div>{position}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">School:</div>
                <div>{school}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Conference:</div>
                <div>{player.get('Conference', 'N/A')}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Year:</div>
                <div>{year}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Era:</div>
                <div>{era}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Opponent:</div>
                <div>{opponent}</div>
            </div>
        </div>
        
        <div class="stats-section">
            <h2>Performance Stats</h2>
            <div class="stats-grid">
                <div class="stat-box">
                    <div class="stat-label">Game Stats:</div>
                    <div class="stat-value">{game_stats}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Season Stats:</div>
                    <div class="stat-value">{season_stats}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Career Stats:</div>
                    <div class="stat-value">{career_stats}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Theoretical Max:</div>
                    <div class="stat-value">{theoretical_max}</div>
                </div>
            </div>
        </div>
        
        <div class="stats-section">
            <h2>System Information</h2>
            <div class="stats-grid">
                <div class="stat-box">
                    <div class="stat-label">Offensive System:</div>
                    <div class="stat-value">{offensive_system}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Defensive Formation:</div>
                    <div class="stat-value">{defensive_system}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Advanced Analytics:</div>
                    <div class="stat-value">{advanced_stats}</div>
                </div>
            </div>
        </div>
        
        <div class="description">
            <strong>Performance Summary:</strong><br>
            {description}
        </div>
        
        <div class="video-section">
            <h2>Game Footage</h2>
            <div class="video-links">
                <div class="video-link">
                    <div><strong>Full Game</strong></div>
                    <a href="{full_game_link}" target="_blank">Watch Full Game →</a>
                </div>
                <div class="video-link">
                    <div><strong>Highlights</strong></div>
                    <a href="{highlights_link}" target="_blank">View Highlights →</a>
                </div>
            </div>
        </div>
        
        <div class="back-link">
            <a href="../../index.html">← Back to Vault Index</a>
        </div>
    </div>
</body>
</html>
"""
        return html
    
    def generate_all_profiles(self):
        """Generate all player profile HTML files"""
        for player in self.players:
            era = player.get('Era', 'Unknown')
            name = player.get('Player', 'Unknown').replace(' ', '_').lower()
            year = player.get('Year', 'Unknown')
            
            era_dir = Path(self.output_dir) / era
            era_dir.mkdir(parents=True, exist_ok=True)
            
            filename = era_dir / f"{name}_{year}.html"
            html_content = self.generate_player_profile(player)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
    
    def generate_index_html(self):
        """Generate master index page"""
        era_sections = ""
        for era in sorted(self.eras.keys()):
            players_html = ""
            for player in sorted(self.eras[era], key=lambda x: x.get('Player', '')):
                name = player.get('Player', 'Unknown')
                year = player.get('Year', 'Unknown')
                school = player.get('School', 'N/A')
                position = player.get('Position', 'N/A')
                milestone = player.get('Milestone_Type', 'N/A')
                name_slug = name.replace(' ', '_').lower()
                profile_link = f"profiles/{era}/{name_slug}_{year}.html"
                
                players_html += f"""
                <tr>
                    <td><a href="{profile_link}" target="_blank">{name}</a></td>
                    <td>{position}</td>
                    <td>{school}</td>
                    <td>{year}</td>
                    <td><span class="badge">{milestone}</span></td>
                </tr>
                """
            
            era_sections += f"""
            <div class="era-section">
                <h3>{era}</h3>
                <table class="players-table">
                    <thead>
                        <tr>
                            <th>Player</th>
                            <th>Position</th>
                            <th>School</th>
                            <th>Year</th>
                            <th>Milestone</th>
                        </tr>
                    </thead>
                    <tbody>
                        {players_html}
                    </tbody>
                </table>
            </div>
            """
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CFB-Jay: College Football Max Dominance Vault</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
            border-bottom: 3px solid #2a5298;
            padding-bottom: 30px;
        }}
        h1 {{
            font-size: 3em;
            color: #1e3c72;
            margin-bottom: 10px;
        }}
        .subtitle {{
            font-size: 1.2em;
            color: #666;
            margin-bottom: 20px;
        }}
        .stats-banner {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }}
        .stat-card {{
            background: #f0f0f0;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            border-top: 3px solid #2a5298;
        }}
        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #2a5298;
        }}
        .stat-label {{
            color: #666;
            font-size: 0.9em;
        }}
        .nav-section {{
            margin: 30px 0;
        }}
        .nav-buttons {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }}
        .nav-button {{
            background: #2a5298;
            color: white;
            padding: 15px 20px;
            border-radius: 5px;
            text-decoration: none;
            text-align: center;
            font-weight: bold;
            transition: background 0.3s;
        }}
        .nav-button:hover {{
            background: #1e3c72;
        }}
        .era-section {{
            margin: 40px 0;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 8px;
            border-left: 5px solid #2a5298;
        }}
        .era-section h3 {{
            color: #1e3c72;
            margin-bottom: 15px;
            font-size: 1.5em;
        }}
        .players-table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
        }}
        .players-table th {{
            background: #2a5298;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
        }}
        .players-table td {{
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }}
        .players-table tr:hover {{
            background: #f0f0f0;
        }}
        .players-table a {{
            color: #2a5298;
            text-decoration: none;
            font-weight: bold;
        }}
        .players-table a:hover {{
            text-decoration: underline;
        }}
        .badge {{
            background: #2a5298;
            color: white;
            padding: 4px 10px;
            border-radius: 15px;
            font-size: 0.85em;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #eee;
            text-align: center;
            color: #666;
        }}
        @media (max-width: 768px) {{
            h1 {{
                font-size: 2em;
            }}
            .container {{
                padding: 20px;
            }}
            .stats-banner {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏈 CFB-Jay: College Football Max Dominance Vault</h1>
            <p class="subtitle">Comprehensive Database of Elite Performances (1970-2026)</p>
            <div class="stats-banner">
                <div class="stat-card">
                    <div class="stat-number">{len(self.players)}</div>
                    <div class="stat-label">Players</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{len(self.eras)}</div>
                    <div class="stat-label">Eras</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{len(self.conferences)}</div>
                    <div class="stat-label">Conferences</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{len(self.milestones)}</div>
                    <div class="stat-label">Milestone Types</div>
                </div>
            </div>
        </div>
        
        <div class="nav-section">
            <h2>Browse by Category</h2>
            <div class="nav-buttons">
                <a href="#heisman" class="nav-button">🏆 Heisman Winners</a>
                <a href="#records" class="nav-button">📊 Record-Holders</a>
                <a href="#eras" class="nav-button">📅 Browse by Era</a>
                <a href="docs/offensive_systems.html" class="nav-button">📋 Offensive Systems</a>
            </div>
        </div>
        
        <div id="eras">
            {era_sections}
        </div>
        
        <div class="footer">
            <p>CFB-Jay Vault • Comprehensive College Football Performance Database</p>
            <p>Last Updated: {datetime.now().strftime('%B %d, %Y')}</p>
            <p><a href="README.md">Documentation</a> | <a href="https://github.com/ckh5jkmb8z-sketch/CFB-Jay">GitHub Repository</a></p>
        </div>
    </div>
</body>
</html>
"""
        return html
    
    def run(self):
        """Execute full profile generation pipeline"""
        print("Loading data...")
        self.load_all_data()
        print(f"Loaded {len(self.players)} player records")
        
        print("Generating individual profiles...")
        self.generate_all_profiles()
        print(f"Generated profiles for {len(self.players)} players across {len(self.eras)} eras")
        
        print("Generating master index...")
        index_html = self.generate_index_html()
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(index_html)
        print("Master index generated: index.html")

if __name__ == '__main__':
    generator = ProfileGenerator()
    generator.run()
    print("\n✅ Profile generation complete!")
