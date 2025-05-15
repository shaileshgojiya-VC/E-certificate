#!/bin/bash

# Timestamp for filenames
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
raw_file="raw_terminal_$timestamp.txt"
clean_file="terminal_history_$timestamp.txt"

# Use a simple prompt
export PS1='\u@\h:\w\$ '

# Start recording using a minimal bash session
echo "Recording session... type 'exit' to stop."
script -q -c "bash --norc --noprofile" "$raw_file"

# Clean the raw output with robust escape sequence remover
perl -pe 's/\e\[?.*?[@-~]//g' "$raw_file" > "$clean_file"

# Optional: remove the raw noisy file
rm "$raw_file"

echo "✅ Clean session saved to: $clean_file"

