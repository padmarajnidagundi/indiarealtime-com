# Location routing without a rewrite-rule regex per state

Every Indian state and city page shares one routing path (`ir_state` / `ir_sub` / `ir_sub2` query vars parsed from the URL) instead of a hand-written WordPress rewrite rule per region. That's necessary at this scale, but it means URL parsing has its own edge cases (trailing slashes, category vs. city ambiguity) that get covered by dedicated test files rather than caught by hand.

Part of [IndiaRealTime](../README.md).
