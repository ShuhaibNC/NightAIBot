#!/bin/bash

echo "📦 Updating system..."
apt update

echo "🎥 Installing FFmpeg..."
apt install -y ffmpeg

echo "🐍 Starting your Python bot..."
python3 start.py