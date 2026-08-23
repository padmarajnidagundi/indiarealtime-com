# How to Contribute

Thank you for your interest in IndiaRealTime! We welcome contributions of all kinds.

## Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/indiarealtime-com.git
   cd indiarealtime-com
   ```

2. **Set up development environment**
   ```bash
   # Python SDK
   pip install -e ".[dev]"
   
   # Or with Docker
   docker-compose up
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Types of Contributions

### 🐛 Bug Reports
Found a broken API or data issue?
- [Open a bug report](https://github.com/padmarajnidagundi/indiarealtime-com/issues/new?template=bug_report.md)
- Include: reproduction steps, expected vs actual, environment details

### ✨ Feature Requests
Have an idea for a new data source or feature?
- [Request a feature](https://github.com/padmarajnidagundi/indiarealtime-com/issues/new?template=feature_request.md)
- Include: use case, example API, why it's valuable

### 📚 Documentation
Help improve our docs?
- Fix typos and unclear sections
- Add examples and tutorials
- Improve API documentation

### 💻 Code Contributions

#### Add a New Data Source (Plugin)
See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed plugin development guide.

Quick checklist:
- [ ] Research API and document in `API/`
- [ ] Create plugin following pattern
- [ ] Add tests (≥80% coverage)
- [ ] Test locally with Docker
- [ ] Update README
- [ ] Submit PR

#### Improve SDK
Help improve the Python SDK or CLI:
- Add new client methods
- Fix bugs
- Improve error handling
- Add type hints

#### Build Examples
Create new examples in `examples/`:
- React dashboard
- Node.js scraper
- Lambda function
- Discord bot
- etc.

#### Improve Tests
- Increase code coverage
- Add integration tests
- Test edge cases
- Performance benchmarks

## Code Standards

### Python
```bash
# Format
black indiarealtime/ tests/

# Lint
flake8 indiarealtime/ tests/

# Type check
mypy indiarealtime/

# Test
pytest tests/ --cov=indiarealtime
```

### Commit Messages
```
feat: Add mandi price alerts
fix: Handle missing commodity names
docs: Improve API documentation
test: Add currency rate tests
chore: Update dependencies
```

### PR Description Template
```markdown
## Description
What does this PR do?

## Changes
- Change 1
- Change 2

## Testing
How to test this?

## Screenshots
Before/after if applicable

## Related Issues
Fixes #123
```

## Review Process

1. Your PR will be reviewed within 48 hours
2. Make requested changes by pushing to your branch
3. Respond to review feedback
4. Once approved, your PR will be merged
5. Your name will be added to CONTRIBUTORS.md

## Recognition

Contributors get:
- Recognition in [CONTRIBUTORS.md](CONTRIBUTORS.md)
- Attribution in commit messages
- Feature showcase in blog posts (for major contributions)
- Maintainer status after 5 merged PRs

## Questions?

- **Documentation**: Check [README.md](README.md) and [notes/](notes/)
- **Architecture**: See [Architecture](README.md#architecture)
- **Plugin development**: See [CONTRIBUTING.md](CONTRIBUTING.md)
- **Ask in Discussions**: [GitHub Discussions](https://github.com/padmarajnidagundi/indiarealtime-com/discussions)

---

**Happy contributing!** 🇮🇳
