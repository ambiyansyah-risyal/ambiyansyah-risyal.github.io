# Data Model: Clear and Readable Site Design

## Content Item
Represents the written content that needs to be presented clearly to users.

**Fields:**
- `title` (string): The title of the content piece
- `content` (string): The main body content in markdown/html format
- `author` (string): The author of the content
- `date` (date): The publication date
- `tags` (array of strings): Content categorization tags
- `readTime` (number): Estimated reading time in minutes
- `contentType` (string): Type of content (article, blog post, page, etc.)

**Validation:**
- `title` must be 1-200 characters
- `content` must not be empty
- `date` must be a valid date
- `readTime` must be a positive number

## Layout Component
Represents the structural elements that organize content in a readable manner.

**Fields:**
- `componentType` (string): Type of layout component (header, sidebar, container, etc.)
- `styling` (object): CSS properties and values
- `accessibilityProps` (object): ARIA labels and attributes for accessibility
- `responsiveBehavior` (object): How the component behaves on different screen sizes

**Validation:**
- `componentType` must be one of predefined values
- `styling` must contain valid CSS properties
- `accessibilityProps` must comply with WCAG 2.1 AA standards

## User Preference (Optional)
Represents user-specific preferences for content presentation.

**Fields:**
- `fontSizePreference` (string): Preferred font size (small, medium, large)
- `highContrastMode` (boolean): Whether to enable high contrast mode
- `readingWidth` (string): Preferred content width (narrow, medium, wide)

**Validation:**
- `fontSizePreference` must be one of the predefined values
- `highContrastMode` must be boolean