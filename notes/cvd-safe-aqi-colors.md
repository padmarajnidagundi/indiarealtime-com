# Accessibility and color are load-bearing, not decorative

Every semantic color (success/warning/danger states, the AQI severity scale) is checked against WCAG contrast ratios *and* color-vision-deficiency (CVD) simulation, and documented with the actual ratio next to the hex code. The AQI bands specifically match the official CPCB scale rather than an arbitrary gradient, because an air-quality site getting a color wrong has real consequences for someone deciding whether to go outside.

Part of [IndiaRealTime](../README.md).
