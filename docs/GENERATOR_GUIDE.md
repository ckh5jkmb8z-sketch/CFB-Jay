# Python Generator Script Guide

## Overview
The `generate_profiles.py` script automatically generates individual HTML profiles for every player in the vault, organized by era.

## Features

### Automatic Profile Generation
- Reads all data from CSVs in `/data` directory
- Creates individual HTML profile for each player
- Organized into era-specific directories (1970s/, 1980s/, etc.)
- Includes game stats, season stats, career stats, and theoretical maxes
- Embeds YouTube links (full game + highlights)
- Spoiler-free descriptions
- Advanced analytics display

### Master Index Generation
- Creates `index.html` at vault root
- Displays all players organized by era
- Sortable tables by position, school, year, milestone type
- Navigation buttons to browse by category
- Stats banner showing total counts
- Responsive design for mobile/desktop

### Profile Features
Each player profile includes:
- Player metadata (position, school, conference, year, era)
- Performance statistics (game/season/career)
- Theoretical maximum calculations
- Offensive/defensive system info
- Advanced analytics (EPA, success rate, efficiency %)
- Dual YouTube links with spoiler-free descriptions
- Milestone classification (Heisman, record-holder, etc.)
- Back navigation to master index

## Usage

```bash
cd CFB-Jay
python scripts/generate_profiles.py
```

## Output Structure

```
CFB-Jay/
├── index.html (Master index)
├── profiles/
│   ├── 1970s/
│   │   ├── jim_brown_1956.html
│   │   ├── jack_tatum_1969.html
│   │   └── ...
│   ├── 1980s/
│   │   ├── barry_sanders_1988.html
│   │   ├── reggie_white_1983.html
│   │   └── ...
│   ├── 1990s/
│   │   └── ...
│   ├── 2000s/
│   │   └── ...
│   ├── 2010s/
│   │   ├── trent_richardson_2011.html
│   │   ├── johnny_manziel_2012.html
│   │   └── ...
│   └── 2020s/
│       └── ...
└── data/
    ├── sec_performances.csv
    ├── big_ten_performances.csv
    └── ...
```

## File Naming Convention
- Profile files: `{firstname_lastname}_{year}.html`
- All lowercase, spaces replaced with underscores
- Located in era-specific subdirectory

## Customization

### To add new fields to profiles:
1. Edit `generate_player_profile()` method
2. Add new stat-box divs in the stats-section
3. Reference player dict key (e.g., `player.get('FieldName')`)

### To change styling:
1. Modify CSS in `<style>` section
2. Update color scheme (currently #2a5298 blue primary)
3. Adjust grid layouts as needed

### To add new organizing categories:
1. Add new dictionary in `__init__` (e.g., `self.positions`)
2. Populate in `organize_player()` method
3. Add section to `generate_index_html()` for navigation

## Performance
- Generates 50+ profiles in < 5 seconds
- Index page loads in < 1 second
- Responsive design optimized for all devices
- All links are YouTube search queries (no video embeds to reduce size)

## Future Enhancements
- Add search functionality
- Add filtering by position/conference
- Add statistical comparison charts
- Add video embedding with thumbnails
- Add community ratings/comments section
