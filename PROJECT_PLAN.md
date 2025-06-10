# Oddball Recruiting Challenges Project Plan

## Overview

This repository contains technical challenges used in Oddball's hiring process. These challenges are designed to assess candidates' skills during the third step of our hiring process. The challenges primarily consist of markdown files that provide instructions, context, and requirements for candidates.

## Project Structure
- The repository uses a two-level folder hierarchy:
  - **First level:** Each role has its own directory (e.g., `frontend-engineer`, `mobile-engineer`, etc.)
  - **Second level:** Each challenge for that role is a subdirectory within the role folder (e.g., `frontend-engineer/itunes-search`, `mobile-engineer/library-list`).
- Within each role directory:
  - A main `README.md` serves as an index to the challenges
  - Each challenge subdirectory contains its own `README.md` with specific instructions
  - Additional resource files may be included when necessary for completing challenges

## Guidelines

### Content

- All challenge descriptions should be clear, concise, and well-structured
- Maintain a friendly and welcoming tone consistent with Oddball's culture
- Provide sufficient context for candidates to understand what's expected
- Include evaluation criteria where appropriate

### Navigation

- Ensure all README files include proper navigation links
- All challenge subdirectories should be linked from their parent directory's README
- Use relative links for all internal navigation
- Regularly verify that all links are working

### Formatting

We use standard markdown formatting conventions to ensure clarity, consistency, and a professional appearance across all challenges and documentation. Please follow these guidelines:

- Every challenge README should begin with a title and include the following standard section headings:
  - `## Overview`
  - `## Requirements`
  - Additional sections as needed (e.g., `## Bonus (Optional)`, `## Evaluation Criteria`)
- Use one blank line between sections for readability.
- Use tables for structured data or comparisons whenever appropriate.
- Always use language labels in code blocks (e.g., ```python, ```bash) for syntax highlighting.

- Use headings (`#`, `##`, `###`) to organize content
- Use bullet points (`-`, `*`) for lists and requirements
- Use **bold** for emphasis and key terms (e.g., `**important**`)
- Use [links](https://example.com) for navigation and references
- Use code blocks with language labels for code, commands, and configuration examples:

```python
# Python example
def hello():
    print("Hello, Oddball!")
```

```bash
# Bash example
git clone https://github.com/oddballteam/recruiting-challenges.git
```

- Use tables for structured data or comparisons:

| Feature    | Supported | Notes           |
| ---------- | --------- | --------------- |
| Markdown   | Yes       | Standard syntax |
| Codeblocks | Yes       | Use labels      |

- Use images for branding and context:

![Oddball Logo](https://oddball.io/wp-content/uploads/2024/01/Oddball-Logo-High-Res.png)

- Use horizontal rules (`---`) to separate major sections

Maintain these conventions throughout all challenge and documentation files to provide a clear, welcoming, and professional experience for candidates and contributors.

## Maintenance

- Regularly review challenges to ensure they remain relevant
- Update technology requirements as needed
- Check for broken links periodically
- Ensure all challenge instructions are clear and error-free

## Adding New Challenges

When adding new challenges:

1. Create a new subdirectory within the appropriate role directory
2. Create a comprehensive README.md with clear instructions
3. Add any necessary resource files
4. Update the parent README.md to include a link to the new challenge
5. Verify all links work correctly

## Notes for Contributors

- Keep challenges focused on practical skills relevant to the role
- Design challenges to be completable within a reasonable timeframe
- Provide clear evaluation criteria for candidates
- Maintain a consistent difficulty level appropriate for the role
- Keep the scope to an appropriate degree that can be completed in the timeframe
- Any internal notes, for interviewers, should be stored in Google Drive with restricted access. It can be linked to from the challenge, labeled appropriately as internal.
- Each challenge should end with links to the appropriate next steps for realtime, take home, or either formats. This provides candidates with context for what to expect and how to prepare.
- Any new challenges or updated paths, should be updated in the recruiter's spreadsheet in Google Drive.
