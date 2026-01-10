# Importing needed libraries
import os
import yaml
from pathlib import Path
from typing import Any,Dict,Optional
from dataclasses import dataclass

# Config class 
@dataclass
class Config:
    def __init__(self, config_dict: Dict[str: Any]):
        self._config = config_dict

    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Get config value using dot notation.
        
        Example:
            config.get("retry.max_retries")  # Returns 3
            config.get("tokens.context_management.hard_prompt_cap")
        """
        keys = key_path.split(".")
        value = self._config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def __getitem__(self, key: str) -> Any:
        """Allow dict-style access."""
        return self._config[key]
    
    def __contains__(self, key: str) -> bool:
        """Check if key exists."""
        return key in self._config
    
    @property
    def raw(self) -> Dict[str, Any]:
        """Get raw config dict."""
        return self._config
    

# Global config instance
_config: Optional[Config] = None
