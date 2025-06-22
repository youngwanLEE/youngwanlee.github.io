# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Local Development
- **Run development server**: `bash run_server.sh` or `bundle exec jekyll liveserve`
  - Opens local server at http://127.0.0.1:4000
  - Includes live reload for automatic refresh when files change

### Dependency Management
- **Install dependencies**: `bundle install`
- **Update dependencies**: `bundle update`

### Google Scholar Citation Updates
- **Manual trigger**: Use GitHub Actions workflow "Update Google Scholar Citations"
- **Automatic**: Runs daily at midnight UTC via cron job
- **Local testing**: `cd google_scholar_crawler && python main.py`

## Architecture Overview

This is an academic personal homepage built on Jekyll with automated Google Scholar citation tracking.

### Core Components

**Jekyll Site Structure**:
- `_config.yml`: Main Jekyll configuration with site metadata, author profile, and CDN settings
- `_pages/about.md`: Main homepage content with publications and bio
- `_includes/`: Reusable HTML components (analytics, author profile, etc.)
- `_layouts/default.html`: Main page template
- `_sass/`: SCSS stylesheets for custom styling

**Google Scholar Integration**:
- `google_scholar_crawler/main.py`: Python script that fetches citation data using the scholarly library
- `google-scholar-stats/gs_data_shieldsio.json`: Citation data in shields.io format for badge display
- `_includes/fetch_google_scholar_stats.html`: JavaScript that dynamically loads citation counts into the page
- `.github/workflows/update-citations.yml`: GitHub Action that runs the crawler daily and commits updates

### Key Architectural Patterns

**Citation Display System**:
- Uses `<span class='show_paper_citations' data='PAPER_ID'></span>` tags to mark where individual paper citations should appear
- JavaScript fetches full citation data and populates these elements dynamically
- Total citations displayed via shields.io badge that pulls from the JSON file

**CDN Strategy**:
- `google_scholar_stats_use_cdn: true` in config enables CDN delivery via jsdelivr.net
- Falls back to raw GitHub URLs when CDN is disabled

**Error Handling**:
- Citation crawler includes timeout protection (8 minutes) and retry logic with exponential backoff
- Graceful degradation when Google Scholar blocks requests - preserves existing citation data

## File Organization

- **Content**: `_pages/about.md` contains all homepage content
- **Styling**: Custom CSS in `assets/css/` and SCSS in `_sass/`
- **Data**: Citation data stored in `google-scholar-stats/` branch
- **Scripts**: Python crawler in `google_scholar_crawler/`
- **Assets**: Images, fonts, and JavaScript in `assets/`

## Important Configuration

**Google Scholar ID**: Set as `GOOGLE_SCHOLAR_ID` environment variable (currently: EqemKYsAAAAJ)

**Jekyll Exclusions**: The build excludes documentation, crawler files, and development assets to keep the site clean.

**Citation Badge**: Displays real-time citation count from Google Scholar via automated daily updates.