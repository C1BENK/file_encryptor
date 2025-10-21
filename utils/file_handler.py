import os
import datetime
from rich.console import Console

console = Console()

class FileHandler:
    def __init__(self):
        pass
    
    def get_file_info(self, file_path: str) -> dict:
        """Get basic file information"""
        try:
            stat = os.stat(file_path)
            size_mb = stat.st_size / (1024 * 1024)
            
            return {
                'name': os.path.basename(file_path),
                'size': round(size_mb, 2),
                'type': self._get_file_type(file_path),
                'path': file_path
            }
        except Exception as e:
            return {'name': 'Unknown', 'size': 0, 'type': 'Unknown', 'path': file_path}
    
    def get_detailed_file_info(self, file_path: str) -> dict:
        """Get detailed file information"""
        try:
            stat = os.stat(file_path)
            size_mb = stat.st_size / (1024 * 1024)
            
            return {
                'file_name': os.path.basename(file_path),
                'file_path': os.path.abspath(file_path),
                'file_size': f"{round(size_mb, 2)} MB ({stat.st_size} bytes)",
                'file_type': self._get_file_type(file_path),
                'created': datetime.datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
                'modified': datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'permissions': oct(stat.st_mode)[-3:],
                'is_readable': os.access(file_path, os.R_OK),
                'is_writable': os.access(file_path, os.W_OK)
            }
        except Exception as e:
            return {'error': str(e)}
    
    def get_files_in_folder(self, folder_path: str) -> list:
        """Get all files in a folder (excluding subdirectories)"""
        try:
            files = []
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isfile(item_path):
                    files.append(item_path)
            return files
        except Exception as e:
            console.print(f"[red]Error reading folder: {str(e)}[/red]")
            return []
    
    def _get_file_type(self, file_path: str) -> str:
        """Determine file type based on extension"""
        ext = os.path.splitext(file_path)[1].lower()
        
        file_types = {
            '.txt': 'Text File',
            '.pdf': 'PDF Document',
            '.jpg': 'JPEG Image',
            '.jpeg': 'JPEG Image',
            '.png': 'PNG Image',
            '.doc': 'Word Document',
            '.docx': 'Word Document',
            '.xls': 'Excel Spreadsheet',
            '.xlsx': 'Excel Spreadsheet',
            '.zip': 'Zip Archive',
            '.encrypted': 'Encrypted File',
            '.py': 'Python Script',
            '.json': 'JSON File',
            '.xml': 'XML File'
        }
        
        return file_types.get(ext, 'Unknown File Type')
