#!/usr/bin/env python3
"""
File utility functions.
"""

import os
from pathlib import Path

def read_file(filepath):
    """Read file contents."""
    with open(filepath, 'r') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file."""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)

def file_exists(filepath):
    """Check if file exists."""
    return os.path.exists(filepath)


"""
Shiny Octo Eureka - Performance Improvement
"""

import logging
from functools import lru_cache

logger = logging.getLogger(__name__)

@lru_cache(maxsize=128)
def cached_computation(value):
    """Cached computation for better performance"""
    logger.debug(f"Computing value: {value}")
    # Complex computation here
    return value ** 2

def batch_process(items, batch_size=100):
    """Process items in batches for better memory usage"""
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        yield process_batch(batch)

def process_batch(batch):
    """Process a single batch"""
    return [item.upper() for item in batch]
