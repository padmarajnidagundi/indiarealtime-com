# ~20 plugins is a maintainability bet, not a free lunch

The upside is fault isolation and independent scheduling: if one government API changes its response format or goes down, exactly one plugin breaks, and the other ~19 keep serving. The tradeoff is more surface area to keep consistent. Shared conventions (transient naming, cache durations, failure-flag patterns) have to be enforced by discipline and code review rather than a shared framework, since each plugin is deliberately self-contained.

Part of [IndiaRealTime](../README.md).
