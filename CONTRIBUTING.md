# Contributing to IndiaRealTime

Thank you for wanting to help! This guide covers how to contribute to the open parts of this repository.

## What Is Open in This Repository

IndiaRealTime's production WordPress codebase is private right now. Contributions are welcome in these public areas:

- `indiarealtime/` - Python SDK + CLI
- `tests/` - SDK and CLI test coverage
- `API/` - Public India API catalog and source notes
- `examples/` - Integration examples (FastAPI, bots, dashboards)
- `scripts/` - Standalone fetch/normalize examples
- `docs/` and `notes/` - Technical documentation and engineering decisions

## Quick Start

### Adding a New Data Source

1. **Research the API**
   - Find the endpoint, authentication method, and response format
   - Check rate limits and terms of service
   - Document findings in `API/india-free-apis.md` or `API/india-paid-apis.md`

2. **Contribute in this repo**
   - Add/update API documentation in `API/`
   - Add SDK support in `indiarealtime/` when applicable
   - Add or update examples in `examples/`
   - Add tests in `tests/`

3. **Follow the fetch → validate → normalize pattern**
   - Fetch source data with clear error handling
   - Validate required fields before exposing data to users
   - Normalize output shape so SDK/examples stay consistent

4. **Add Cache Fallback**
   - On fetch failure, serve last cached value
   - Set appropriate cache TTL based on data freshness requirements
   - See [stale-cache-fallback.md](notes/stale-cache-fallback.md)

5. **Test Locally**
   ```bash
   pip install -e ".[dev]"
   pytest tests/ --cov=indiarealtime
   ```

6. **Submit PR with**
   - Updated `API/` documentation and/or SDK code
   - Unit tests for behavior changes
   - Example updates if user-facing workflows change

## Code Style

### Python (SDK/CLI)
- Follow existing project style in `indiarealtime/`
- Add type hints for new public methods where practical
- Keep user-facing errors actionable

### JavaScript
- Applies to `examples/` and `scripts/` contributions
- Use modern, readable ES6+ syntax
- Prefer `const` by default
- Keep external API handling and normalization logic explicit

### Documentation
- Markdown format
- Code examples are runnable
- Link to source data docs

## Testing

```bash
# Run all tests
pytest tests/

# Check code coverage
pytest tests/ --cov=indiarealtime
```

## Reporting Issues

Use [GitHub Issues](https://github.com/padmarajnidagundi/indiarealtime-com/issues) with:
- **Clear title**: "AQI API returns 500 on Sundays"
- **Reproduction steps**: curl command, screenshot, timestamp
- **Expected vs actual**: "Expected AQI for Delhi, got generic error"
- **Environment**: OS, browser, WordPress version

Label your issue:
- `bug` - Something broken
- `new-api` - Suggest a new data source
- `enhancement` - Improve existing feature
- `documentation` - Docs/examples need work
- `good-first-issue` - Good for newcomers

## Pull Request Process

1. **Fork and create a branch**
   ```bash
   git checkout -b feature/add-<data-source>
   ```

2. **Make your changes**
   - Keep commits atomic and well-messaged
   - Add tests for new functionality
   - Update documentation

3. **Run quality checks**
   ```bash
   black indiarealtime/ tests/
   flake8 indiarealtime/ tests/
   mypy indiarealtime/
   pytest tests/ --cov=indiarealtime
   ```

4. **Push and open PR**
   - Reference related issues: "Fixes #123"
   - Describe what changed and why
   - Link to API docs you used

5. **Respond to review feedback**
   - We'll review within 48 hours
   - Update code if requested
   - Re-request review when ready

## Architecture Notes

### Data Source Independence
Data sources are handled independently in production so one failing upstream should not break unrelated data flows. Keep that principle when proposing new SDK methods, docs, or example patterns.

### Caching Strategy
- Prefer stale-cache fallback semantics in integrations where source reliability is low
- Document expected refresh cadence per source
- Clearly separate fresh vs cached responses in examples

### Schema
Use [schema.org](https://schema.org) JSON-LD for machine-readable output. For most source entries, align primarily with [schema.org/Dataset](https://schema.org/Dataset), and choose additional types when a data category is better represented by another schema type.

### Monitoring
If you add new fetch scripts or API integrations, document health signals (status checks, expected response shape, stale fallback behavior) so failures are easy to detect and debug.

## Documentation to Update

When adding a source or integration, update:
- `API/india-free-apis.md` or `API/india-paid-apis.md` (add source to table)
- `README.md` (if new category)
- Related example in `examples/` if major feature

## Getting Help

- **Questions?** Open a [GitHub Discussion](https://github.com/padmarajnidagundi/indiarealtime-com/discussions)
- **Design feedback?** Comment on issues before coding
- **Technical help?** Tag maintainers with @padmarajnidagundi

## Recognition

- All contributors are recognized via repository history and contributor docs
- Major contributions may be highlighted in project updates
- 10+ merged PRs → maintainer role

## Code of Conduct

Be respectful. We don't tolerate harassment, discrimination, or abuse. Report issues to [email].

---

**Thank you for making IndiaRealTime better!** 🇮🇳
