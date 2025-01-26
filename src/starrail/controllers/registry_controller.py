import winreg

from .star_rail_app import HonkaiStarRail

class SRRegistry:
    
    def __init__(self, starrail_instance: HonkaiStarRail):
        self.starrail_instance = starrail_instance
    
    
    
    def update_fps(self, new_fps: int) -> bool:
        if not isinstance(new_fps, int):
            return False
        
        # set fps
        return True
    
    
    def __read_registry(self, registry_path, registry_key_name):
        try:
            registry_key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, 
                registry_path, 
                0, 
                winreg.KEY_READ
            )
            
            # Read the value
            value, regtype = winreg.QueryValueEx(registry_key, registry_key_name)
            winreg.CloseKey(registry_key)
            
            # Print the value
            print(f"Value: {value}")
            return value
        except FileNotFoundError:
            print("The specified registry key or value does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    
    def __write_registry(self, registry_path, registry_key_name, new_value):
        pass
    
    
    
    

REGISTRY_PATH   = r"Software\miHoYo\崩坏：星穹铁道"
REGISTRY_KEY_NAME    = "GraphicsSettings_Model_h2986158309"




def read_registry_value(registry_path, registry_key_name):
    try:
        registry_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, 
            registry_path, 
            0, 
            winreg.KEY_READ
        )
        
        # Read the value
        value, regtype = winreg.QueryValueEx(registry_key, registry_key_name)
        winreg.CloseKey(registry_key)
        
        # Print the value
        print(f"Value: {value}")
        return value
    except FileNotFoundError:
        print("The specified registry key or value does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
read_registry_value(REGISTRY_PATH, REGISTRY_KEY_NAME)