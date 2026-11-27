# Yevqo — advertising launch readiness

Last reviewed: 2026-11-27  
Product stage: **Free beta / Android ARM64 validation in progress**

## Positioning

Yevqo is an Android-first server control plane for people who want to run and manage their own applications in Termux. A Go Agent connects an Android device to a browser dashboard for projects, applications, builds, deployments, logs and device telemetry.

**Core promise:** Your Android. Your Server. Your Control.

**Accurate supporting points**
- Run supported workloads on Android + Termux; no VPS is required for local execution.
- Create a project application and have Yevqo provision its site on the selected Agent.
- Manage builds, deployment history, logs and device metrics from one dashboard.
- The current Free beta permits one connected Android device; project count is not capped.
- Seven first-party starter templates are available.

## Recommended first campaign

Until a refreshed public package and physical-device acceptance are complete, run only a small **beta-awareness / beta-registration** campaign. Send traffic to https://yevqo.cc.cd/ and use the “Join the beta” CTA to reach https://app.yevqo.cc.cd/register.

Do not run an “install now”, “host a public website in one click” or “production-ready hosting” campaign yet. Registration is available, but the latest public release is an older development artifact and should not be presented as the current installer.

## Audience

1. Android + Termux users who already run scripts, bots or small services.
2. Self-hosting and homelab enthusiasts interested in repurposing Android hardware.
3. Developers experimenting with lightweight personal APIs, static sites and automation.
4. Technical creators who can tolerate beta limitations and provide device feedback.

Avoid broad targeting of businesses looking for guaranteed uptime, managed hosting, enterprise SLAs or turnkey public web hosting.

## Ready-to-use ad copy

### Short social ad
**Your Android can be a server.**  
Yevqo brings projects, applications, builds and device monitoring into one control panel built around Android + Termux. Join the free beta.

### Search / text ad
**Run your projects on Android with Yevqo**  
An Android-first control plane for Termux. Manage applications, deployments and logs from one dashboard. Free beta · one connected device.

### Short video hook
“You already have a computer in your pocket. What if you could manage the services it runs from one dashboard? Meet Yevqo — built for Android and Termux.”

### CTA
**Join the beta** — not “Download now” until the current public package is verified and published.

## Claims that must not appear in ads

- “Production ready”, “enterprise hosting”, “guaranteed uptime” or “always online”.
- “One-click public hosting”, “free domain included” or “public URL automatically works”.
- “Docker runs natively on Android”.
- “Unlimited devices” on Free; Free is limited to one connected Android device.
- “AI agents available”; AI agents are roadmap-only.
- “Pro subscription available”; public checkout and billing are not available.
- “No network configuration needed”; public access depends on carrier/router, DNS and tunnel setup.
- “Fully tested on all Android devices”; physical-device coverage is incomplete.

## Hard launch gates before scaling paid ads

- [ ] Publish a fresh, correctly named Android ARM64 release with both intended .deb packages and SHA256SUMS; retire or clearly mark the old development artifact.
- [ ] Complete clean install, upgrade, service start, Agent pairing, application start/port check and reboot smoke tests on at least one real Android ARM64 device.
- [ ] Verify public website and app registration from an external network; test the complete registration flow and support path.
- [ ] Complete a real external-network test for at least one domain/tunnel route before advertising public hosting.
- [ ] Publish an owner-approved Privacy Notice and Terms, including data controller/contact, data collected, processors, retention, deletion and security disclosures.
- [ ] Publish a real support contact and incident/reporting route with an expected response process.
- [ ] Add privacy-compliant conversion measurement only after the privacy notice and consent requirements are settled.
- [ ] Capture real product screenshots/video from a verified device; keep illustrative dashboard mockups clearly labelled.

## Measurement

No analytics or ad pixels are currently configured in this static website. Use campaign UTM parameters for traffic attribution, but do not claim signup conversion tracking until a privacy-reviewed analytics path is installed and tested.

Suggested landing URL pattern:

https://yevqo.cc.cd/?utm_source=PLATFORM&utm_medium=paid_social&utm_campaign=beta_launch&utm_content=CREATIVE

## Current release facts checked for this plan

- The latest public VELTRIX Dock release is tagged Yevqo / Yevqo v0.1.0-beta.1, published 2026-11-21.
- It contains one named package, yevqo-all_0.1.0-dev.1640_aarch64.deb, plus an unnamed ZIP asset. It is not the latest CI build and has no published SHA256SUMS asset.
- A later CI package artifact contains both ARM64 packages and checksums, but it is a GitHub Actions artifact, not a refreshed public release.
- CI success proves automated build/package checks, not physical Android installation or public routing.
