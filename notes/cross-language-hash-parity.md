# A hash has to agree across two languages

Author attribution computes a hash on the PHP backend and again in JS on the frontend. PHP and JavaScript disagree on integer overflow by default, so the JS side has to explicitly use `Math.imul` to reproduce PHP's 32-bit wraparound. Otherwise the two sides silently compute different values and attribution breaks in a way that's invisible until someone checks production data.

Part of [IndiaRealTime](../README.md).
