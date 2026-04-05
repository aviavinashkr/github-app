#!/usr/bin/env python3
"""Simple Notes Application"""

import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    """Load notes from file"""
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_notes(notes):
    """Save notes to file"""
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=2)

def add_note(title, content):
    """Add a new note"""
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "created_at": datetime.now().isoformat()
    }
    notes.append(note)
    save_notes(notes)
    print(f"✓ Note added: {title}")

def list_notes():
    """List all notes"""
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    for note in notes:
        print(f"\n[{note['id']}] {note['title']}")
        print(f"    Created: {note['created_at']}")

def main():
    """Main application loop"""
    print("📝 Python Notes App")
    print("-" * 40)
    
    # Example usage
    add_note("First Note", "This is my first note!")
    add_note("Python Workflow", "Testing GitHub Actions workflow")
    list_notes()

if __name__ == "__main__":
    main()