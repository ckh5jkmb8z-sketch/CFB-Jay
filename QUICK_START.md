# CFB-Jay: Quick Start & Navigation Guide

## 🚀 Getting Started

**You are currently viewing the CFB-Jay vault home page.**

### How to Browse the Vault

1. **Via index.html (this file):**
   - Opens in your browser
   - Shows all players organized by era
   - Click any player name to view their full profile
   - Each profile includes game footage links and complete statistics

2. **Via GitHub:**
   - https://github.com/ckh5jkmb8z-sketch/CFB-Jay
   - View raw data in `/data/` directory (CSV files)
   - Download entire vault for local use

### 📂 Repository Structure

```
CFB-Jay/
├── README.md                          # Main documentation
├── index.html                         # Master vault index (START HERE)
├── QUICK_START.md                     # This file
├── docs/
│   ├── offensive_systems.md           # All offensive system classifications
│   ├── defensive_formations.md        # All defensive formation classifications
│   ├── player_categories.md           # Player classification system
│   ├── era_breakdown.md               # Historical era guide
│   └── GENERATOR_GUIDE.md             # Python script documentation
├── data/                              # Raw performance data
│   ├── sec_performances.csv           # SEC conference performances
│   ├── big_ten_performances.csv       # Big Ten performances
│   ├── pac12_performances.csv         # Pac-12 performances
│   ├── acc_performances.csv           # ACC performances
│   ├── big12_performances.csv         # Big 12 performances
│   ├── mac_aac_g5_performances.csv    # MAC/AAC/G5 performances
│   └── independent_performances.csv   # Independent school performances
├── profiles/                          # Individual player HTML profiles (generated)
│   ├── 1970s/
│   ├── 1980s/
│   ├── 1990s/
│   ├── 2000s/
│   ├── 2010s/
│   └── 2020s/
└── scripts/
    └── generate_profiles.py           # Profile generation script
```

## 📊 Featured Players

### 🏅 Heisman Trophy Winners (12)
- **Tim Tebow** (2008, Florida) - Dual-threat QB dominance
- **Johnny Manziel** (2012, Texas A&M) - Historic upset over #1 Alabama
- **Robert Griffin III** (2011, Baylor) - Elite athleticism
- **Marcus Mariota** (2014, Oregon) - Peak efficiency
- **Desmond Howard** (1991, Michigan) - Return specialist elite
- **Charlie Ward** (1993, Florida State) - ACC rivalry excellence
- **Chris Weinke** (2000, Florida State) - Elite passing
- **Lamar Jackson** (2016, Louisville) - Speed and rushing dominance
- **Earl Campbell** (1977, Texas) - Wishbone era power
- **Barry Sanders** (1988, Oklahoma State) - 2628 rushing yard season
- **Ty Detmer** (1990, BYU) - Air Raid passing mastery
- **Marcus Allen** (1981, USC) - Vision and power running

### 📊 National Record-Holders
- **Barry Sanders** - 3932 career rushing yards (1988)
- **Ty Detmer** - 15,665 career passing yards
- **Ron Dayne** - 6,397 career rushing yards
- **Marcus Mariota** - 14,043 career passing yards
- **Reggie Bush** - Elite versatility (rushing + receiving)
- **O.J. Simpson** - Historic Pac-12 rushing dominance

### ⚡ Elite Specialists
- **Trent Richardson** (Alabama) - Elite vision and burst
- **Dri Archer** (Kent State) - MAC speed demon
- **Billy "White Shoes" Johnson** - Return specialist legend
- **Jeff Demps** (Alabama) - Track-caliber speed
- **Josh Cribbs** (Kent State) - Dynamic returner and receiver

### 🛡️ Defensive Standouts
- **Charles Tillman** (South Carolina) - Elite gap control
- **Reggie White** (Tennessee) - DE dominance
- **Brian Bosworth** (Oklahoma) - Linebacker machine
- **Jack Tatum** (Ohio State) - Safety excellence
- **Chris Spielman** (Ohio State) - Multi-year dominance
- **Lee Roy Selmon** (Oklahoma) - Option era fundamental excellence
- **Lester Hayes** (UC Berkeley) - Cornerback elite
- **Al Worley** (Washington) - Coverage prowess

## 📈 Data Included Per Player

Each player record contains:
- **Basic Info:** Position, school, conference, year, era
- **Game Statistics:** Rushing/receiving/passing/defensive stats from specific performance
- **Season Statistics:** Full season performance metrics
- **Career Statistics:** Complete career totals
- **Theoretical Maximum:** Peak performance calculations
- **Advanced Analytics:** EPA, success rate %, efficiency metrics
- **System Classification:** Offensive and defensive system used
- **YouTube Links:** 
  - Column A: Full game broadcast link
  - Column B: Highlights reel link
- **Spoiler-Free Description:** Game context without spoiling results

## 🎯 How to Use the Data

### For Casual Browsing:
1. Open `index.html` in your browser
2. Browse players by era
3. Click any player name
4. View profile with stats and YouTube links

### For Data Analysis:
1. Download CSV files from `/data/` directory
2. Open in Excel, Google Sheets, or Python
3. Analyze trends across eras and conferences
4. Compare offensive/defensive systems

### For Developers:
1. Run Python generator script: `python scripts/generate_profiles.py`
2. Generates individual HTML profiles for each player
3. Creates master index with navigation
4. Outputs to `/profiles/` organized by era

## 🔍 Search & Filter Options

### By Era:
- 1950s-1960s: Classic Era
- 1970s: Wishbone & Option Dominance
- 1980s: Transition & Emergence
- 1990s: Modern Spread Begins
- 2000s: Spread Dominance Era
- 2010s: Uptempo Revolution
- 2020s: Modern Hybrid Era

### By Milestone Type:
- Heisman Trophy Winners
- National Record-Holders
- All-American Selections
- Era-Defining Performances
- Conference Elite
- Notable Specialists
- Defensive Standouts
- Return Specialist Elite

### By Offensive System:
- Wishbone, Veer, Power Option
- Spread, Air Raid, Run & Shoot
- Pro-Style, I-Form
- Option varieties (Read Option, Triple Option)
- Modern RPO and tempo systems

### By Defensive Formation:
- 4-4, 5-2, 6-2, 4-3
- 3-4 (Base, Nickel, variants)
- Nickel, Dime, Quarter packages
- Cover 0-4 shell coverages
- Exotic blitz packages

## 📱 Mobile & Desktop Access

- **Desktop:** Full table view with all statistics
- **Tablet:** Responsive grid layout
- **Mobile:** Optimized single-column view

All profiles use responsive design for optimal viewing.

## 🔗 External Links

Each player profile includes YouTube search query links:
- **Full Game:** Direct YouTube search for complete broadcast
- **Highlights:** Curated highlights reel search
- All links open in new tabs (no external embeds)

## 📞 Support & Updates

- **GitHub Issues:** Report problems or request features
- **Data Contributions:** Community-sourced performance data welcome
- **Profile Additions:** Process for adding new players documented

## ✨ Coming Soon

- Video thumbnail integration
- Advanced search functionality
- Statistical comparison tools
- Player rating system
- Community discussion threads
- Mobile app version

---

**Ready to explore?** Start with `index.html` to browse all players!
