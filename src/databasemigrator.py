#!/usr/bin/env python3
"""
DatabaseMigrator - Database migration and versioning tool.
"""

from pathlib import Path
from typing import List, Dict
import json

class DatabaseMigrator:
    """Database migration manager."""
    def __init__(self, migrations_dir: str = "migrations"):
        self.migrations_dir = Path(migrations_dir)
        self.migrations_dir.mkdir(exist_ok=True)
    
    def create_migration(self, name: str, up_sql: str, down_sql: str) -> str:
        """Create a new migration."""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{name}.json"
        filepath = self.migrations_dir / filename
        
        migration = {
            "name": name,
            "up": up_sql,
            "down": down_sql,
            "timestamp": timestamp
        }
        
        with open(filepath, 'w') as f:
            json.dump(migration, f, indent=2)
        
        return str(filepath)
    
    def list_migrations(self) -> List[Dict]:
        """List all migrations."""
        migrations = []
        for filepath in sorted(self.migrations_dir.glob("*.json")):
            with open(filepath) as f:
                migrations.append(json.load(f))
        return migrations

if __name__ == "__main__":
    migrator = DatabaseMigrator()
    print("DatabaseMigrator initialized")
