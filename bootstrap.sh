#!/bin/bash
# Bootstrap script for The $24 Playbook project

echo "🚀 Bootstrapping The $24 Playbook..."

# Ensure directory structure
mkdir -p assets logs

# Mock PDF generation (simulated)
echo "Generating mock playbook.pdf from playbook.md..."
cp playbook.md playbook.pdf 

echo "✅ Build complete. Ready for deployment."
