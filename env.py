from dotenv import load_dotenv
import os
from typing import Final


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
print(dotenv_path)
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
        
TOKEN: Final = os.environ.get('TOKEN', 'define me!')
