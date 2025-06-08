#!/bin/bash
# Fails if agent.md refers to agents.md
if grep -n "agents.md" agent.md; then
  echo "Found outdated filename." >&2
  exit 1
fi
echo "Filename reference OK."
