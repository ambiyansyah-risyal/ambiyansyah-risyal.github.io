# Data Model: Privacy-Safe Website Implementation

## Content Entities

### Posts
- **title**: String - Title of the post
- **content**: Markdown - Main content of the post
- **date**: DateTime - Publication date
- **tags**: Array<String> - Content tags for categorization
- **draft**: Boolean - Whether the post is a draft

### Pages
- **title**: String - Title of the page
- **content**: Markdown - Main content of the page
- **path**: String - URL path for the page
- **layout**: String - Template used to render the page

## Privacy Controls

### PrivacyConfiguration
- **trackingAllowed**: Boolean - Whether any tracking is allowed (should be false)
- **allowedCookies**: Array<String> - List of cookies that are allowed (only essential ones)
- **thirdPartyContentPolicy**: String - Policy for third-party content (privacy-safe alternatives only)
- **analyticsProvider**: String - Analytics provider (should be empty/none)

## Verification Entities

### PrivacyVerification
- **verificationDate**: DateTime - Date of last verification
- **trackingScriptsFound**: Array<String> - List of any tracking scripts found
- **status**: String - Overall verification status (PASS/FAIL)
- **details**: Object - Detailed breakdown of verification checks

## State Transitions

### Content State Transitions
1. **Draft** → **Published** (when content is ready for public access)
2. **Published** → **Archived** (when content is deprecated)

### Privacy Verification State Transitions
1. **Unverified** → **Verified** (after verification process is run)
2. **Verified** → **Failed** (if tracking is detected)

## Relationships
- Posts and Pages use PrivacyConfiguration for compliance
- PrivacyVerification checks Posts and Pages for compliance