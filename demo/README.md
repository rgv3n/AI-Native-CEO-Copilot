# Interactive CEO Demo

This folder contains a self-contained public executive demo for AI-Native CEO Copilot.

## What it demonstrates

- executive questions instead of technical prompts,
- Finance, Sales and Operations perspectives,
- cross-functional evidence reconciliation,
- decision options and trade-offs,
- explicit recommendation,
- confidence, authority and urgency,
- a visible decision trace,
- CompaniesAutomation implementation support.

## Important

This public demo is deterministic and uses synthetic Northstar Industrial Systems S.L. data.

It deliberately does **not** call an external LLM or paid API. That keeps the public demo free to run and makes its behavior reproducible.

A production implementation can replace the deterministic demo layer with governed agents, real enterprise connectors, model routing and private / hybrid / NVIDIA-accelerated inference.

## Running locally

Open `index.html` in a browser or serve the folder with any static web server.

It can also be published through GitHub Pages or hosted under a CompaniesAutomation domain.
