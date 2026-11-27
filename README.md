# Yevqo — Official Website

A lightweight static website for Yevqo, a personal server platform built around Android and Termux.

## Project structure

- `index.html` — homepage
- `features/`, `how-it-works/`, `templates/`, `pricing/`, `faq/` — product pages
- `docs/` — documentation pages
- `css/global.css` — shared styles
- `js/main.js` — shared navigation and FAQ interactions
- `public/favicon.svg` — site icon

## Run locally

No Node.js, package manager, framework, build step or dependencies are required.

Open `index.html` directly, or start a local static server from the repository root:

```bash
python -m http.server 8080
```

Then open `http://localhost:8080`.

On Android, the same files can be served from Termux with Python or another static HTTP server. Keep the working directory at the repository root so relative paths resolve.

## Deployment

Publish the repository root as the static document root. The entry point is `index.html`; do not configure an Astro, Vite or Node build command.

## Product status

This repository contains the public static website and product documentation. The Yevqo Control Plane and Go Agent are implemented for beta testing. Dashboard illustrations are explicitly labelled as illustrative and are not live telemetry. The current Free beta permits one connected Android device; projects are not limited by count. Public package distribution, physical Android clean-install/upgrade acceptance and external-domain reachability remain launch gates. AI agents and public Pro checkout are not available.

## Marketing and release readiness

See [marketing/launch-readiness.md](marketing/launch-readiness.md) before publishing paid campaigns. Do not advertise one-click public hosting, production readiness, included domains, Docker-on-Android or a current public installer until the listed acceptance checks pass. The current release link must be refreshed with verified .deb packages and checksums before promoting installation.
