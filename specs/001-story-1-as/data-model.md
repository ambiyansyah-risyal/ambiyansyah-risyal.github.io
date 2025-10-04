# Data Model: Hugo Site Structure

## Entities

### Hugo Site Structure
- **content/**: Directory containing all content
  - **posts/**: Blog posts in Markdown format
    - title: string - Post title
    - description: string - Post description
    - date: datetime - Publication date
    - tags: array<string> - Post tags
    - draft: boolean - Whether post is a draft
  - **portfolio/**: Portfolio items in Markdown format
    - title: string - Project title
    - description: string - Project description
    - date: datetime - Project date
    - tags: array<string> - Project tags
    - url: string - Project URL (optional)
    - images: array<string> - Project images (optional)

- **layouts/**: HTML templates
  - Single templates for content types
  - List templates for content collections
  - Partial templates for reusable components

- **static/**: Static assets
  - **css/**: Stylesheets
  - **js/**: JavaScript files
  - **images/**: Image assets

- **config/_default/**: Configuration files
  - config.toml: Main site configuration
  - params.toml: Site parameters
  - menu.toml: Navigation menu

- **themes/**: Hugo themes
  - Selected theme directory
  - Customizations and overrides

### Theme Configuration
- name: string - Theme name
- version: string - Theme version
- settings: object - Theme-specific configuration settings
- customCSS: array<string> - Custom CSS files to include
- customJS: array<string> - Custom JS files to include

## Validation Rules
1. All content files must have proper front matter
2. Dates must follow RFC3339 format
3. Tags must be lowercase alphanumeric with hyphens
4. Image files must be optimized for web
5. HTML must pass accessibility validation for WCAG AA compliance

## State Transitions
1. Content draft → published (when draft: false)
2. Development → staging → production (through GitHub Actions)