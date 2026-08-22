# Serving stale data on purpose

Government and exchange APIs are not reliable, and the site still has to look reliable.

Fuel price and commodity sources fail, rate-limit, or return malformed data often enough that "just show what the API returned" isn't viable. The fix was a stale-while-revalidate style cache: fetch fails silently fall back to the last successfully cached value (comment in the code literally says *"serving yesterday's cached transient value"*), with a short-lived failure flag so retries don't hammer a source that's already down. Visitors see a slightly-stale number instead of a broken page.

Part of [IndiaRealTime](../README.md).
