# Snyk Projects Manager

This repository manages Snyk projects using the Snyk API. It provides a centralized way to configure and synchronize Snyk projects across your organization.

## 📋 Overview

The repository contains:
- **Configuration file**: `snyk-projects.yml` - Defines project settings and branches
- **Sync script**: `scripts/sync-snyk-projects.py` - Python script to create/update projects via Snyk API

## ✨ Features

- **Centralized Configuration**: Manage all Snyk projects in a single YAML file
- **Automated Project Import**: Script automatically imports projects that don't exist
- **Branch Management**: Configure specific branches for each project
- **Organization Integration**: Works with Snyk organization `38bc7259-fb9b-4413-b69a-741f25d5d5bf`
- **GitHub Integration**: Uses GitHub integration for project import

## Project Structure

```
snyk-projects/
├── README.md                    # This file
├── snyk-projects.yml           # Project configuration
├── scripts/
│   └── sync-snyk-projects.py   # Sync script
└── .github/
    └── workflows/
        └── sync-snyk-projects.yml  # GitHub Action workflow
```

## 🔧 Prerequisites

- Python 3.x
- Snyk account with API access
- Snyk API token
- GitHub integration configured in Snyk

## ⚙️ Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd snyk-projects
   ```

2. **Set up your Snyk API token**:
   ```bash
   export SNYK_TOKEN='your-snyk-api-token'
   ```
   
   You can get your API token from:
   - Snyk → Account Settings → API Token

3. **Install Python dependencies**:
   ```bash
   pip install requests pyyaml
   ```

## ⚙️ Configuration

Edit `snyk-projects.yml` to define your projects:

```yaml
projects:
  - name: "spring-boot-template"
    branch: "main"

  - name: "products-search-api"
    branch: "main"
```

### Configuration Options

- **name**: The repository name to import into Snyk
- **branch**: The branch to monitor (defaults to "main" if not specified)

## 🚀 Usage

### Manual Execution

Run the sync script to import/update projects:

```bash
python scripts/sync-snyk-projects.py
```

### Automated Execution via GitHub Actions

The repository includes a GitHub Action workflow that automatically runs the sync script whenever changes are made to the `main` branch that affect the `snyk-projects.yml` file.

**When it triggers:**
- Push to `main` branch with changes to `snyk-projects.yml`
- Manual workflow dispatch

**What it does:**
1. Checks out the repository
2. Installs Python dependencies
3. Runs the sync script with the configured `SNYK_TOKEN` secret

### What the script does:
1. Read the project configuration from `snyk-projects.yml`
2. Check if each project exists in Snyk
3. Import new projects that don't exist using the GitHub integration
4. Skip projects that already exist
5. Display status messages for each operation

## 🔌 API Integration

The script uses the following Snyk API endpoints:
- `GET /rest/orgs/{org-id}/projects` - List existing projects
- `POST /v1/orgs/{org-id}/integrations/{integration-id}/import` - Import new project

## 🤝 Contributing

1. Add new projects to `snyk-projects.yml`
2. Run the sync script to import them
3. Commit both the configuration and any script improvements

## 🔧 Troubleshooting

**Error: SNYK_TOKEN environment variable is not set**
- Make sure you've exported your Snyk API token

**API request failed**
- Verify your API token has the necessary permissions
- Check your network connection to Snyk

**Failed to import project**
- Ensure the repository exists in GitHub
- Verify the GitHub integration is properly configured in Snyk
- Check that the specified branch exists in the repository

**Project already exists**
- The script will skip projects that are already imported
- This is normal behavior to avoid duplicate imports
