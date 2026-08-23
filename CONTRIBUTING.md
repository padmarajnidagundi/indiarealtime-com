# Contributing to IndiaRealTime

Thank you for wanting to help! This guide covers how to contribute — whether it's adding a new data source, improving existing plugins, fixing bugs, or improving documentation.

## Quick Start

### Adding a New Data Source / Plugin

1. **Research the API**
   - Find the endpoint, authentication method, and response format
   - Check rate limits and terms of service
   - Document findings in `API/india-free-apis.md` or `API/india-paid-apis.md`

2. **Create the Plugin**
   ```
   wp-content/plugins/irt-<data-source-name>/
   ├── irt-<data-source-name>.php
   ├── includes/
   │   ├── fetcher.php        # API call logic
   │   ├── transformer.php    # Normalize response to schema
   │   └── cache.php          # Cache handling
   ├── tests/
   │   └── test-fetcher.php   # Unit tests
   └── readme.txt
   ```

3. **Follow the Fetcher Pattern**
   ```php
   // includes/fetcher.php
   class IRT_<DataSource>_Fetcher {
       public function fetch() {
           // 1. Call external API
           // 2. Handle errors gracefully
           // 3. Return raw data
       }
   }
   ```

4. **Implement the Transformer**
   ```php
   // includes/transformer.php
   class IRT_<DataSource>_Transformer {
       public function transform($raw_data) {
           // Normalize to irt-dataset-schema
           // Return structured data for caching
       }
   }
   ```

5. **Add Cache Fallback**
   - On fetch failure, serve last cached value
   - Set appropriate cache TTL based on data freshness requirements
   - See [stale-cache-fallback.md](notes/stale-cache-fallback.md)

6. **Test Locally**
   ```bash
   docker-compose up
   wp-cli plugin activate irt-<data-source-name>
   wp eval 'do_action("irt_fetch_<data_source>")'
   ```

7. **Submit PR with**
   - Plugin code
   - Unit tests (≥80% coverage)
   - Updated `API/` documentation
   - Screenshot of data rendering

## Code Style

### PHP
- PSR-12 coding standard
- Prefix all functions: `irt_`
- Use WordPress hooks, not direct database queries
- Add i18n strings with `__()` and `_e()`

### JavaScript
- ES6+ syntax
- ESLint config in repo root
- Use `const` by default
- Comment complex logic

### Documentation
- Markdown format
- Code examples are runnable
- Link to source data docs

## Testing

```bash
# Run all tests
npm test

# Run specific plugin tests
npm test -- --plugin=irt-mandi-prices

# Check code coverage
npm run coverage
```

## Reporting Issues

Use [GitHub Issues](../../issues) with:
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
   npm run lint
   npm test
   npm run coverage
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

### Plugin Independence
Each plugin is isolated — if one breaks, others keep working. This means:
- Don't share databases or caches between plugins
- Don't depend on load order
- Each plugin owns its fetch schedule

### Caching Strategy
- `transient` for short-term cache (use WordPress transients API)
- Serve stale data on fetch failure rather than erroring
- Set different TTLs based on data freshness: 6h for prices, 24h for historical, etc.

### Schema
All normalized data follows [irt-dataset-schema](https://schema.org). Use JSON-LD for machine-readable output.

### Monitoring
Register your plugin with `irt-api-health-monitor` so failures are visible:
```php
do_action('irt_register_health_check', [
    'plugin' => 'irt-<name>',
    'endpoint' => 'https://api.example.com/data',
    'check_interval' => '6 hours',
    'alert_email' => 'your@email.com'
]);
```

## Documentation to Update

When adding a plugin, update:
- `API/india-free-apis.md` or `API/india-paid-apis.md` (add source to table)
- `README.md` (if new category)
- Plugin's own `readme.txt` (for WordPress.org listing)
- Example in `docs/examples/` if major feature

## Getting Help

- **Questions?** Open a [GitHub Discussion](../../discussions)
- **Design feedback?** Comment on issues before coding
- **Technical help?** Tag maintainers with @padmarajnidagundi

## Recognition

- All contributors are listed in `CONTRIBUTORS.md`
- Major plugins get a blog post featuring the contributor
- 10+ merged PRs → maintainer role

## Code of Conduct

Be respectful. We don't tolerate harassment, discrimination, or abuse. Report issues to [email].

---

**Thank you for making IndiaRealTime better!** 🇮🇳
