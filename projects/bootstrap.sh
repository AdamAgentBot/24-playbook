#!/bin/bash
# OpenClaw Autonomous Bootstrap Script
# $24 Playbook: The One-Click Co-Founder

echo "🦾 Bootstrapping your Autonomous AI Co-Founder..."

# Check dependencies
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Visit https://nodejs.org/"
    exit 1
fi

# Install OpenClaw
echo "📦 Installing OpenClaw..."
npm install -g openclaw

# Setup Workspace
echo "📂 Setting up your workspace at ~/.openclaw/workspace..."
mkdir -p ~/.openclaw/workspace

# Start the Gateway
echo "🚀 Starting the OpenClaw Gateway..."
openclaw gateway start

echo "✅ Success! Your autonomous co-founder is ready."
echo "👉 Run 'openclaw status' to check the connection."
