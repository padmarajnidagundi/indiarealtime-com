# PyPI Publishing Setup Guide for IndiaRealTime

This guide walks you through publishing the `indiarealtime` package to PyPI using GitHub OIDC (Trusted Publishing).

## Step 1: Fill in PyPI Trusted Publishing Form

Go to: https://pypi.org/manage/account/publishing/

Fill in the following information:

### Field Values

| Field | Value |
|-------|-------|
| **PyPI Project Name** | `indiarealtime` |
| **Owner** | `padmarajnidagundi` |
| **Repository name** | `indiarealtime-com` |
| **Workflow name** | `publish-pypi.yml` |
| **Environment name** | `pypi` |

### Explanations

- **PyPI Project Name**: This is how your package will be named on PyPI (e.g., `pip install indiarealtime`)
- **Owner**: Your GitHub username
- **Repository name**: The GitHub repository containing your code
- **Workflow name**: The GitHub Actions workflow file (already created at `.github/workflows/publish-pypi.yml`)
- **Environment name**: GitHub Actions environment for security (already configured in the workflow)

## Step 2: Verify Prerequisites

Before proceeding, ensure:

✅ You have a PyPI account: https://pypi.org/account/register/
✅ The workflow file exists: `.github/workflows/publish-pypi.yml` (created ✓)
✅ Your `setup.py` has correct metadata (already configured ✓)

## Step 3: Create a Release to Test

```bash
# Commit the workflow file
git add .github/workflows/publish-pypi.yml
git commit -m "Add PyPI publishing workflow"
git push origin main

# Create a test release tag
git tag -a v0.1.0 -m "First release"
git push origin v0.1.0
```

This will trigger the workflow and publish to PyPI.

## Step 4: Verify on PyPI

After the workflow completes:
- Visit: https://pypi.org/project/indiarealtime/
- Install and test: `pip install indiarealtime`

## Automatic Publishing

After setup, every time you push a tag matching `v*`:
```bash
git tag -a v0.2.0 -m "Release version 0.2.0"
git push origin v0.2.0
```

The package will automatically build and publish to PyPI.

## Troubleshooting

### Workflow fails with "Permission denied"
- Ensure PyPI Trusted Publishing is configured correctly
- Check that project name matches exactly: `indiarealtime`

### "No such file or directory: setup.py"
- Verify `setup.py` exists in repo root
- Check it's staged in git: `git ls-files | grep setup.py`

### Build fails
- Run locally: `python -m build`
- Fix any errors in setup.py
- Check Python version compatibility (3.8+)

## Manual Publishing (Fallback)

If OIDC doesn't work, use API tokens:

1. Create PyPI API token at: https://pypi.org/manage/account/tokens/
2. Add as GitHub secret: `PYPI_API_TOKEN`
3. Modify workflow to use:
   ```yaml
   - uses: pypa/gh-action-pypi-publish@release/v1
     with:
       password: ${{ secrets.PYPI_API_TOKEN }}
   ```

## Resources

- [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
- [GitHub OIDC Documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [setuptools Documentation](https://setuptools.pypa.io/)
