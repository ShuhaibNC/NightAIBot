#!/bin/bash

echo "📦 Updating system..."
sudo apt update

echo "🎥 Installing FFmpeg..."
sudo apt install -y ffmpeg

echo "🐍 Starting your Python bot..."
python3 start.py